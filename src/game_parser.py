import re
from parser import Parser


class GameParser(Parser):
    EVENT_KEY = 'Event'
    RESULT_KEY = 'Result'
    DATE_KEY = 'UTCDate'
    TIME_KEY = 'UTCTime'
    WHITE_ELO_KEY = 'WhiteElo'
    BLACK_ELO_KEY = 'BlackElo'
    ECO_KEY = 'ECO'
    OPENING_KEY = 'Opening'
    TIME_CONTROL_KEY = 'TimeControl'
    TERMINATION_KEY = 'Termination'
    MOVES_KEY = 'Moves'

    def __init__(self):
        super().__init__()
        self._fields = [
            self.EVENT_KEY,
            self.RESULT_KEY,
            self.DATE_KEY,
            self.TIME_KEY,
            self.WHITE_ELO_KEY,
            self.BLACK_ELO_KEY,
            self.ECO_KEY,
            self.OPENING_KEY,
            self.TIME_CONTROL_KEY,
            self.TERMINATION_KEY,
            self.MOVES_KEY
        ]

    def get_fields(self):
        return self._fields

    def parse_game(self, game_lines):
        data = {}

        for field in self._fields:
            data[field] = None

        for line in game_lines[:-1]:
            key, value = self.parse_line(line)
            if key in self._fields:
                if key == self.EVENT_KEY:
                    r = re.compile("\shttp.*")
                    value = r.sub('', value)
                data[key] = value

        move_list, checkmate = self.parse_moves(game_lines[-1])

        data[self.MOVES_KEY] = move_list

        if data[self.TERMINATION_KEY] != 'Time forfeit':
            if data[self.RESULT_KEY] == '1/2-1/2':
                termination = 'Draw'
            elif checkmate:
                termination = 'Checkmate'
            else:
                termination = 'Resignation'

            data[self.TERMINATION_KEY] = termination

        return data
