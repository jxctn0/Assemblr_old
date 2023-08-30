# Imports

# Preinstalled modules
import random, time, os, sys, json, re, argparse

# Custom modules
import startup, cli, menu

def startup():
    # Import config
    global config
    config = json.load(open("config.json"))

    # GLOBALS
    global registers
    class registers:
        accumulator = 0
        line_counter = 0
        cache = [0*config["cache_num"]]

    global system
    class system:
        CLOCK_SPEED = config["CLOCK_SPEED"]
        BIT_LENGTH = config["BIT_LENGTH"]
        RAM_SIZE = config["RAM_SIZE"]

    global ram
    # Initialise RAM
    ram = startup.initialiseRAM(system.RAM_SIZE)

##################################################################################################

# parse arguments
parser = argparse.ArgumentParser(description="Assemblr CLI")
# Verbose
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
# Filename to run
parser.add_argument("-f","--filename", help="filename to run")
# Show RAM
parser.add_argument("-r", "--ram", help="show RAM", action="store_true")

args = parser.parse_args()

# Set verbose
if args.verbose:
    VERBOSE = True
else:
    VERBOSE = False

# Set filename
if args.filename:
    filename = args.filename

# Set show RAM
if args.ram:
    SHOW_RAM = True
else:
    SHOW_RAM = False


# Main loop
def main():
    # if filename is not set, show menu
    if not filename:
        menu.main()
    else:
        system.execute(filename)
    
if __name__ == "__main__":
    startup()
    main()
    cli.notify.info("Program finished Successfully")
    quit(0)