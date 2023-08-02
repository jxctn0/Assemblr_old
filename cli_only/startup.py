import main, instruction_set
import json
import os

# import config

config = json.load(open("config.json"))

# GLOBALS

RAM_SIZE = config["RAM_SIZE"]
VERBOSE = config["VERBOSE"]
BIT_LENGTH = config["BIT_LENGTH"]
CLOCK_SPEED = config["CLOCK_SPEED"]

ERROR_CODES = {
    # 0 General Errors
    00: "No error",
    01: "Unknown error",
    # 1 Instruction Errors
    11: "Unknown instruction",
    12: "Syntax error",
    # 2 Address Errors
    21: "Address not found",
    22: "Address already in use",
    # 3 Accumulator Errors
    31: "Accumulator overflow",
    32: "Accumulator underflow",
    # 4 Port Errors
    41: "Bad input",
    42: "Invalid signal",
    43: "Unknown Port",
    44: "Port already in use"
    }

def initialiseRAM(size):
    #      0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    ram = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(0, size):
        ram[i] = [0]
    return ram

# initialise ram
main.ram = initialiseRAM(RAM_SIZE)

# Initialise ROM
# Get ROM Files location from config
ROM_FILES = config["directories"]["ROM_FILES"]

# create list of ROM files from all *.asrom files in ROM_FILES directory
ROM_FILES = [f for f in os.listdir(ROM_FILES) if f.endswith(".asrom")]
