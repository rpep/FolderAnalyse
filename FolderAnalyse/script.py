"""
Ryan Pepper (2018)

This script contains the main entrypoint to the folder-analyse application.

"""

import argparse
import os
import sys
from FolderAnalyse.process import process_dir, process_file

def parse_args():
    parser = argparse.ArgumentParser(
        description="%(prog)s [options]"
                    "Produce wordcount statistics for files in a directory."
        )

    parser.add_argument('path', type=str,
                        help="Path to a directory or a file.")

    parser.add_argument('-r', '--report', type=str, default=None,
                        help="Generate a report about a directory and\n"
                             "save it to this filename")

    parser.add_argument('-t', '--type', type=str, default='.txt',
                        help="If path is to a directory, file extension\n"
                             "of files that to be processed.")

    parser.add_argument('-c', '--case-insensitive', action='store_true',
                        help="By default, processing is case sensitive.\n"
                             "Add this flag to make it case insensitive")

    return parser.parse_args()


def exit(message):
    """
    exit(message)

    Quits the running application and gives an error message
    of message.
    """
    print(message)
    sys.exit()


def main():
    args = parse_args()
    print(dir(args))
    path = args.path
    extension = args.type
    report = args.report
    case_insensitive = args.case_insensitive

    directory = os.path.isdir(path)
    file = os.path.isfile(path)

    if file:
         stats_text, report_text = process_file(file, report)

    elif directory:
         stats_text, report_text = process_dir(path, extension, report)

    else:
         exit("Path does not exist")







if __name__ == '__main__':
    main()
