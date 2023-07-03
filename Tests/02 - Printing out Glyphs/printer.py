#!/bin/env python3

import argparse

argparser = argparse.ArgumentParser(description="Prints out given sprites")
argparser.add_argument("file", help="File to print out")
argparser.add_argument("-c", "--color", help="Color to print out glyphs in (0-255)")
args = argparser.parse_args()

VERSION = "0.0.1" 

with open(args.file) as f:
    if args.color is not None:
        # print out color escape
        print("\033[38;5;{}m".format(args.color))
    # print out all glyphs in file, handling any inline variables in {}
    for line in f:
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        print(line.format(**globals()))
    # print out color reset escape
    if args.color is not None:
        print("\033[0m")