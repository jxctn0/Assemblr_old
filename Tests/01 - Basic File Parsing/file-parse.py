#!/bin/env python3

import re
import time

# GLOBALS
# global ACCUMULATOR
ACCUMULATOR = 0
RAM_SIZE = 1024
RAM = [[""]*RAM_SIZE]
USED_RAM = 0

print(RAM)

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
        print("Save value")
        # save value to next available RAM slot
        RAM[USED_RAM] = ACCUMULATOR
    
    elif opcode == "LDA":
        # Code to execute if the opcode is "LDA"
        print("Load value")
        # load value from RAM slot
        ACCUMULATOR = RAM[int(params[0])]
    
    elif opcode == "ADD":
        # Code to execute if the opcode is "ADD"
        print("Add values")
        # add value to accumulator
        ACCUMULATOR += int(params[0])
    
    elif opcode == "SUB":
        # Code to execute if the opcode is "SUB"
        print("Subtract values")
        # subtract value from accumulator
        ACCUMULATOR -= int(params[0])
    
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
        # Input value from specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)
        # ACCUMULATOR = GPIO.input(int(params[0]))
        ACCUMULATOR = int(input("Enter a value: "))
    
    elif opcode == "OUT":
        # Code to execute if the opcode is "OUT"
        print("Output value")
        print("ACCUMULATOR:", ACCUMULATOR)

    elif opcode == "SIG":
        # Code to execute if the opcode is "SIG"
        print("Send signal")
        # Send signal to specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)
        # GPIO.output(int(params[0]), int(params[1]))
        print("Pin " + params[0] + " set to " + params[1])

    elif opcode == "BAD":
        # Code to execute if the opcode is "BAD"
        print("Bitwise AND")
        # Bitwise AND
        ACCUMULATOR = ACCUMULATOR & int(params[0])

    elif opcode == "BOR":
        # Code to execute if the opcode is "BOR"
        print("Bitwise OR")
        # Bitwise OR
        ACCUMULATOR = ACCUMULATOR | int(params[0])

    elif opcode == "BXR":
        # Code to execute if the opcode is "BXR"
        print("Bitwise XOR")
        ACCUMULATOR = ACCUMULATOR ^ int(params[0])

    elif opcode == "BNT":
        # Code to execute if the opcode is "NOT"
        print("Bitwise NOT")
        # Bitwise NOT
        ACCUMULATOR = ~ACCUMULATOR

    elif opcode == "DLY":
        # Code to execute if the opcode is "DLY"
        print("Delay")
        # Delay for a specified number of cycles
        time.sleep(int(params[0]))
    else:
        # Code to execute if the opcode doesn't match any of the given opcodes
        print("Unknown opcode " + opcode)
        quit()

"""
Instruction | Parameters | Description
------------|------------|------------
HLT         | N/A        | Halt the program
SAV         | N/A        | Save the value in the accumulator to RAM
LDA         | Address    | Load the value from RAM[Address] into the accumulator
ADD         | Value      | Add the value to the accumulator
SUB         | Value      | Subtract the value from the accumulator
JMP         | Label      | Jump Always to the specified label 
JEZ         | Label      | Jump to the specified label if the accumulator is equal to zero
JGZ         | Label      | Jump to the specified label if the accumulator is greater than zero
JLZ         | Label      | Jump to the specified label if the accumulator is less than zero
INP         | Pin        | Input a value from the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)/ Console
OUT         | N/A        | Output the value in the accumulator to the console
SIG         | Pin, Value | Send a signal to the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)
BAD         | Value      | Bitwise AND the value with the accumulator
BOR         | Value      | Bitwise OR the value with the accumulator
BXR         | Value      | Bitwise XOR the value with the accumulator
BNT         | N/A        | Bitwise NOT the accumulator
DLY         | Cycles     | Delay for a specified number of cycles




"""


def main():
    filename = "testfile01.asr"
    verbose = True
    
    with open(filename) as program_file:
        for line in program_file:
            print(line)
            execute(line)
            if verbose:
                 print(u"\u001b[31mACCUMULATOR:", ACCUMULATOR, u"\u001b[0m")




''' MAIN LOOP '''
if __name__ == '__main__':
    main()