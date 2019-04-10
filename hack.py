import string
import collections
import decode


def hack_caesar(analysis_file, input_file, output_file, input_file_name):
    analysis_data = analysis_file.read().split()
    analysis_data = list(map(int, analysis_data))
    lowercase_letters = string.ascii_lowercase
    letter_counter = collections.Counter()

    for line in input_file:
        for letter in line:
            if letter.isalpha():
                letter_counter[letter.lower()] += 1

    shift = int()
    max_mutual_match_index = 0
    for i in range(26):
        mutual_match_index = 0
        for j in range(26):
            mutual_match_index += analysis_data[j] * letter_counter[lowercase_letters[(j + i) % 26]]
        if mutual_match_index > max_mutual_match_index:
            max_mutual_match_index = mutual_match_index
            shift = i

    input_file.close()
    input_file = open(input_file_name)
    decode.decode_caesar(shift, input_file, output_file)
