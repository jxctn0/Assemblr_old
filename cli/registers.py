# Registers for program

# Imports
import json

# Import config file
config = json.load(open("config.json"))

# Read config file and set variables
CLOCK_SPEED = config["CLOCK_SPEED"]
BIT_LENGTH = config["BIT_LENGTH"]
RAM_SIZE = config["RAM_SIZE"]

# Initialise RAM with 0s
RAM = [0]*RAM_SIZE

# Initialise registers
class registers:
    accumulator = 0
    line_counter = 0
    cache = [0*config["cache_num"]]
    program_length = 0

