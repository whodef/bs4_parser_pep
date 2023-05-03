import re
import logging
import requests_cache

from collections import Counter
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from tqdm import tqdm

from configs import configure_argument_parser, configure_logging
from constants import BASE_DIR, EXPECTED_STATUS, MAIN_DOC_URL, PEP_URL, ERROR
from exceptions import ParserFindTagException
from outputs import control_output
from utils import find_tag, get_response


def pep(session):
    try:
        response = get_response(session, PEP_URL)
        soup = BeautifulSoup(response.text, 'lxml')
        result = Counter()

        for tbody in tqdm(soup.find_all('tbody')[:-1]):
            different_statuses = ''

            for tr in tqdm(tbody.find_all('tr'), leave=False):
                tr_status = find_tag(tr, 'td').text

                if tr_status:
                    tr_status = tr_status[1:]

                tr_url = urljoin(PEP_URL, find_tag(tr, 'a')['href'])
                pep_status = get_pep_status(session, tr_url)

                if pep_status not in EXPECTED_STATUS.get(tr_status):
                    if different_statuses:
                        different_statuses += '\n\n'

                    different_statuses += (
                        f'Несовпадающие статусы:\n{tr_url}\n'
                        f'Статус в карточке: {pep_status}\n'
                        f'Ожидаемые статусы: {EXPECTED_STATUS.get(tr_status)}'
                    )
                result[pep_status] += 1

            if different_statuses:
                logging.info(different_statuses)

        return [
            ('Статус', 'Количество'),
            *result.most_common(),
            ('Всего', sum(result.values()))
        ]
    except Exception as error:
        logging.exception(ERROR.format(error))


def whats_new(session):
    try:
        whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')
        response = get_response(session, whats_new_url)
        soup = BeautifulSoup(response.text, 'lxml')
        toc_tree_items = soup.find(class_='toctree-wrapper compound').find_all(
            'li', attrs={'class': 'toctree-l1'}
        )
        results = [('Ссылка на статью', 'Заголовок', 'Редактор, Автор')]

        for version_item in tqdm(toc_tree_items):
            article_url = urljoin(whats_new_url, version_item.a['href'])
            response = get_response(session, article_url)
            soup = BeautifulSoup(response.text, 'lxml')
            title_tag = find_tag(soup, 'h1')
            dl_tag = find_tag(soup, 'dl')
            dl_text = dl_tag.text.replace('\n', '')
            results.append([article_url, title_tag.text, dl_text])

        return results

    except Exception as error:
        logging.exception(ERROR.format(error))


def latest_versions(session):
    try:
        response = get_response(session, MAIN_DOC_URL)
        soup = BeautifulSoup(response.text, 'lxml')
        sidebar_wrapper = find_tag(soup, 'div', attrs={'class': 'sphinxsidebarwrapper'})
        ul_tags = sidebar_wrapper.find_all('ul')

        for ul in ul_tags:
            if 'All versions' in ul.text:
                version_links = ul.find_all('a')
                break
        else:
            raise ParserFindTagException(Exception)

        results = [('Ссылка на документацию', 'Версия', 'Статус')]
        pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'

        for version_link in version_links:
            link = version_link['href']
            text_match = re.search(pattern, version_link.text)

            if text_match:
                version, status = text_match.groups()
            else:
                version, status = version_link.text, ''

            results.append([link, version, status])
        return results

    except Exception as error:
        logging.exception(ERROR.format(error))


def download(session):
    try:
        downloads_url = urljoin(MAIN_DOC_URL, 'download.html')
        response = get_response(session, downloads_url)
        soup = BeautifulSoup(response.text, 'lxml')
        doc_table = find_tag(soup, 'table', {'class': 'docutils'})
        pdf_a4_tag = find_tag(doc_table, 'a', {'href': re.compile(r'.+pdf-a4\.zip$')})
        pdf_a4_link = pdf_a4_tag['href']
        archive_url = urljoin(downloads_url, pdf_a4_link)
        response = session.get(archive_url)
        file_name = archive_url.split('/')[-1]
        downloads_folder = BASE_DIR / 'downloads'
        downloads_folder.mkdir(exist_ok=True)
        archive_path = downloads_folder / file_name

        with open(archive_path, 'wb') as file:
            file.write(response.content)

        logging.info(f'Архив был загружен и сохранён:{archive_path}')

    except Exception as error:
        logging.exception(ERROR.format(error))


def get_pep_status(session, url):
    response = get_response(session, url)
    soup = BeautifulSoup(response.text, 'lxml')

    return soup.find(string='Status').parent.find_next_sibling('dd').text


MODE_TO_FUNCTION = {
    'pep': pep,
    'latest-versions': latest_versions,
    'whats-new': whats_new,
    'download': download,
}


def main():
    try:
        configure_logging()
        logging.info(('' + '=' * 60) + ' Начало ' + ('' + '=' * 60))
        arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
        args = arg_parser.parse_args()
        logging.info(f'Аргументы командной строки: {args}')
        session = requests_cache.CachedSession()

        if args.clear_cache:
            session.cache.clear()

        parser_mode = args.mode
        results = MODE_TO_FUNCTION[parser_mode](session)

        if results:
            control_output(results, args)

        logging.info(
            ('' + '=' * 47) + ' Парсер успешно завершил работу! ' + ('' + '=' * 48 + '\n')
        )

    except Exception as error:
        logging.exception(ERROR.format(error))


if __name__ == '__main__':
    main()
