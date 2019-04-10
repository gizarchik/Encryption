import string


def encode_caesar(key, input_file, output_file):
    encode_vigener(string.ascii_lowercase[key], input_file, output_file)


def encode_vigener(key, input_file, output_file):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase

    index = 0
    key_length = len(key)
    letter_length = len(lowercase_letters)
    for lines in input_file:
        for letter in lines:
            index %= key_length
            if letter.islower():
                letter_number = (lowercase_letters.find(letter) + lowercase_letters.find(key[index])) % letter_length
                output_file.write(lowercase_letters[letter_number])
                index += 1
            elif letter.isupper():
                letter_number = (uppercase_letters.find(letter) + lowercase_letters.find(key[index])) % letter_length
                output_file.write(uppercase_letters[letter_number])
                index += 1
            elif string.printable.find(letter) != -1:
                output_file.write(letter)
            else:
                raise UnicodeError('Have non-ascii letters')


def encode_vernam(key, input_file, output_file):
    def xor(message, key):
        return bytes(i ^ j for i, j in zip(message, key)).decode()
    output_file.write(xor(input_file.read().encode(), key.read().encode()))

