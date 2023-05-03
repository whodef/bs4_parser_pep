from pathlib import Path


# Base Directory

BASE_DIR = Path(__file__).parent


# URLs to parse

MAIN_DOC_URL = 'https://docs.python.org/3/'

PEP_URL = 'https://peps.python.org/'


# Formats

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

DATETIME_LOG_FORMAT = '%d.%m.%Y %H:%M:%S'

LOG_FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'


# Statuses

EXPECTED_STATUS = {
    'A': ['Active', 'Accepted'],
    'D': ['Deferred'],
    'F': ['Final'],
    'P': ['Provisional'],
    'R': ['Rejected'],
    'S': ['Superseded'],
    'W': ['Withdrawn'],
    '': ['Draft', 'Active'],
}

# Constants

ERROR = 'Ошибка: {}'
