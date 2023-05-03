# Проект парсинга PEP

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=informational)](https://www.python.org/)
[![BeautifulSoup4](https://img.shields.io/badge/-BeautifulSoup4-464646?style=flat&logo=BeautifulSoup4&logoColor=ffffff&color=9cf)](https://www.crummy.com/software/BeautifulSoup/)
[![Logging](https://img.shields.io/badge/-Logging-464646?style=flat&logo=Logging&logoColor=ffffff&color=informational)](https://docs.python.org/3/library/logging.html)
[![Prettytable](https://img.shields.io/badge/-Prettytable-464646?style=flat&logo=Prettytable&logoColor=ffffff&color=9cf)](https://github.com/jazzband/prettytable)

Проект "Парсинг документов PEP" предназначен для удобства доступа к документации, теперь информация будет всегда под рукой.
Развитие языка Python сопровождается документами PEP — Python Enhancement Proposal.
К примеру:

- PEP 8 — Руководство по стилю кода Python
- PEP 20 — Дзен Python (The Zen of Python)
- PEP 257 — конвенция о докстрингах
- PEP 484 — подсказки типов (Type Hints)
- PEP 526 — аннотация переменных и так далее

Каждый из документов PEP относится [к разным типам](https://peps.python.org/#pep-types-key) и может находиться [в разных статусах](https://peps.python.org/#pep-status-key).

## Описание

У проекта есть **4 опции работы парсинга**

- `pep` данные о статусе документа берутся со страницы каждого PEP
- `whats-new` собирает ссылки на статьи о нововведениях и прочую справочную информацию
- `latest-versions` собирает информацию о версиях Python: номера, статус и ссылки на документацию
- `download` скачивает архив с документацией Python на локальный диск в директорию ./src/downloads/
- **Необязательные аргументы**
  - `-h`, `--help` — выводит вспомогательную информацию о работе парсера
  - `-c`, `--clear-cache` — удаляет cache пред стартом
  - `-o {pretty, file}`, `--output {pretty, file}` — дополнительные способы вывода данных. Параметр 'pretty' выводит данные в терминале в виде таблицы, параметр 'file' сохраняет данные в csv-файл в директории results/.

## Запуск проекта

1. Клонируйте репозиторий и перейдите в него
    ```bash
   https://github.com/whodef/bs4_parser_pep.git
   ```
2. Установите и активируйте виртуальное окружение
    ```bash
   python3 -m venv venv
   ```
3. Установите зависимости из файла requirements.txt
    ```bash
    pip3 install -r requirements.txt
    ```
4. Через командную строку в директории src запустите скрипт:
    ```bash
    python3 main.py MODE -ARGS
    ```
    _Где `MODE` — это название режима работы парсинга ('pep', 'whats-new', 'latest-versions', 'download'), а `-ARGS` — это перечисление необязательных аргументов (--help, '--clear-cache' и т.д.)._


## Автор проекта

**[Tatiana Seliuk](https://github.com/whodef)**