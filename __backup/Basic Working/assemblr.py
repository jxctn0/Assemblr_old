#!/bin/env python3

import re
import time

# GLOBALS
# global ACCUMULATOR
ACCUMULATOR = 0
RAM_SIZE = 1024
RAM = [""] * RAM_SIZE
USED_RAM = 0

verbose = True

print(RAM)


# Convert each line into an array
def tokenise(line):
    # if line starts with a comment, ignore it
    if line[0] == ";":
        return []
    # remove comments if any
    line = line.split(";")[0].strip()
    tokens = re.split(r"\s+", line)  #
    return tokens


# 'run' file
def execute(line):
    global ACCUMULATOR

    opcode = line[0]
    # print("o", opcode)
    params = line[1:]
    # print("p", params)

    if opcode == "HLT":
        # Code to execute if the opcode is "HLT"
        print("Halt program")
        quit()

    elif opcode == "SAV":
        # Code to execute if the opcode is "SAV"
        print("Save value")
        # check if RAM slot is empty
        if RAM[int(params[0])] == "":
            # save value to RAM slot
            RAM[int(params[0])] = ACCUMULATOR
        else:
            print("RAM slot", params[0], "is already in use")
            exit()

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
        print(f"Pin {params[0]} set to {ACCUMULATOR}")

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
SAV         | Address    | Save the value in the accumulator to RAM[Address]
LDA         | Address    | Load the value from RAM[Address] into the accumulator
ADD         | Value      | Add the value to the accumulator
SUB         | Value      | Subtract the value from the accumulator
JMP         | Label      | Jump Always to the specified label 
JEZ         | Label      | Jump to the specified label if the accumulator is equal to zero
JGZ         | Label      | Jump to the specified label if the accumulator is greater than zero
JLZ         | Label      | Jump to the specified label if the accumulator is less than zero
INP         | Pin        | Input a value from the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)/ Console
OUT         | N/A        | Output the value in the accumulator to the console
SIG         | Pin        | Send a signal to the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)
BAD         | Value      | Bitwise AND the value with the accumulator
BOR         | Value      | Bitwise OR the value with the accumulator
BXR         | Value      | Bitwise XOR the value with the accumulator
BNT         | N/A        | Bitwise NOT the accumulator
DLY         | Cycles     | Delay for a specified number of cycles
"""

"""

Memory Map:
    RAM
    Program Instructions: 0-255 -- 256 Bytes
    Program Data: 256-511 -- 256 Bytes
    Stack (16 levels): 512-527 -- 16 Bytes
    Runtime: 528-1023 -- 496 Bytes

"""

class Memory:
    def __init__(self):
        self.RAM_SIZE = 1024
        self.ProgramInstructions = 256
        self.ProgramData = 256
        self.Stack = 16
        self.Runtime = self.RAM_SIZE - (self.ProgramInstructions + self.ProgramData + self.Stack)
        self.RAM = [""] * self.RAM_SIZE
        self.UsedProgramInstructions = 0
        self.UsedProgramData = 0
        self.StackPointer = 0
        self.UsedRuntime = 0

    def save(self, data, Namespace = "Runtime"):
        # get next available RAM slot in Namespace
        
        
        
    def load(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()

        for line in range(len(lines)):
            print(line)
            if line[0] == ";":
                if verbose:
                    print("Comment", line)
                continue
            elif line[0] == "\n":
                continue
            this_line = tokenise(line)
            print(this_line)
            instruction = this_line[0]
            params = this_line[1:]
            # save params to next available RAM slot in Program Data Namespace

            

            

def loadToRAM(filename):
    # Open file
    file = open(filename, "r")
    # Read file
    lines = file.readlines()
    # Close file
    file.close()
    for line in range(len(lines)):
        print(line)
        if line[0] == ";":
            if verbose:
                print("Comment", line)
            continue
        elif line[0] == "\n":
            continue
        this_line = tokenise(line)
        print(this_line)
        instruction = this_line[0]
        params = this_line[1:]
        # save instruction to next available RAM slot in Program Namespace
    
    # For each instruction in the program

    
        




def main():
    filename = "testfile01.asr"
    verbose = True

    loadToRAM(filename)


""" MAIN LOOP """
if __name__ == "__main__":
    main()
