#!/bin/env python3

import re
import argparse
import time

# GLOBALS
ACCUMULATOR = 0

# initialise RAM
RAM_SIZE = 255  # Specify the desired size of the dictionary (256 for keys 0 to ff)
RAM = {hex(i)[2:].zfill(2): 0 for i in range(RAM_SIZE)}
NAMED_ADDRESSES = {}

global BIT_LENGTH
BIT_LENGTH = 1024


# Show RAM in neat, tabulated format of 4 columns
def show_ram():
    global RAM
    print("RAM:")
    for key, value in RAM.items():
        print(f"| {key} | {value}", end="\t")
        if int(key, 16) % 4 == 3:
            print(" |")

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

# Load the program into RAM
def load_program(program_file):
    global RAM, LINE_COUNTER
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
                # Save the value to the RAM
                RAM[hex(LINE_COUNTER)[2:].zfill(2)] = int(value)
                # Increment the line counter
                LINE_COUNTER += 1
            else:
                # If the opcode is not SAV, increment the line counter
                LINE_COUNTER += 1
    

# Debugging option to show output:
def devprint():
    global VERBOSE
    if VERBOSE:
        print("ACCUMULATOR:", ACCUMULATOR)
        show_ram()
        print("LINE_COUNTER:", LINE_COUNTER)
        print("STACK:", STACK)
        print("SAVs:", SAVs)
        print("PORTS:", PORTS)

# MNEMONICS
# HLT - Halt the program
def HLT():
    if VERBOSE:
        print("\u001b[32mHalt program\u001b[0m")
    quit()


# SAV - Save the value in the accumulator to the address specified
def SAV(value, name, location):
    global RAM,NAMED_ADDRESSES, VERBOSE
    #convert location from hex to int
    location = int(location, 16)

    # check if address is empty in RAM
    if RAM[location] == 0:
        RAM[location] = int(value)
        NAMED_ADDRESSES[name] = location
    else:
        print(f"Address {NAMED_ADDRESSES} already in use")
        exit(1)


# LDA - Load the value from the address specified (from NAMED_ADDRESSES dictionary) into the accumulator
def LDA(name):
    global ACCUMULATOR, NAMED_ADDRESSES, VERBOSE, RAM
    ACCUMULATOR = RAM[NAMED_ADDRESSES[name]]
    if VERBOSE:
        print("Loaded value ", ACCUMULATOR, " from address ", NAMED_ADDRESSES[name], " into accumulator")
        
# ADD - Add the value to the accumulator
def ADD(value):
    global ACCUMULATOR, VERBOSE
    ACCUMULATOR += int(value)
    # check if accumulator is greater than set size
    if ACCUMULATOR > BIT_LENGTH:
        # kill program
        print("Accumulator Overflow Error")
        exit(3)
    if VERBOSE:
        print("Added value ", value, " to accumulator")

# SUB - Subtract the value from the accumulator
def SUB(value):
    global ACCUMULATOR, VERBOSE
    ACCUMULATOR -= int(value)
    if VERBOSE:
        print("Subtract values")

# JMP - Jump to the address specified
def JMP(address):
    global LINE_COUNTER, VERBOSE
    LINE_COUNTER = int(address)
    if VERBOSE:
        print("Jump to location")

# JEZ - Jump to the address specified if the accumulator is equal to zero
def JEZ(address):
    global ACCUMULATOR, LINE_COUNTER, VERBOSE
    if ACCUMULATOR == 0:
        LINE_COUNTER = int(address)
    if VERBOSE:
        print("Jump if equal to zero")

# JGZ - Jump to the address specified if the accumulator is greater than zero
def JGZ(address):
    global ACCUMULATOR, LINE_COUNTER, VERBOSE
    if ACCUMULATOR > 0:
        LINE_COUNTER = int(address)
    if VERBOSE:
        print("Jump if greater than zero")

# JLZ - Jump to the address specified if the accumulator is less than zero
def JLZ(address):
    global ACCUMULATOR, LINE_COUNTER, VERBOSE
    if ACCUMULATOR < 0:
        LINE_COUNTER = int(address)
    if VERBOSE:
        print("Jump if less than zero")

# JNZ - Jump to the address specified if the accumulator is not equal to zero
def JNZ(address):
    global ACCUMULATOR, LINE_COUNTER, VERBOSE
    if ACCUMULATOR != 0:
        LINE_COUNTER = int(address)
    if VERBOSE:
        print("Jump if not equal to zero")

# INP - Input a value into the accumulator
def INP():
    global ACCUMULATOR, VERBOSE
    ACCUMULATOR = int(input("U >>> "))
    if VERBOSE:
        print("Input value")


# OUT - Output the value in the accumulator
def OUT():
    global ACCUMULATOR, VERBOSE
    print(ACCUMULATOR)
    if VERBOSE:
        print("Output value")

# SIG - Send a signal of given strength to the given port
def SIG(port, strength):
    global PORTS, VERBOSE

    if port in range(0,15):
        # Check that the strength is valid
        if strength < 0:
            strength = 0
        elif strength > 255:
            strength = 255
        PORTS[port] = strength
    else:
        print("Invalid port address")
        exit(1)
    if VERBOSE:
        print("Send signal")

# BAD - Bitwise AND the value in the accumulator with the value given
def BAD(value):
    global ACCUMULATOR, VERBOSE
    ACCUMULATOR = ACCUMULATOR & int(value)
    if VERBOSE:
        print("Bitwise AND")

# BOR - Bitwise OR the value in the accumulator with the value given
def BOR(value):
    global ACCUMULATOR, VERBOSE
    ACCUMULATOR = ACCUMULATOR | int(value)
    if VERBOSE:
        print("Bitwise OR")

# BXR - Bitwise XOR the value in the accumulator with the value given
def BXR(value):
    global ACCUMULATOR, VERBOSE
    ACCUMULATOR = ACCUMULATOR ^ int(value)
    if VERBOSE:
        print("Bitwise XOR")

# DLY - Delay by the given number of ticks
def DLY(ticks):
    global VERBOSE
    time.sleep(ticks)
    if VERBOSE:
        print("Delay")

# Convert each line into an array
def tokenise(line):
    # remove comments if any
    line = line.split(";")[0].strip()
    # remove any whitespace
    tokens = re.split(r"\s+", line)
    return tokens


# Execute a line
def execute(line):
    global ACCUMULATOR, RAM, STACK, LINE_COUNTER

    tokens = tokenise(line)

    opcode = tokens[0]
    params = tokens[1:]

    if VERBOSE:
        print("t", tokens)
        print("p", params)

        
    if opcode == "HLT":
        # Code to execute if the opcode is "HLT"
        HLT()
    elif opcode == "SAV":
        # Code to execute if the opcode is "SAV"
        SAV(params[0],params[1])
    elif opcode == "LDA":
        # Code to execute if the opcode is "LDA"
        LDA(params[0])
    elif opcode == "ADD":
        # Code to execute if the opcode is "ADD"
        ADD(params[0])
    elif opcode == "SUB":
        # Code to execute if the opcode is "SUB"
        SUB(params[0])
    elif opcode == "JMP":
        # Code to execute if the opcode is "JMP"
        JMP(params[0])
    elif opcode == "JEZ":
        # Code to execute if the opcode is "JEZ"
        JEZ(params[0])
    elif opcode == "JGZ":
        # Code to execute if the opcode is "JGZ"
        JGZ(params[0])
    elif opcode == "JLZ":
        # Code to execute if the opcode is "JLZ"
        JLZ(params[0])
    elif opcode == "JNZ":
        # Code to execute if the opcode is "JNZ"
        JNZ(params[0])
    elif opcode == "INP":
        # Code to execute if the opcode is "INP"
        INP()
    elif opcode == "OUT":
        # Code to execute if the opcode is "OUT"
        OUT()
    elif opcode == "SIG":
        # Code to execute if the opcode is "SIG"
        SIG(params[0], params[1])
    elif opcode == "BAD":
        # Code to execute if the opcode is "BAD"
        BAD(params[0])
    elif opcode == "BOR":
        # Code to execute if the opcode is "BOR"
        BOR(params[0])
    elif opcode == "BXR":
        # Code to execute if the opcode is "BXR"
        BXR(params[0])
    elif opcode == "DLY":
        # Code to execute if the opcode is "DLY"
        DLY(params[0])
    else:
        # Code to execute if the opcode doesn't match any of the given opcodes
        print("Unknown opcode", opcode)

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

# Argument to show the RAM output each iteration
parser.add_argument(
    "-r", "--show_ram", action="store_true", help="Show the values in RAM"
)

# set args
args = parser.parse_args()

VERBOSE = args.verbose


""" MAIN LOOP """
if __name__ == "__main__":
    # handle no file
    if args.filename == None:
        # error message in red using colors class
        
        exit(1)
    with open(args.filename) as program_file:
        # Execute each line iteratively
        for line in program_file:
            if line != "\n":
                execute(line)
                if args.verbose:
                    print("\u001b[31mACCUMULATOR:", ACCUMULATOR, "\u001b[0m")
