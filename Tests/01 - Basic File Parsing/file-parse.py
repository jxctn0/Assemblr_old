#!/bin/env python3

import re
import argparse
# Added

# GLOBALS
# global ACCUMULATOR
ACCUMULATOR = 0
RAM_SIZE = 1024
RAM = [[0]*RAM_SIZE]
STACK = []

# Convert each line into an array
def tokenise(line):
    # remove comments if any
    line = line.split(";")[0].strip()
    tokens = re.split(r'\s+', line) #
    return tokens

# 'run' file
def execute(line):
    global ACCUMULATOR

    tokens = tokenise(line)
    print("t", tokens)

    opcode = tokens[0]
    params = tokens[1:]
    print("p",params)

    if opcode == "HLT":
        # Code to execute if the opcode is "HLT"
        print("Halt program")
        quit()
    elif opcode == "SAV":
        # Code to execute if the opcode is "SAV"
        RAM = {RAM,params[0],ACCUMULATOR}
        print("Save value")
    elif opcode == "LDA":
        # Code to execute if the opcode is "LDA"
        print("Load value")
    elif opcode == "ADD":
        # Code to execute if the opcode is "ADD"
        ACCUMULATOR += int(params[0])
        print("Add values")
    elif opcode == "SUB":
        # Code to execute if the opcode is "SUB"
        ACCUMULATOR -= int(params[0])
        print("Subtract values")
    elif opcode == "JMP":
            # Code to execute if the opcode is "JMP"
        print("Jump to location")
    elif opcode == "JEZ":
        # Code to execute if the opcode is "JEZ"
        print("Jump if equal to zero")
    elif opcode == "JGZ":
        # Code to execute if the opcode is "JGZ"
        print("Jump if greater than zero")
    elif opcode == "JLZ":
        # Code to execute if the opcode is "JLZ"
        print("Jump if less than zero")
    elif opcode == "INP":
        # Code to execute if the opcode is "INP"
        print("Input value")
    elif opcode == "OUT":
        # Code to execute if the opcode is "OUT"
        print(ACCUMULATOR)
        print("Output value")
    elif opcode == "SIG":
        # Code to execute if the opcode is "SIG"
        print("Send signal")
    elif opcode == "BAD":
        # Code to execute if the opcode is "BAD"
        print("Bad opcode")
    elif opcode == "BOR":
        # Code to execute if the opcode is "BOR"
        print("Bitwise OR")
    elif opcode == "BXR":
        # Code to execute if the opcode is "BXR"
        print("Bitwise XOR")
    elif opcode == "DLY":
        # Code to execute if the opcode is "DLY"
        print("Delay")
    else:
        # Code to execute if the opcode doesn't match any of the given opcodes
        print("Unknown opcode " + opcode)
        quit()

# Argument handling
parser = argparse.ArgumentParser(description='')

# Add arguments
parser.add_argument('-v', '--verbose', action='store_true',
                    help='Enable Verbose')
# Add the 'filename' argument
parser.add_argument('-f','--filename', metavar='FILE', type=str,
                    help='The input filename')


#set args
args = parser.parse_args()


''' MAIN LOOP '''
if __name__ == '__main__':
    with open(args.filename) as program_file:
        for line in program_file:
            print(line)
            execute(line)
            if args.verbose:
                 print(u"\u001b[31mACCUMULATOR:", ACCUMULATOR, u"\u001b[0m")