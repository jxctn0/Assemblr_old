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

# Confirm menu
def confirm(extraText = ""):
    # ncurses window for confirm menu
    confirm_menu = curses.newwin(10, 40, 10, 10)
    # 0: no border
    confirm_menu.border(0)
    # set confirm string if extraText is empty
    if extraText == "":
        extraText = "Are you sure?"
    # Print confirm message with yellow background
    confirm_menu.addstr(1, 1, cli.format.bg.yellow + extraText + cli.format.reset)
    # Option to confirm
    confirm_menu.addstr(2, 1, cli.format.fg.yellow + "Yes" + cli.format.reset)

    # Option to cancel
    confirm_menu.addstr(3, 1, cli.format.fg.yellow + "No" + cli.format.reset)
    # Refresh menu
    confirm_menu.refresh()
    # Get keypress
    key = confirm_menu.getch()
    # Check keypress
    if key == ord("1") or key

# Show menu with Assemblr logo, and options to load a ROM file or exit

def main():
    # Clear screen
    cli.clear()

    # Print Assemblr logo
    cli.print_sprite()

    # Print menu options in a curses window
    menu = curses.newwin(10, 40, 10, 10)
    menu.border(0)
    # Print menu options:
    # Assemblr Main Menu
    menu.addstr(1, 1, "Assemblr Main Menu")
    # Load ROM
    menu.addstr(3, 1, "1. Load ROM")
    # Exit
    menu.addstr(4, 1, "2. Exit")
    # Refresh menu
    menu.refresh()

    # Check for keypress
    key = menu.getch()

    # Check keypress
    if key == ord("1"):
        """
        Load ROM Files
        
        """
        # Clear screen
        cli.clear()
        # Print Assemblr logo
        cli.print_sprite("assemblr")
        # Get ROM files
        getROMFiles()
        # Print ROM files
        for i in range(len(ROM_FILES)):
            # Remove .asrom extension
            ROM_FILES[i] = ROM_FILES[i].replace(".asrom", "")
            # create menu window for ROM files (scale for number of ROM files)
            rom_menu = curses.newwin(10, 40, 10, 10)
            # 0: no border
            # 1: border
            # 2: thick border
            # 3: double border
            # 4: dashed border
            # 5: dotted border
            # 6: dashed/dotted border

            rom_menu.border(1)

            # Print ROM files
            rom_menu.addstr(1, 1, f"{i+1}. {ROM_FILES[i]}")
            # Refresh menu
            rom_menu.refresh()

            # Get keypress
            key = rom_menu.getch()

            # Check keypress, and load appropriate ROM file if valid
            valid_keys = [ord(str(i+1)) for i in range(len(ROM_FILES))]
            while key not in valid_keys:
                if key == ord(str(i+1)):
                    # Clear screen
                    cli.clear()
                    # Set ROM file to load
                    app.filename = ROM_FILES[i]
                    # exit menu
                    break
                else:
                    # Clear screen
                    cli.clear()
                    # Print Assemblr logo
                    cli.print_sprite("assemblr")
                    # Print error message
                    cli.notify.error("Invalid option", 1)
                    # Refresh menu
                    rom_menu.refresh()
                    # Wait for keypress
                    key = rom_menu.getch()
                    # Clear screen
                    cli.clear()
            # Clear screen
            cli.clear()
            # Exit menu
            break
    elif key == ord("2"):
        # Exit
        exit(0)
    else:
        # invalid option
        # add ncurses window for error message
        error_menu = curses.newwin(10, 40, 10, 10)
        # 1: border
        error_menu.border(1)
        # Print error message
        error_menu.addstr(1, 1, cli.format.bg.red +"Invalid option" + cli.format.reset)
        # Option to try again
        error_menu.addstr(2, 1, cli.format.fg.red +"Try again" + cli.format.reset)
        # Option to exit
        error_menu.addstr(3, 1, cli.format.fg.red +"Exit" + cli.format.reset)
        # Refresh menu
        error_menu.refresh()
        # Get keypress
        key = error_menu.getch()
        # Check keypress
        if key == ord("1"):
            # try again
            main()
        elif key == ord("2"):
            # check if sure
            # add ncurses window for confirm message



"""
test config.json:
{
    "directories": {
        "ROM_FILES": "ROM_FILES"


"""

