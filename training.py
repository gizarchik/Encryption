import string
import collections


def training_caesar(input_file, output_file):
    lowercase_letters = string.ascii_lowercase
    letter_counter = collections.Counter()

    for line in input_file:
        for letter in line:
            if letter.isalpha():
                letter_counter[letter.lower()] += 1

    for i in range(26):
        output_file.write(str(letter_counter[lowercase_letters[i]]) + ' ')
