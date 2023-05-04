import logging
from requests import RequestException
from exceptions import ParserFindTagException, ResponseIsEmptyException


def get_response(session, url):
    try:
        fetched_response = session.get(url)
        fetched_response.encoding = 'utf-8'

        if fetched_response is None:
            error_message = 'Response is Empty'
            logging.error(error_message, stack_info=True)
            raise ResponseIsEmptyException(error_message)

    except RequestException as error:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}', stack_info=True
        )
        raise error

    return fetched_response


def find_tag(soup_object, tag_name, attrs=None):
    found_tag = soup_object.find(tag_name, attrs=(attrs or {}))

    if found_tag is None:
        error_message = f'Не найден тег {tag_name} {attrs}'
        logging.error(error_message, stack_info=True)
        raise ParserFindTagException(error_message)

    return found_tag
