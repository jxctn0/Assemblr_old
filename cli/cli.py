# Classes and functions for printing to terminal.
# Contains:
#   - format class
#   - notify class

# Formatting class
class format:
    class fg:
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        yellow = "\033[33m"
        blue = "\033[34m"
        magenta = "\033[35m"
        cyan = "\033[36m"
        white = "\033[37m"
    
    class bg:
        black = "\033[40m"
        red = "\033[41m"
        green = "\033[42m"
        yellow = "\033[43m"
        blue = "\033[44m"
        magenta = "\033[45m"
        cyan = "\033[46m"
        white = "\033[47m"
    
    class style:
        bold = "\033[1m"
        dim = "\033[2m"
        italic = "\033[3m"
        underline = "\033[4m"
        blink = "\033[5m"
        reverse = "\033[7m"
        hidden = "\033[8m"

    class presets:
        info = "\033[1m\033[34m" # bold blue
        fatalError = "\033[1m\033[31m" # bold red
        warning = "\033[1m\033[33m" # bold yellow
        success = "\033[1m\033[32m" # bold green


    reset = "\033[0m"


# Error Codes
ERROR_CODES = {
    # 0 General Errors
    0: "No error",
    1: "Unknown error",
    # 1 Instruction Errors
    11: "Unknown instruction",
    12: "Syntax error",
    # 2 Address Errors
    21: "Address not found",
    22: "Address already in use",
    23: "Address out of range",
    24: "Unknown Address Error",
    # 3 Accumulator Errors
    31: "Accumulator overflow",
    32: "Accumulator underflow",
    33: "Unknown Accumulator Error",
    # 4 Port Errors
    41: "Bad input",
    42: "Invalid signal",
    43: "Unknown Port",
    44: "Port already in use",
    45: "Unknown Port Error",
    # 5 File Errors
    51: "File not found",
    52: "File already exists",
    53: "File is not a ROM file",
    54: "Unknown File Error"
    }

class notify:
    def error(code, location="", text=""):
        # Print basic error message
        print(f"{format.fg.red}ERROR: {ERROR_CODES[code]} ({code}), {format.reset}")
        # Print location of error
        if location != "":
            print(f"{format.fg.red}Location: {location, format.reset}")
        # Print error text
        if text != "":
            print(f"{format.fg.red}Text: {text, format.reset}")
        exit(code)

    def warning(code, location="", text=""):
        # Print basic error message
        print(f"{format.fg.yellow}WARNING: {ERROR_CODES[code]}, {format.reset}")
        # Print location of error
        if location != "":
            print(f"{format.fg.yellow}Location: {location, format.reset}")
        # Print error text
        if text != "":
            print(f"{format.fg.yellow}Text: {text, format.reset}")

    def info(text):
        print(f"{format.fg.blue}INFO: {text}{format.reset}")


        
class sprites:
    class text:
        assemblr_title_logo = """

 █████╗  ██████╗ ██████╗███████╗███╗   ███╗██████╗ ██╗      
██╔══██╗██╔════╝██╔════╝██╔════╝████╗ ████║██╔══██╗██║     ██╗████╗
███████║╚█████╗ ╚█████╗ █████╗  ██╔████╔██║██████╦╝██║     ███╔═══╝
██╔══██║ ╚═══██╗ ╚═══██╗██╔══╝  ██║╚██╔╝██║██╔══██╗██║     ██╔╝
██║  ██║██████╔╝██████╔╝███████╗██║ ╚═╝ ██║██████╦╝███████╗██║ 
╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  
""",
        assemblr_logo_small = """ ___  __  __  _______  _______ __   ____ 
// \\(( \(( \||   ||\\//|||| ))||   || \\
||=|| \\  \\ ||== || \/ ||||=) ||   ||_//
|| ||\_))\_))||___||    ||||_))||__||| \\"""
        cpu = """
 ||||||||
-████████-
-████████-
-████████-
-████████-
 ||||||||"""



def print_sprite(sprite):
    print(sprite, end="")