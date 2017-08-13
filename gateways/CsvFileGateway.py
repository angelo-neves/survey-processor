import csv
import os
import sys
import itertools


class CsvFileGateway(object):

    def __init__(self, file_path, first_line_is_header=False):
        self.lines = []
        self.keys = []
        self.lines_with_keys = []
        self.absolute_path = self._get_absolute_path(file_path)

        self._read_lines(first_line_is_header)
        if first_line_is_header:
            self._build_lines_with_headers()

    def _get_absolute_path(self, file_path):
        if file_path[0] != '/':
            absolute_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', file_path))
        else:
            absolute_path = file_path
        return absolute_path

    def _read_lines(self, read_keys=False):
        try:
            with open(self.absolute_path) as csv_file:
                csv_reader = csv.reader(csv_file)
                keys_are_set = False
                for line in csv_reader:
                    if not keys_are_set and read_keys:
                        self.keys = line
                        keys_are_set = True
                    else:
                        self.lines.append(line)
        except (OSError, IOError):
            sys.exit('File not found: ' + self.absolute_path)

    def _build_lines_with_headers(self):
        for values in self.lines:
            line_values_with_keys = dict(zip(self.keys, values))
            self.lines_with_keys.append(line_values_with_keys)

    def get_all_lines(self):
        return self.lines

    def get_all_lines_with_keys(self):
        return self.lines_with_keys
