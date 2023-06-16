import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference'
    )
    parser.add_argument('first_filepath')
    parser.add_argument('second_filepath')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output')

    args = parser.parse_args()
    return args
