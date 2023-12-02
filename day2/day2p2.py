"""
Advent of Code 2023 - Day 2, Part 2
Brian Bullis - brian [AT] bullis [DOT] me
"""

# how many cubes of each color would we need in a bag to make each game valid?
if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        data = input_file.read().splitlines()
        powers = []
        for line in data:
            # we will now gather data from each reveal and track the largest number of cubes of each color
            max_cubes = {'red': 0, 'green': 0, 'blue': 0}

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

                    # check each color's value, if it exceeds our current maximum, replace it
                    if reveal_data[1] == 'red' and int(reveal_data[0]) > max_cubes['red']:
                        max_cubes['red'] = int(reveal_data[0])
                    elif reveal_data[1] == 'green' and int(reveal_data[0]) > max_cubes['green']:
                        max_cubes['green'] = int(reveal_data[0])
                    elif reveal_data[1] == 'blue' and int(reveal_data[0]) > max_cubes['blue']:
                        max_cubes['blue'] = int(reveal_data[0])

            # calculate the "power" of this game - multiply the necessary number of cubes for each color
            power = max_cubes['red'] * max_cubes['green'] * max_cubes['blue']
            powers.append(power)

        # the answer is the sum of the game powers
        print(sum(powers))
