"""
Ryan Pepper (2018)

This script contains the main entrypoint to the folder-analyse application.

"""

import argparse
import os
import sys
#from process import process_file, process_dir


def parse_args():
    parser = argparse.ArgumentParser(
        description="%(prog)s [options]"
                    "Produce wordcount statistics for files in a directory."
        )

    parser.add_argument('path', type=str,
                        help="Path to a directory or a file.")

    parser.add_argument('-r', '--report', action='store_true',
                        help="Generate a report about a directory")

    parser.add_argument('-t', '--type', type=str, default='.txt',
                        help="If path is to a directory, file extension\n"
                             "of files that to be processed.")

    parser.add_argument('-c', '--case-insensitive', action='store_true',
                        help="By default, processing is case sensitive.\n"
                             "Add this flag to make it case insensitive")

    parser.add_argument('-e', '--exclude', type=str, nargs='+',
                        help="Remove these strings from the text before\n"
                             "processing.")

    return parser.parse_args()


def exit(message):
    """
    exit(message)

    Quits the running application and gives an error message
    of message.
    """
    print(message)
    sys.exit()
