#!usr/bin/env python3
from gendiff.generate_diff import generate_diff
from gendiff.parse_args import parse_args


def main():
    args = parse_args()
    print(generate_diff(args.first_filepath, args.second_filepath,
                        args.format))


if __name__ == '__main__':
    main()
