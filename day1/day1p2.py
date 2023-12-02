"""
Advent of Code 2023 - Day 1, Part 2
Brian Bullis - brian [AT] bullis [DOT] me
"""
import regex

# the lines actually contain numbers spelled out! we have to take those into account.
if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        data = input_file.read().splitlines()

        # every line contains digits that serve as the calibration values for that line
        calibration_values = []

        # map the spelled out numbers to their digits
        number_words = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }

        for line in data:
            digits = []

            # using a regex matching digits or all the spelled out words, get a list of the numbers in the line
            matches = regex.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)

            # gather the numbers contained in that line - convert to a digit if spelled out
            for number in matches:
                if number in number_words:
                    digits.append(number_words[number])
                else:
                    digits.append(number)

            # make a 2-digit number out of the first and last digits of the line
            line_value = digits[0] + digits[-1]
            calibration_values.append(int(line_value))

        # the answer is the sum of all the calibration values
        print(sum(calibration_values))
