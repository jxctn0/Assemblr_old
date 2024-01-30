#!/bin/env python3

import re
import time
import os

# GLOBALS
# global ACCUMULATOR
ACCUMULATOR = 0
RAM_SIZE = 1024
global VERBOSE
VERBOSE = False

# Convert each line into an array
def tokenise(line):
    # if line starts with a comment, ignore it
    if line[0] == ";":
        return []
    # remove comments if any
    line = line.split(";")[0].strip()
    tokens = re.split(r"\s+", line)  #
    return tokens

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
           
    

class Processor:
    def __init__(self, quirks=[]):
        self.setQuirks(quirks)
        self.ACCUMULATOR = 0
        self.RAM = Memory()
        self.Halted = False
        self.INSTRUCTION_REGISTER = "" # Instruction Register -- used to store the current instruction
        self.PROGRAM_COUNTER = 0 # Program Counter -- used to store the address of the next instruction to be executed
        self.DATA_REGISTER = 0 # Data Register -- used to store the address of the next data to be used
        self.Program = [] # Program -- used to store the program to be executed


    def setQuirks(self, quirks):
        return 0

    def execute(self):
        # For each instruction in the program
        for instruction in self.Memory.Program:
            # get instruction from RAM slot
            instruction = self.RAM.get_instruction(instruction)
            # execute instruction
            self.execute_instruction(instruction)
            # if Halted, break
            if self.Halted:
                break

    def get_address_from_label(self, label):
        # get address from label
        labels = self.RAM.get_labels()
        return labels[label]

    def execute_instruction(self, line):
        opcode = line[0]
        # print("o", opcode)
        params = line[1:]
        # print("p", params)

        if opcode == "HLT":
            if params != []:
                print("HLT takes no parameters")
                exit()
            # Code to execute if the opcode is "HLT"
            print("Halt program")
            # Halt the program
            self.Halted = True

        elif opcode == "SAV":
            if params == []:
                print("SAV takes one parameter --> SAV <address>")
                exit()
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
            if params == []:
                print("LDA takes one parameter --> LDA <address>")
                exit()
            # Code to execute if the opcode is "LDA"
            print("Load value")
            # load value from RAM slot
            ACCUMULATOR = self.RAM[int(params[0])]

        elif opcode == "ADD":
            if params == []:
                print("ADD takes one parameter --> ADD <value>")
                exit()
            # Code to execute if the opcode is "ADD"
            print("Add values")
            # add value to accumulator
            ACCUMULATOR += int(params[0])

        elif opcode == "SUB":
            if params == []:
                print("SUB takes one parameter --> SUB <value>")
                exit()
            # Code to execute if the opcode is "SUB"
            print("Subtract values")
            # subtract value from accumulator
            ACCUMULATOR -= int(params[0])

        elif opcode == "JMP":
            if params == []:
                print("JMP takes one parameter --> JMP <label>")
                exit()
            # Code to execute if the opcode is "JMP"
            print("Jump to location")
            # Jump to label
            label = params[0]
            self.PROGRAM_COUNTER = Memory.get_address_from_label(label)

        elif opcode == "JEZ":
            if params == []:
                print("JEZ takes one parameter --> JEZ <label>")
                exit()
            # Code to execute if the opcode is "JEZ"
            print("Jump if equal to zero")
            if ACCUMULATOR == 0:
                # Jump to label
                label = params[0]
                self.PROGRAM_COUNTER = Memory.get_address_from_label(label)

        elif opcode == "JGZ":
            # Code to execute if the opcode is "JGZ"
            print("Jump if greater than zero")
            if ACCUMULATOR > 0:
                # Jump to label
                label = params[0]
                self.PROGRAM_COUNTER = Memory.get_address_from_label(label)
                pass


        elif opcode == "JLZ":
            # Code to execute if the opcode is "JLZ"
            print("Jump if less than zero")
            if ACCUMULATOR < 0:
                # Jump to label
                label = params[0]
                # find label in program 
                pass

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

        return 0 # Return 0 if no errors

class Memory(Processor):
    def __init__(self, RAM_SIZE = 1024, quirks=[]):
        self.setQuirks(quirks)
        self.RAM_SIZE = RAM_SIZE
        self.ProgramInstructions = 256
        self.ProgramData = 256
        self.Stack = 16
        self.Runtime = self.RAM_SIZE - (self.ProgramInstructions + self.ProgramData + self.Stack)
        self.RAM = [""] * self.RAM_SIZE
        self.UsedProgramInstructions = self.RAM_SIZE - self.ProgramInstructions
        self.UsedProgramData = self.RAM_SIZE - self.ProgramData
        self.StackPointer =  0
        self.UsedRuntime = self.RAM_SIZE - self.Runtime
        self.labels = {}

    def setQuirks(self, quirks):
        # Quirks are a list of tuples of the form (quirk, value)
        # i.e. ("Stack", 32) will set the stack size to 32, and runtime memory is reduced accordingly
        # Possible quirks:
        # Stack: Set stack size to value ==> ("Stack", value)
        # Memory: Set total memory size to a number in 2^n format ==> ("Memory", value)
        # Runtime: Set runtime memory size to value ==> ("Runtime", value)
        # ProgramInstructions: Set program instructions memory size to value ==> ("ProgramInstructions", value)
        # ProgramData: Set program data memory size to value ==> ("ProgramData", value)

        for quirk in quirks:
            if quirk[0] == "Stack":
                self.Stack = quirk[1]
                self.Runtime = self.RAM_SIZE - (self.ProgramInstructions + self.ProgramData + self.Stack)
                self.UsedRuntime = self.RAM_SIZE - self.Runtime
            elif quirk[0] == "Memory":
                self.RAM_SIZE = quirk[1]
                self.Runtime = self.RAM_SIZE - (self.ProgramInstructions + self.ProgramData + self.Stack)
                self.UsedRuntime = self.RAM_SIZE - self.Runtime
            elif quirk[0] == "Runtime":
                self.Runtime = quirk[1]
                self.UsedRuntime = self.RAM_SIZE - self.Runtime
            elif quirk[0] == "ProgramInstructions":
                self.ProgramInstructions = quirk[1]
                self.UsedProgramInstructions = self.RAM_SIZE - self.ProgramInstructions
            elif quirk[0] == "ProgramData":
                self.ProgramData = quirk[1]
                self.UsedProgramData = self.RAM_SIZE - self.ProgramData
            else:
                print("Invalid Quirk")
                exit()

    def save(self, data, Namespace = "Runtime"):
        # get next available RAM slot in Namespace
        if Namespace == "Runtime": # Runtime memory is used for variables and other data that are set during runtime
            nextAddress = self.UsedRuntime + 1 # +1 because RAM starts at 0
        elif Namespace == "ProgData": # Program Data is used for data that is part of the program and labels for Jump instructions
            nextAddress = self.UsedProgramData + 1
        elif Namespace == "ProgInst": # Program Instructions is used for the actual program instructions
            nextAddress = self.UsedProgramInstructions + 1
        else:
            print("Invalid Memory Namespace")
            exit()
        
        # save data to RAM slot
        self.RAM[nextAddress] = data
        return nextAddress
        
    def load(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()

        for line in range(len(lines)):
            if VERBOSE:
                print(line)
            if lines[line][0] == ";":
                if VERBOSE:
                    print("Comment", lines[line])
                continue
            elif lines[line][0] == "\n":
                continue
            if lines[line][0] == ":":
                # Create label
                label = lines[line][1:].strip()
                address = line + 2 # +2 because RAM starts at 0 and next line is the instruction to be executed
                self.create_label(label, )
                continue
            this_line = tokenise(lines[line])
            if VERBOSE:
                print(this_line)
            instruction = this_line[0]
            params = this_line[1:]
            # save params to next available RAM slot in Program Data Namespace
            dataAddress = self.save(params, "ProgData")
            # save instruction to next available RAM slot in Program Instructions Namespace
            instructionAddress = self.save([instruction,dataAddress], "ProgInst")

    def create_label(self, name, address):
        self.labels[name] = address

    def get_address_from_label(self, label):
        return self.labels[label]


class Program(Memory):
    def __init__(self):
        self.program = {}
        self.instructions = []
        self.data = []
        self.labels = {}

    def load(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()

        # Create a program dictionary in the following format:
        """ 
        {
            "line{num}": {
                "type": "instruction|data|label",
                "instruction": {
                    "name": "name",
                    "parameters": ["param1", "param2", "param3"],
                }
                OR
                "data": {
                    "name": "name",
                    "address": "address"
                }
                OR
                "label": {
                    "name": "name",
                    "address": "address"
                },
            }
        }

        """
        for line in range(len(lines)):
            if lines[line][0] == ";": # Ignore comments
                if VERBOSE:
                    print("Comment", lines[line]) # Print comment if VERBOSE
                continue
            elif lines[line][0] == "\n": # Ignore blank lines
                continue
            elif lines[line][0] == ":": # If line is a label
                # Create label
                label = lines[line].split(":")[1].strip()
                address = line + 1 # Next line is the instruction to be 
                # Create label object
                label = {
                    "name": label,
                    "address": address
                }
                # Add label object to program dictionary
                self.program[f"line{line}"] = {
                    "type": "label",
                    "label": label
                }
                continue
            elif lines[line][0] == "$": # If line is a data declaration
                # Create data object
                data = lines[line].split("$")[1].strip()
                # Create data object
                data = {
                    "name": data,
                    "address": address
                }
                # Add data object to program dictionary
                self.program[f"line{line}"] = {
                    "type": "data",
                    "data": data
                }
                continue
            else: # If line is an instruction
                # tokenise line
                instruction = tokenise(lines[line])
                # create instruction object
                instruction = {
                    "name": instruction[0],
                    "parameters": instruction[1:]
                }
                # Add instruction object to program dictionary
                self.program[f"line{line}"] = {
                    "type": "instruction",
                    "instruction": instruction
                }
                continue

    
    def get_instruction(self, line):
        # get instruction from program dictionary
        instruction = self.program[line]["instruction"]
        # return instruction
        return instruction
    
    def get_label(self, id):
        # get labels from program dictionary
        labels = self.labels

        # get the address of the label
        address = labels[id]

        # return address
        return address
    
    def get_data(self, id):
        # get data from program dictionary
        data = self.data[id]

        # return data
        return data


def getFile():
    filename = "testfile01.asr"
    # will be the code to retrieve the file from the gui
    return filename

def main():
    filename = getFile()
    VERBOSE = True
    assemblr = Processor()
    assemblr.RAM.load(filename)
    assemblr.execute()


""" MAIN LOOP """
if __name__ == "__main__":
    os.system("clear")
    main()
