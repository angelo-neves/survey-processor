class CsvFileGateway(object):

    def __init__(self):
        self.lines = []
        self.lines_with_keys = []

    def get_all_lines(self):
        return self.lines

    def get_all_lines_with_keys(self):
        return self.lines_with_keys
