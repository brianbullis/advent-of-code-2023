"""
Advent of Code 2023 - Day 1, Part 1
Brian Bullis - brian [AT] bullis [DOT] me
"""

if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        data = input_file.read().splitlines()

        # every line contains digits that serve as the calibration values for that line
        calibration_values = []

        for line in data:
            # gather the digits contained in that line
            digits = [i for i in line if i.isdigit()]

            # make a 2-digit number out of the first and last digits of the line
            line_value = digits[0] + digits[-1]
            calibration_values.append(int(line_value))

        # the answer is the sum of all the calibration values
        print(sum(calibration_values))
