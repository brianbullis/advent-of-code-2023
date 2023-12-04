"""
Advent of Code 2023 - Day 3, Part 1
Brian Bullis - brian [AT] bullis [DOT] me
"""
import regex

with open('input.txt', 'r') as input_file:
    data = input_file.read().splitlines()
    parsed = {}
    line_count = 0
    for line in data:
        symbols = regex.finditer(r'\@|\#|\$|\%|\^|\&|\*|\-|\_|\=|\+|\/', line)
