import re


class Parser:
    def __init__(self):
        self._regex_line = re.compile('\[(\w*)\s"(.*)"]')
        self._regex_annotations_1 = re.compile('{.*?}\s')
        self._regex_annotations_2 = re.compile('[?!]')
        self._regex_annotations_3 = re.compile('\d*\.+\s')

    def parse_line(self, line):
        return self._regex_line.match(line).groups()

    def parse_moves(self, pgn_line):
        move_list = self._regex_annotations_1.sub('', pgn_line)  # remove eval and clock info
        move_list = self._regex_annotations_2.sub('', move_list)  # remove move marks
        move_list = self._regex_annotations_3.sub('', move_list)  # remove numbers

        # remove game result
        if move_list[-7:] == '1/2-1/2':
            move_list = move_list[:-8]
        else:
            move_list = move_list[:-4]

        # check for mate
        checkmate = move_list and move_list[-1] == '#'

        return move_list, checkmate
