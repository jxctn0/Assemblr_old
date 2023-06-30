#!/bin/env python3

import re
import argparse
# Added

# GLOBALS
ACCUMULATOR = 0

# initialise RAM
RAM_SIZE = 255 # Specify the desired size of the dictionary (256 for keys 0 to ff)
RAM = {hex(i)[2:].zfill(2): 0 for i in range(RAM_SIZE)}

print("RAM", RAM)
print(len(RAM))

# initialise STACK
global STACK
STACK = []

# initialise line counter
LINE_COUNTER = 0


# MNEMONICS
# HLT - Halt the program
def hlt():
    quit()

# SAV - Save the value in the accumulator to the address specified
def SAV(value):
    global RAM
    # Find the first available space in the RAM dictionary
    available_key = None
    for key, val in RAM.items():
        if val == 0:
            available_key = key
            break
    
    if available_key is not None:
        # Update the RAM dictionary with the value
        RAM[available_key] = value
        print(f"Value {value} saved at key {available_key}")
    else:
        print("No available space in RAM to save the value.")
        MemoryError()
    print("RAM", RAM)



# Convert each line into an array
def tokenise(line):
    # remove comments if any
    line = line.split(";")[0].strip()
    #remove any whitespace
    tokens = re.split(r'\s+', line)
    return tokens

# Execute a line
def execute(line):
    global ACCUMULATOR, RAM, STACK, LINE_COUNTER

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
        SAV(params[0])
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
        print(f"Line {LINE_COUNTER} Unknown opcode " + opcode)
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
        # Execute each line iteratively
        for line in program_file:
            if line != "\n":
                execute(line)
                if args.verbose:
                    print(u"\u001b[31mACCUMULATOR:", ACCUMULATOR, u"\u001b[0m")