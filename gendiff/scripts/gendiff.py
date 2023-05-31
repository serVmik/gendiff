#!usr/bin/env python3
from gendiff.generate_diff import generate_diff
from gendiff.parse_args import parse_args


def main():
    first_file_path, second_file_path, format = parse_args()
    print(generate_diff(first_file_path, second_file_path, format))


if __name__ == '__main__':
    main()
