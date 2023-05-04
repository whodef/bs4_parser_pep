import argparse
import logging
from logging.handlers import RotatingFileHandler

from constants import (
    BASE_DIR, DATETIME_LOG_FORMAT, LOG_FORMAT, OUTPUT_CHOICES
)


def configure_argument_parser(available_modes):
    parser = argparse.ArgumentParser(description='Парсинг документов PEP')
    parser.add_argument(
        'mode', choices=available_modes, help='Режимы работы парсера'
    )
    parser.add_argument(
        '-c', '--clear-cache', action='store_true', help='Очистка кеша'
    )
    parser.add_argument(
        '-o',
        '--output',
        choices=OUTPUT_CHOICES,
        help='Дополнительные способы вывода данных',
    )
    return parser


def configure_logging():
    log_dir = BASE_DIR / 'logs'
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'parser.log'
    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=10**6, backupCount=5, encoding='utf-8'
    )
    logging.basicConfig(
        datefmt=DATETIME_LOG_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler()),
    )
