#!usr/bin/env python3
import argparse
from gendiff.display_in_format import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference'
    )
    parser.add_argument('first_filepath')
    parser.add_argument('second_filepath')
    parser.add_argument(
        '-f', '--format', default="stylish",
        choices=['stylish', 'plain', 'json'],
        help='set format of output'
    )
    args = parser.parse_args()

    print(generate_diff(
        args.first_filepath,
        args.second_filepath,
        args.format
    ))


if __name__ == '__main__':
    main()
