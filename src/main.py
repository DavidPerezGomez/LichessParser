import sys
from game_parser import GameParser
from writer import Writer

if __name__ == '__main__':
    if len(sys.argv) > 1:
        output_path = sys.argv[1]
    else:
        output_path = './lichess.csv'

    data = sys.stdin.read().splitlines()
    total_lines = len(data)
    print('Total lines:', total_lines)

    parser = GameParser()
    writer = Writer(output_path, parser.get_fields(), sep=';')

    writer.open()
    writer.write_header()

    game_lines = []
    empty_lines = 0
    lines_parsed = 0
    games_parsed = 0
    try:
        for line in data:
            if line:
                game_lines.append(line)
            else:
                empty_lines += 1
                if empty_lines == 2:
                    game_data = parser.parse_game(game_lines)
                    writer.write_game(game_data)
                    game_lines = []
                    empty_lines = 0
                    games_parsed += 1
            lines_parsed += 1
            percent = lines_parsed * 100 // total_lines
            print("Lines parsed: {} ({}%) - Games parsed: {}".format(lines_parsed, percent, games_parsed), end="\r")
        print("\n")
    except Exception as ex:
        print("\nError at line", lines_parsed)
        print(ex)
    finally:
        writer.close()
