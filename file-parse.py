#!/bin/env python3

import re
import argparse


# GLOBALS
# global ACCUMULATOR
ACCUMULATOR = 0
RAM_SIZE = 1024

# Convert each line into an array
def tokenise(line):
    # remove comments if any
    line = line.split(";")[0].strip()
    tokens = re.split(r'\s+', line) # split on whitespace
    # remove empty tokens
    tokens = list(filter(None, tokens))
    # convert numbers to integers
    for i in range(len(tokens)):
        try:
            tokens[i] = int(tokens[i])
        except ValueError:
            pass
    return tokens

# 'run' file
def execute(line):   
    opcode = line[0]
    params = line[1:]
    print("p",params)
    if opcode == "HLT":
        # Code to execute if the opcode is "HLT"
        print("Halt program")
        quit()
    elif opcode == "SAV":
        # Code to execute if the opcode is "SAV"
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


class Processor:
    def __init__(self):
        self.accumulator = 0
        self.stack = Memory.memory[Memory.StackStart:Memory.StackStart + 256]
        self.ram = Memory(RAM_SIZE)
        self.programCounter = 0
        self.instructionRegister = ""
        self.running = False
        self.programStart = 0
        self.programEnd = self.programStart
    
    def executeInstruction(self):
        # fetch instruction
        self.instructionRegister = self.ram[self.programCounter]
        # increment program counter
        self.programCounter += 1
        # "decode" instruction

            


class Memory(Processor):
    def __init__(self, size = 1024):
        self.progStart = 0
        self.progEnd = 0
        self.stackStart = 0
        self.stackEnd = 0
        self.size = [[0]*size]

    def load(self, program):
        # "load" program into memory
            
        # 1. set "namespaces" for the program
        self.memory.progStart = 0
        self.memory.progEnd = len(program)-1
        self.memory.stackStart = len(program)
        self.memory.stackEnd = len(program) + 256
        self.memory.usableStart = self.memory.progEnd + 256

        # 2. load program into memory        
        for instruction_number in range(len(program)):
            self.ram[instruction_number] = program[instruction_number][0]
            self.memory.ram = program[instruction_number][1]
            if len(program[instruction_number]) > 1:
                self.memory.ram = program[instruction_number][2]
            
        # 3. set program counter to start of program
        self.programCounter = self.memory.progStart

def getProgram(local):
    args = local
    # Open file and read lines
    with open(args.filename, 'r') as f:
        lines = f.readlines()

    # Tokenise each line
    program = []
    for line in lines:
        tokens = tokenise(line)
        if len(tokens) > 0:
            program.append(tokens)

    return program

def init():
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

    # set globals
    global VERBOSE
    VERBOSE = args.verbose

    system = Processor(), Memory()

    program = getProgram(args)

    return program, system

def confirmNextAction(Text = "Continue?"):
    while True:
        response = input("\r\n" +Text + " [Y/n] ")
        if response.lower() in ["y", "yes", ""]:
            return True
        elif response.lower() in ["n", "no"]:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue


def main():
    try:
        program, system = init()
        if VERBOSE:
            print(program)

        system.memory.load(program)
        
        if confirmNextAction():
            system.Processor.halted
    except KeyboardInterrupt:
        system.cleanup()


''' MAIN LOOP '''
if __name__ == '__main__':
    confirmNextAction("Start?")

    