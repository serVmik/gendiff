#!usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference')
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()


def main():
    pass


if __name__ == '__main__':
    main()
