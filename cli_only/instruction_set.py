import time
import main

# GLOBALS
ACCUMULATOR = main.ACCUMULATOR
RAM = main.RAM



# HLT - Halt the program
def HLT():
    if VERBOSE:
        print("\u001b[32mHalt program\u001b[0m")
    quit()


# SAV - Save the value in the accumulator to the address specified
def SAV(value, name, location):
    global ram,NAMED_ADDRESSES, VERBOSE
    #convert location from hex to int
    location = int(location, 16)

    # check if address is empty in ram
    if ram[location] == 0:
        ram[location] = int(value)
        NAMED_ADDRESSES[name] = location
    else:
        print(f"Address {NAMED_ADDRESSES} already in use")
        exit(1)


# LDA - Load the value from the address specified (from NAMED_ADDRESSES dictionary) into the accumulator
def LDA(name):
    global ACCUMULATOR, NAMED_ADDRESSES, VERBOSE, ram
    ACCUMULATOR = ram[NAMED_ADDRESSES[name]]
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

