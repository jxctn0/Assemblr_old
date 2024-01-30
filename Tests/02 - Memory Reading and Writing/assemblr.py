# CPU RUNS INSTRUCTIONS
# PROGRAMS ARE A QUEUE OF INSTRUCTIONS
# INSTRUCTIONS ARE STORED IN RAM

# Imports
import re # Regular Expressions


# Global Variables
verbose = True # Set to True to print out debug information

# Convert each line into an array
def tokenise(line):
    # if line starts with a comment, ignore it
    if line[0] == ";":
        return []
    # remove comments if any
    line = line.split(";")[0].strip()
    tokens = re.split(r"\s+", line)  #
    return tokens

class System:
    def __init__(self):
        """
        System contains:
        - Program Counter
        - Accumulator
        - Memory Data Register --> This is the 
        - RAM --> List of Instruction Objects
        - Instruction Register --> Instruction Object

            - Data
        """
        self.program_counter = 0
        self.accumulator = 0
        self.memory_data_register = 0
        self.ram = []
        self.instruction_register = None
        self.halted = False
        self.programLength = 0

    def run(self):
        # fetch the next instruction
        self.instruction_register = self.ram[self.program_counter]
        # increment the program counter
        self.program_counter += 1
        # execute the instruction
        self.program_counter += self.instruction_register.execute()
        # if the program counter is bigger than the length of the program:
        if self.program_counter >= self.programLength:
            # halt the program
            self.set_HALTED()

    # read/write registers
            
    # Set Program Counter
    def set_PROGRAM_COUNTER(self, value):
        self.program_counter = value

    # Get Program Counter Not Needed
        
    # Set Accumulator
    def set_accumulator(self, value):
        self.accumulator = value

    # Get Accumulator
    def get_accumulator(self):
        return self.accumulator
    
    # Set/Get Memory Data Register Not Needed

    # Read/Write RAM
    def read_RAM(self, address):
        return self.ram[address]
    
    def write_RAM(self, address, value):
        self.ram[address] = value

    # Halt the program
    def set_HALTED(self):
        self.halted = True

    # Check if the program is halted
    def is_HALTED(self):
        return self.halted


"""
Number | Name | Use | Description
-------|------|-----|------------
0      | HLT  | HLT | Halt the program
1      | SAV  | SAV <Address> | Save the value in the accumulator to RAM[Address]
2      | LDA  | LDA <Address> | Load the value from RAM[Address] into the accumulator
3      | ADD  | ADD <Value> | Add the value to the accumulator
4      | SUB  | SUB <Value> | Subtract the value from the accumulator
5      | OUT  | OUT | Output the value in the accumulator to the console
6      | INP  | INP | Input a value from the console
7      | BAD  | BAD <Value> | Bitwise AND the value with the accumulator
8      | BOR  | BOR <Value> | Bitwise OR the value with the accumulator
9      | BXR  | BXR <Value> | Bitwise XOR the value with the accumulator
a      | BNT  | BNT | Bitwise NOT the accumulator
b      | JMP  | JMP <Label> | Jump Always to the specified label
c      | JEZ  | JEZ <Label> | Jump to the specified label if the accumulator is equal to zero
d      | JGZ  | JGZ <Label> | Jump to the specified label if the accumulator is greater than zero
e      | JLZ  | JLZ <Label> | Jump to the specified label if the accumulator is less than zero
f      | SIG  | SIG <Pin> | Send a signal to the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)
"""



#################################################################################
# Instruction Classes                                                           #
# -------------------                                                           #
# Classes for each instruction                                                  #
# Instruction Set                                                               #
#   Each instruction is a subclass of the Instruction class                     #
#   Each instruction has an execute method which runs the instruction           #
#   Each instruction has a name and a list of operands (parameters)             #
#   Each instruction has a set of methods to read and write to RAM              #
#   Each instruction has a set of methods to read and write to the accumulator  #


class Instruction:
    def __init__(self, opcode, operands):
        super().__init__() # Inherit from System
        self.opcode = opcode # The name of the instruction
        self.operands = operands # List of operands (parameters) for the instruction

    # read/write registers
            
    # Set Program Counter
    def set_PROGRAM_COUNTER(self, value):
        super().set_PROGRAM_COUNTER(value)

    # Get Program Counter Not Needed
        
    # Set Accumulator
    def set_accumulator(self, value):
        super().set_accumulator(value)

    # Get Accumulator
    def get_accumulator(self):
        return super().get_accumulator()
    
    # Set/Get Memory Data Register Not Needed

    # Read/Write RAM
    def read_RAM(self, address):
        return super().read_RAM(address)
    
    def write_RAM(self, address, value):
        super().write_RAM(address, value)

    # Halt the program
    def set_HALTED(self):
        super().set_HALTED()
        
# HLT
# Halts the program
class HLT(Instruction):
    def __init__(self):
        super().__init__("HLT", []) 

    def execute(self):
        super.SET_HALTED = True
        return 1
    
# SAV
# Saves the value in the accumulator to RAM[operand]
class SAV(Instruction):
    def __init__(self, operands):
        super().__init__("SAV", operands)

    def execute(self):
        self.write_RAM((self.operands[0], self.get_accumulator()))
        return 1
    
# LDA
# Loads the value from RAM[operand] into the accumulator
class LDA(Instruction):
    def __init__(self, operands):
        super().__init__("LDA", operands)

    def execute(self):
        self.set_accumulator(self.read_RAM((self.operands[0], 0)))
        return 1
    
# ADD
# Adds the value to the accumulator
class ADD(Instruction):
    def __init__(self, operands):
        super().__init__("ADD", operands)

    def execute(self):
        self.set_accumulator(self.get_accumulator() + int(self.operands[0]))
        return 1

    
# SUB
# Subtracts the value from the accumulator
class SUB(Instruction):
    def __init__(self, operands):
        super().__init__("SUB", operands)

    def execute(self):
        self.set_accumulator(self.get_accumulator() - int(self.operands[0]))
        return 1
    
# OUT
# Outputs the value in the accumulator to the console
class OUT(Instruction):
    def __init__(self):
        super().__init__("OUT", [])

    def execute(self):
        print(self.get_accumulator())
        return 1
    
# INP
# Inputs a value from the console
class INP(Instruction):
    def __init__(self):
        super().__init__("INP", [])

    def execute(self):
        self.set_accumulator(int(input("Enter a value: ")))
        return 1
    
# BAD
# Bitwise AND the value with the accumulator
class BAD(Instruction):
    def __init__(self, operands):
        super().__init__("BAD", operands)

    def execute(self):
        self.set_accumulator(self.get_accumulator() & int(self.operands[0]))
        return 1
    
# BOR
# Bitwise OR the value with the accumulator
class BOR(Instruction):
    def __init__(self, operands):
        super().__init__("BOR", operands)

    def execute(self):
        self.set_accumulator(self.get_accumulator() | int(self.operands[0]))
        return 1
    
# BXR
# Bitwise XOR the value with the accumulator
class BXR(Instruction):
    def __init__(self, operands):
        super().__init__("BXR", operands)

    def execute(self):
        self.set_accumulator(self.get_accumulator() ^ int(self.operands[0]))
        return 1
    
# BNT
# Bitwise NOT the accumulator
class BNT(Instruction):
    def __init__(self):
        super().__init__("BNT", [])

    def execute(self):
        self.set_accumulator(~self.get_accumulator())
        return 1
    
# JMP
# Jump Always to the specified label
class JMP(Instruction):
    def __init__(self, operands):
        super().__init__("JMP", operands)

    def execute(self):
        self.set_PROGRAM_COUNTER(int(self.operands[0]))
        return 0
    
# JEZ
# Jump to the specified label if the accumulator is equal to zero
    
class JEZ(Instruction):
    def __init__(self, operands):
        super().__init__("JEZ", operands)

    def execute(self):
        if self.get_accumulator() == 0:
            self.set_PROGRAM_COUNTER(int(self.operands[0]))
            return 0
        return 1
    
# JGZ
# Jump to the specified label if the accumulator is greater than zero
class JGZ(Instruction):
    def __init__(self, operands):
        super().__init__("JGZ", operands)

    def execute(self):
        if self.get_accumulator() > 0:
            self.set_PROGRAM_COUNTER(int(self.operands[0]))
            return 0
        return 1
    
# JLZ
# Jump to the specified label if the accumulator is less than zero
class JLZ(Instruction):
    def __init__(self, operands):
        super().__init__("JLZ", operands)

    def execute(self):
        if self.get_accumulator() < 0:
            self.set_PROGRAM_COUNTER(int(self.operands[0]))
            return 0
        return 1
    
# SIG
# Send a signal to the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)
class SIG(Instruction):
    def __init__(self, operands):
        super().__init__("SIG", operands)

    def execute(self):
        print(f"Sending signal of strength {self.get_accumulator()} to pin {self.operands[0]}")
        return 1
    
###########################################
# END OF Instruction Classes              #
    

# Main Function
def main():
    global system # Make system global so it can be accessed from anywhere
    system = System() # Create a new system
    
    # Create a new program
    program = "test.asr"

    # open the program file
    with open(program, "r") as f:
        # read the program file
        program = f.read()
        # split the program into lines
        program = program.split("\n")
        if verbose:
            print(program)
        # for each line in the program:
    for line in program:
        # if the line is not empty:
        if len(line) > 0: 
            if line[0] == ";": # or a comment
                continue
            # tokenize the line
            line = tokenise(line)
            # convert the tokens into Instruction objects
            opcode = line[0]
            operands = line[1:]
            if opcode == "HLT":
                system.ram.append(HLT())
            elif opcode == "SAV":
                system.ram.append(SAV(operands))
            elif opcode == "LDA":
                system.ram.append(LDA(operands))
            elif opcode == "ADD":
                system.ram.append(ADD(operands))
            elif opcode == "SUB":
                system.ram.append(SUB(operands))
            elif opcode == "OUT":
                system.ram.append(OUT())
            elif opcode == "INP":
                system.ram.append(INP())
            elif opcode == "BAD":
                system.ram.append(BAD(operands))
            elif opcode == "BOR":
                system.ram.append(BOR(operands))
            elif opcode == "BXR":
                system.ram.append(BXR(operands))
            elif opcode == "BNT":
                system.ram.append(BNT())
            elif opcode == "JMP":
                system.ram.append(JMP(operands))
            elif opcode == "JEZ":
                system.ram.append(JEZ(operands))
            elif opcode == "JGZ":
                system.ram.append(JGZ(operands))
            elif opcode == "JLZ":
                system.ram.append(JLZ(operands))
            elif opcode == "SIG":
                system.ram.append(SIG(operands))
            else:
                raise ValueError(f"Unknown opcode {opcode}")
    if verbose:
        print(system.ram)
    # Ram is now a list of Instruction objects
        
    # Get the length of the program
    system.programLength = len(system.ram)
    # set ram to it's full length
    system.ram = system.ram + [None] * (256 - system.programLength)
    system.is_HALTED = False # Set the system to not be halted
    # run the program
    while system.is_HALTED == False:
        system.run()
        

# Run the main function
if __name__ == "__main__":
    main()

# END OF FILE