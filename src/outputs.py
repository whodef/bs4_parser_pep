import csv
import datetime as dt
import logging

from prettytable import PrettyTable
from constants import BASE_DIR, DATETIME_FORMAT


def control_output(parsed_data, command_line_args):
    output_option = command_line_args.output

    output_functions = {
        'pretty': pretty_output,
        'file': lambda parsed_data: file_output(
            parsed_data, command_line_args
        ),
        'standard': standard_output,
    }

    output_function = output_functions.get(output_option, standard_output)
    output_function(parsed_data)


def standard_output(parsed_data):
    for row in parsed_data:
        print(*row)


def pretty_output(parsed_data):
    formatted_table = PrettyTable()
    formatted_table.field_names = parsed_data[0]
    formatted_table.align = 'l'
    formatted_table.add_rows(parsed_data[1:])

    print(formatted_table)


def file_output(parsed_data, command_line_args):
    output_directory = BASE_DIR / 'results'
    output_directory.mkdir(exist_ok=True)
    parser_type = command_line_args.mode
    current_time = dt.datetime.now()
    formatted_time = current_time.strftime(DATETIME_FORMAT)

    file_name = f'{parser_type}_{formatted_time}.csv'
    file_path = output_directory / file_name

    with open(file_path, 'w', encoding='utf-8') as file:
        csv_writer = csv.writer(file, dialect='unix')
        csv_writer.writerows(parsed_data)

    logging.info(f'Файл с результатами был сохранён: {file_path}')
