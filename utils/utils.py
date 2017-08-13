import sys
import csv


def get_csv_reader(file_path):
    try:
        csv_reader = csv.reader(open(file_path))
    except (OSError, IOError):
        sys.exit('File not found: ' + file_path)

    return csv_reader


def get_average_from_list(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        total += number
    return total / len(list_of_numbers)


def skip_one_line(file_iterator):
    next(file_iterator)