#!/usr/bin/env python3
import sys
from util import convert_time_in_seconds

if __name__== '__main__':
    if len(sys.argv) != 2:
        exit(f'Usage: {sys.argv[0]} time_string')

    print(f'{sys.argv[1]} -> {convert_time_in_seconds(sys.argv[1])} secondes')