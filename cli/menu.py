# Imports
import cli, app # Import custom modules
import curses, os # Import preinstalled modules
import json # Import json module

# Import config
# check if config.json exists
if not os.path.isfile("./config.json"):
    cli.notify.error("Config.json not found", 51) # 51: "File not found"
else:
    global config
    config = json.load(open("config.json"))
    if app.VERBOSE:
        cli.notify.info("Loaded config.json")

# GLOBALS
global ROM_FILES
ROM_FILES = []

def getROMFiles():
    # Initialise ROM
    # Get ROM Files location from config
    rom_dir = config["directories"]["ROM_FILES"]

    # check if rom_dir exists
    if not os.path.isdir(rom_dir):
        cli.error(f"ROM directory {rom_dir} does not exist", 51) # 51: "File not found"

    # create list of ROM files from all *.asrom files in ROM_FILES directory to be used in menu
    for file in os.listdir(rom_dir):
        if file.endswith(".asrom"):
            ROM_FILES.append(file)

    # check if ROM_FILES is empty
    if len(ROM_FILES) == 0:
        cli.error(f"No ROM files found in {rom_dir}", 51) # 51: "File not found"

# Show menu with Assemblr logo, and options to load a ROM file or exit

def showMainMenu():
    # Clear screen
    cli.clear()

    # Print Assemblr logo
    cli.printLogo()

    # Print menu options in a curses window
    menu = curses.newwin(10, 40, 10, 10)
    menu.border(0)
    menu.addstr(1, 1, "Main Menu")
    menu.addstr(3, 1, "1. Load ROM")
    menu.addstr(4, 1, "2. Exit")
    menu.refresh()

"""
test config.json:
{
    "directories": {
        "ROM_FILES": "ROM_FILES"


"""