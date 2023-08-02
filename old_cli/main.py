#!/bin/env python3

import re
import argparse

import instruction_set, startup

# Constants
ACCUMULATOR = 0


global BIT_LENGTH
BIT_LENGTH = 1024

ram = []


# initialise ROM (instruction set)
# ROM is a dictionary of functions
# Each function is a different instruction

ROM = {
    "HLT": instruction_set.HLT,
    "SAV": instruction_set.SAV,
    "LDA": instruction_set.LDA,
    "ADD": instruction_set.ADD,
    "SUB": instruction_set.SUB,
    "JMP": instruction_set.JMP,
    "JEZ": instruction_set.JEZ,
    "JGZ": instruction_set.JGZ,
    "JLZ": instruction_set.JLZ,
    "JNZ": instruction_set.JNZ,
    "INP": instruction_set.INP,
    "OUT": instruction_set.OUT,
    "SIG": instruction_set.SIG,
    "BAD": instruction_set.BAD,
    "BOR": instruction_set.BOR,
    "BXR": instruction_set.BXR,
    "DLY": instruction_set.DLY
}

# Show ram in neat, tabulated format of f columns
# print out ram
def showram(ram):
    print("""
╔═══╦══════╤══════╤══════╤══════╤══════╤══════╤══════╤══════╤══════╤══════╤══════╤══════╤══════╤══════╤══════╤══════╗
║   ║  0   │ 1    │ 2    │  3   │  4   │  5   │  6   │  7   │  8   │  9   │  a   │  b   │  c   │  d   │  e   │  f   ║""")
    
    for i in range(0, len(ram)):

        print("╟───╫──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────╢")
        
        # convert i to a hex string
        rownum = str(hex(i)[2:].zfill(1))

        print("║ " + rownum, end=" ║")

        for j in range(0, len(ram[str(hex(i)[2:].zfill(2))])-1):
            print(" " + str(ram[str(hex(i)[2:].zfill(2))][j]), end=" │")
        print(" " + str(ram[str(hex(i)[2:].zfill(2))][len(ram[str(hex(i)[2:].zfill(2))])-1]), end=" ║\n")
    
    print("╚═══╩══════╧══════╧══════╧══════╧══════╧══════╧══════╧══════╧══════╧══════╧══════╧══════╧══════╧══════╧══════╧══════╝\n")


# initialise STACK
global STACK
STACK = []


# initialise STACK functions
# push if stack isn't full
def push(value):
    global STACK
    if len(STACK) < 16:
        STACK.append(value)
    else:
        print("Stack Overflow Error")
        exit(4)

# pop if stack isn't empty
def pop():
    global STACK
    if len(STACK) > 0:
        return STACK.pop()
    else:
        print("Stack Underflow Error")
        exit(5)


# initialise line counter
LINE_COUNTER = 0

# set global VERBOSE
VERBOSE = None


# Initialise Ports
PORTS = [0] * 16 # Makes 16 different "port" options

# Load the program into ram
def load_program(program_file):
    global ram, LINE_COUNTER
    # Iterate over each line in the file
    for line in program_file:
        # If the line is not empty
        if line != "\n":
            # Remove the newline character
            line = line.strip()
            # Split the line into tokens
            tokens = re.split(r"\s+", line)
            # Get the first token
            opcode = tokens[0]
            # Get the remaining tokens
            params = tokens[1:]

            # If the opcode is SAV
            if opcode == "SAV":
                # Get the first parameter
                value = params[0]
                # Save the value to the ram
                ram[hex(LINE_COUNTER)[2:].zfill(2)] = int(value)
                # Increment the line counter
                LINE_COUNTER += 1
            else:
                # If the opcode is not SAV, increment the line counter
                LINE_COUNTER += 1
    

# Helper functions

# Error Text
def error(text, code=0):
    print("\u001b[31m" + text + "\u001b[0m")
    startup.errorcodes
    exit(code)

def verbose():
    global VERBOSE
    if VERBOSE:
        print("ACCUMULATOR:", ACCUMULATOR)
        print("LINE_COUNTER:", LINE_COUNTER)
        print("STACK:", STACK)
        print("PORTS:", PORTS)

# Convert each line into an array
def tokenise(line):
    # remove comments if any
    line = line.split(";")[0].strip()
    # remove any whitespace
    tokens = re.split(r"\s+", line)
    return tokens


# Execute a line
def execute(line):
    global ACCUMULATOR, ram, STACK, LINE_COUNTER

    tokens = tokenise(line)

    opcode = tokens[0]
    params = tokens[1:]

    if VERBOSE:
        print("t", tokens)
        print("p", params)

    # run opcode according to instruction set
    if opcode in ROM:
        ROM[opcode](params)
    else:
        error("Unknown opcode " + opcode)

        
    # if opcode == "HLT":
    #     # Code to execute if the opcode is "HLT"
    #     HLT()
    # elif opcode == "SAV":
    #     # Code to execute if the opcode is "SAV"
    #     SAV(params[0],params[1])
    # elif opcode == "LDA":
    #     # Code to execute if the opcode is "LDA"
    #     LDA(params[0])
    # elif opcode == "ADD":
    #     # Code to execute if the opcode is "ADD"
    #     ADD(params[0])
    # elif opcode == "SUB":
    #     # Code to execute if the opcode is "SUB"
    #     SUB(params[0])
    # elif opcode == "JMP":
    #     # Code to execute if the opcode is "JMP"
    #     JMP(params[0])
    # elif opcode == "JEZ":
    #     # Code to execute if the opcode is "JEZ"
    #     JEZ(params[0])
    # elif opcode == "JGZ":
    #     # Code to execute if the opcode is "JGZ"
    #     JGZ(params[0])
    # elif opcode == "JLZ":
    #     # Code to execute if the opcode is "JLZ"
    #     JLZ(params[0])
    # elif opcode == "JNZ":
    #     # Code to execute if the opcode is "JNZ"
    #     JNZ(params[0])
    # elif opcode == "INP":
    #     # Code to execute if the opcode is "INP"
    #     INP()
    # elif opcode == "OUT":
    #     # Code to execute if the opcode is "OUT"
    #     OUT()
    # elif opcode == "SIG":
    #     # Code to execute if the opcode is "SIG"
    #     SIG(params[0], params[1])
    # elif opcode == "BAD":
    #     # Code to execute if the opcode is "BAD"
    #     BAD(params[0])
    # elif opcode == "BOR":
    #     # Code to execute if the opcode is "BOR"
    #     BOR(params[0])
    # elif opcode == "BXR":
    #     # Code to execute if the opcode is "BXR"
    #     BXR(params[0])
    # elif opcode == "DLY":
    #     # Code to execute if the opcode is "DLY"
    #     DLY(params[0])
    # else:
    #     # Code to execute if the opcode doesn't match any of the given opcodes
    #     print("Unknown opcode", opcode)


###############################################################################################################################

# Main program starts here

# Argument handling
parser = argparse.ArgumentParser(description="")

# Add arguments
parser.add_argument(
    "-v", "--verbose", action="store_true", help="Enable Verbose output"
)

# Add the 'filename' argument
parser.add_argument(
    "-f", "--filename", metavar="FILE", type=str, help="The input filename"
)

# Argument to show the ram output each iteration
parser.add_argument(
    "-r", "--show_ram", action="store_true", help="Show the values in ram"
)

# set args
args = parser.parse_args()

VERBOSE = args.verbose


""" MAIN LOOP """
if __name__ == "__main__":
    # handle no file
    if args.filename == None:
        # error message in red using colors class
        error("No file specified")
        exit(1)

    if args.show_ram:
        showram(ram)
    
    with open(args.filename) as program_file:
        # Execute each line iteratively
        for line in program_file:
            if line != "\n":
                execute(line)
                if args.verbose:
                    print("\u001b[31mACCUMULATOR:", ACCUMULATOR, "\u001b[0m")
                if args.show_ram:
                    showram(ram)
