#!usr/bin/env python3
from gendiff import parse_plain
from gendiff.gendiff_tools import get_dct_from_file


def main():
    dct1 = get_dct_from_file('tests/fixtures/file1.json')
    dct2 = get_dct_from_file('tests/fixtures/file2.json')
    parse_plain.parse_plain(dct1, dct2)


if __name__ == '__main__':
    main()
