class CsvFileGateway(object):

    def __init__(self, lines):
        self.lines = lines

    def get_all_lines(self):
        return self.lines
