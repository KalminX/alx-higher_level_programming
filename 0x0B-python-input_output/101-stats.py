#!/usr/bin/python3
"""My file module"""
import sys


def stats():
    """Method to append to a file"""
    data = sys.stdin.readlines()
    total_file_size = 0
    status_counts = {200: 0, 301: 0, 400: 0,
                     401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    for line in data:
        parts = line.split()
        if len(parts) >= 10:
            file_size = int(parts[-1])
            total_file_size += file_size
            status_code = int(parts[-2])
            if status_code in status_counts:
                status_counts[status_code] += 1

    return print_statistics(total_file_size, status_counts)
        

def print_statistics(total_file_size, status_counts):
    print(f"Total file size: {total_file_size}")
    for status_code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")
