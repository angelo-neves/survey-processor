import csv
import os
import sys


class CsvFileGateway(object):
    lines = []

    def __init__(self, file_path):
        self.lines = []
        if file_path[0] != '/':
            absolute_path = self._get_absolute_path(file_path)
        else:
            absolute_path = file_path

        try:
            with open(absolute_path) as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    self.lines.append(line)

        except (OSError, IOError):
            sys.exit('File not found: ' + absolute_path)

    def _get_absolute_path(self, relative_path):
        absolute_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', relative_path))
        return absolute_path

    def get_all_lines(self):
        return self.lines
