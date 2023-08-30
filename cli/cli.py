# All functions for the CLI

# Import modules

# Import custom modules

# Set Formatting class

class fmt:
    class fg: # Foreground Colours
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        yellow = "\033[33m"
        blue = "\033[34m"
        magenta = "\033[35m"
        cyan = "\033[36m"
        white = "\033[37m"
        class br: # Bright
            black = "\033[30;1m"
            red = "\033[31;1m"
            green = "\033[32;1m"
            yellow = "\033[33;1m"
            blue = "\033[34;1m"
            magenta = "\033[35;1m"
            cyan = "\033[36;1m"
            white = "\033[37;1m"
        class dim: # Dim
            black = "\033[30;2m"
            red = "\033[31;2m"
            green = "\033[32;2m"
            yellow = "\033[33;2m"
            blue = "\033[34;2m"
            magenta = "\033[35;2m"
            cyan = "\033[36;2m"
            white = "\033[37;2m"
    class bg: # Background Colours
        black = "\033[40m"
        red = "\033[41m"
        green = "\033[42m"
        yellow = "\033[43m"
        blue = "\033[44m"
        magenta = "\033[45m"
        cyan = "\033[46m"
        white = "\033[47m"
        class br: # Bright
            black = "\033[40;1m"
            red = "\033[41;1m"
            green = "\033[42;1m"
            yellow = "\033[43;1m"
            blue = "\033[44;1m"
            magenta = "\033[45;1m"
            cyan = "\033[46;1m"
            white = "\033[47;1m"
        class dim: # Dim
            black = "\033[40;2m"
            red = "\033[41;2m"
            green = "\033[42;2m"
            yellow = "\033[43;2m"
            blue = "\033[44;2m"
            magenta = "\033[45;2m"
            cyan = "\033[46;2m"
            white = "\033[47;2m"
    class style: # Styles
        reset = "\033[0m"
        bold = "\033[1m"
        dim = "\033[2m"
        italic = "\033[3m"
        underline = "\033[4m"
        blink = "\033[5m"
        reverse = "\033[7m"
        hidden = "\033[8m"
        strike = "\033[9m"
    class notify: # specific notify styles
        info = "\033[1m\033[34m" # bold blue
        fatalError = "\033[1m\033[31m" # bold red
        warning = "\033[1m\033[33m" # bold yellow
        success = "\033[1m\033[32m" # bold green
        debug = "\033[30m\033[43m" # black on yellow



# Set error codes dictionary
# Format: <code>: <message>
# 

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

# Set notify class
class notify:
    # All notify functions follow the same format:
    # <colour> + <bold> + "[<type>] " + <italic> + "[<code>] " + <reset> + <colour> + <message> + <reset>
    
    # Error text
    def error(code, text="", fatal=False):
        if text == "":
            text = ERROR_CODES[code] # Set text to error message if no specific text is given
            # testing
            print("text = " + text)

        print(f" {fmt.fg.red}{fmt.style.bold}[ERROR] {fmt.style.italic}[{code}] {fmt.style.reset}{fmt.fg.red}{text}{fmt.style.reset} ")

        if fatal:
            exit(code)

    # Warning text
    def warning(text):
        print(f" {fmt.fg.yellow}{fmt.style.bold}[WARNING] {fmt.style.reset}{fmt.fg.yellow}{text}{fmt.style.reset} ")

    # Info text
    def info(text):
        print(f" {fmt.fg.blue}{fmt.style.bold}[INFO] {fmt.style.reset}{fmt.fg.blue}{text}{fmt.style.reset} ")

    # Debug text
    def debug(text, type=""):
        if type != "":
            type = f" [{type}] " # Add brackets around type if type is given
        # print in black and yellow
        print(f" {fmt.fg.black + fmt.bg.yellow}{fmt.style.bold}[DEBUG] {fmt.style.italic}{type}{fmt.style.reset}{fmt.fg.black + fmt.bg.yellow}{text}{fmt.style.reset} ")

    # Success text
    def success(text):
        print(f" {fmt.fg.green}{fmt.style.bold}[SUCCESS] {fmt.style.reset}{fmt.fg.green}{text}{fmt.style.reset} ")

################################
#                              #
#    TEMPORARY TESTING CODE    #
#                              #
################################

# Test notify functions
notify.error(0) # No error
notify.error(1) # Unknown error
notify.error(11) # Unknown instruction
notify.error(12) # Syntax error
notify.error(21) # Address not found
notify.error(22) # Address already in use

notify.warning("This is a warning")
notify.info("This is info")
notify.debug("This is debug")
notify.success("This is success")

# Test formatting
print(f"{fmt.fg.red}This is red text{fmt.style.reset}")
print(f"{fmt.fg.red}{fmt.style.bold}This is bold red text{fmt.style.reset}")
print(f"{fmt.fg.red}{fmt.style.italic + fmt.style.bold}This is bold italic red text{fmt.style.reset}")
