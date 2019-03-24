import argparse
import sys


def parse():
    parser = argparse.ArgumentParser(description='encode, decode, hack or training')

    action_types = ['encode', 'decode', 'hack', 'training']
    parser.add_argument('type', choices=action_types)

    if sys.argv[1] == 'encode' or sys.argv[1] == 'decode':
        cipher_types = ['caesar', 'vigenere', 'vernam']

        parser.add_argument('--cipher', choices=cipher_types)
        parser.add_argument('--key')
        parser.add_argument('--input-file')
        parser.add_argument('--output-file')
    elif sys.argv[1] == 'training':
        parser.add_argument('--cipher', choices=['caesar'])
        parser.add_argument('--input-file')
        parser.add_argument('--output-file')
    elif sys.argv[1] == 'hack':
        parser.add_argument('--cipher', choices=['caesar'])
        parser.add_argument('--frequency_analysis-file')
        parser.add_argument('--input-file')
        parser.add_argument('--output-file')

    return vars(parser.parse_args())
