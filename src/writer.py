class Writer:

    def __init__(self, output_path, fields, sep=','):
        self._output_path = output_path
        self._fields = fields
        self._sep = sep
        self._file = None

    def open(self):
        self._file = open(self._output_path, 'w')

    def close(self):
        self._file.close()

    def write_header(self):
        line = self._sep.join(self._fields)
        self._write_line(line)

    def write_game(self, game_data):
        data = []
        for field in self._fields:
            data.append(game_data[field])
        line = self._sep.join(data)
        self._write_line(line)

    def _write_line(self, line):
        if self._file and not self._file.closed:
            self._file.write(line + '\n')
