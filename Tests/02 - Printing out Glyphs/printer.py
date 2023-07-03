#!/bin/env/ Python 3

import argparse

argparser = argparse.ArgumentParser(description="Prints out given sprites")
argparser.add_argument("file", help="File to print out")
args = argparser.parse_args()

with open(args.file) as file:
    for line in file:
        print(line, end="")