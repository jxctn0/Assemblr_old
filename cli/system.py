# ASSEMBLr Opcodes

# Imports
import registers


"""
Opcodes are:

0000    HLT    Halt program
0001    SAV    Save accumulator first availible RAM address
0010    LDA    Load accumulator with value at given RAM address
0011    ADD    Add value at given RAM address to accumulator or add given value to accumulator
0100    SUB    Subtract value at given RAM address from accumulator or subtract given value from accumulator
0101    STA    Store accumulator at given RAM address
0110    OUT    Output accumulator value to console or given port output
0111    INP    Input value to accumulator from console or given port input
1000    JMP    Jump to given RAM address (instruction)
1001    JEZ    Jump to given RAM address (instruction) if accumulator is equal to zero
1010    JLZ    Jump to given RAM address (instruction) if accumulator is not equal to zero
1011    JGZ    Jump to given RAM address (instruction) if accumulator is greater than zero
1111    DLY    Delay processing for given number of clock cycles

"""

# Opcode Functions

def HLT():
    exit(0)

def SAV(data):
    # Check if data is given
    if data == None:
        
    