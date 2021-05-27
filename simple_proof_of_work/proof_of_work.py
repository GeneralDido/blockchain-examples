import hashlib
import random
import string
import argparse


def make_hex():
    hex_nums = list(string.digits + 'abcdef')
    return '0000' + ''.join(random.sample(hex_nums, 4))


def solution(input_string):
    while True:
        sol = make_hex()
        bytes_input = bytes.fromhex(input_string)
        bytes_solution = bytes.fromhex(sol)
        encoded_input = bytes_solution + bytes_input
        output = hashlib.sha256(encoded_input).hexdigest()
        if output[-4:] == 'cafe':
            print(output)
            print(sol)
            return output, sol


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input String")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse()
    solution(args.input)