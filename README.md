# Проект парсинга PEP

Проект "Парсинг документов PEP". Развитие языка Python сопровождается документами PEP — Python Enhancement Proposal.
Таких как:

- PEP 8 — Руководство по стилю кода Python
- PEP 20 — Дзен Python (The Zen of Python)
- PEP 257 — конвенция о докстрингах
- PEP 484 — подсказки типов (Type Hints)
- PEP 526 — аннотация переменных и так далее

Каждый из документов PEP относится [к разным типам](https://peps.python.org/#pep-types-key) и может находиться [в разных статусах](https://peps.python.org/#pep-status-key).

## Запуск проекта

- Клонируйте репозиторий и перейдите в него
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt

```bash
pip install -r requirements.txt
```
- Через командную строку в директории src запустите скрипт:

```bash
python main.py MOD -ARGS
```
_Где `MOD` — это название режима работы, а `-ARGS` — это перечисление необязательных аргументов._


## Автор проекта

**[Tatiana Seliuk](https://github.com/whodef)**