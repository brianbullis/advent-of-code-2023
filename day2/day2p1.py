"""
Advent of Code 2023 - Day 2, Part 1
Brian Bullis - brian [AT] bullis [DOT] me
"""

if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        data = input_file.read().splitlines()
        valid_games = []
        for line in data:
            valid_game = True

            # each line starts with 'Game #:' - get the game ID
            game_record = line.split(':')
            game_id = game_record[0].split()[1]

            # the second part of each line is the draws that were taken from the bag, separated by ';'
            game_cubes = game_record[1].split(';')

            for reveal in game_cubes:
                # each reveal of the cubes has a number and a color of cubes, separated by ','
                cubes_shown = reveal.split(', ')

                for count in cubes_shown:
                    # get the data of the reveal as a list - number then color, space separated
                    reveal_data = count.split()

                    # validate the number of cubes of each color is within the contraints of the rules, invalidate it
                    # if there's too many cubes
                    if reveal_data[1] == 'red' and int(reveal_data[0]) > 12:
                        valid_game = False
                    elif reveal_data[1] == 'green' and int(reveal_data[0]) > 13:
                        valid_game = False
                    elif reveal_data[1] == 'blue' and int(reveal_data[0]) > 14:
                        valid_game = False

            # if the game we're on is valid, put its ID in the valid games
            if valid_game:
                valid_games.append(int(game_id))

        # the answer is the sum of the IDs of valid games
        print(sum(valid_games))
