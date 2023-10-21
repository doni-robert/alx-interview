#!/usr/bin/python3
""" Contains the log_parsing module """
import sys
import re


total_size = 0
status_code_count = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
        }
pattern = (
        r'^(\d+\.\d+\.\d+\.\d+)\s+-\s+'
        r'\[([^\]]+)]\s+"GET\s+\/projects\/\d+\s+HTTP\/1\.1"\s+'
        r'(\d+)\s+(\d+)$'
        )
count = 0

try:
    for line in sys.stdin:
        match = re.match(pattern, line)
        if match:
            total_size += int(match.group(4))

            status_code = match.group(3)
            if status_code in status_code_count:
                status_code_count[status_code] += 1

        count += 1
        if count == 10:
            print(f'File size: {total_size}')
            for k, v in status_code_count.items():
                print(f'{k}: {v}')
            count = 0
except KeyboardInterrupt:
    print(f'File size: {total_size}')
    for k, v in status_code_count.items():
        print(f'{k}: {v}')

