# Create colors class to color text
class colors:
    # Colors for text
    BLACK = "\u001b[30m"
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    PURPLE = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"

    # Colors for background
    BLACK_BG = "\u001b[40m"
    RED_BG = "\u001b[41m"
    GREEN_BG = "\u001b[42m"
    YELLOW_BG = "\u001b[43m"
    BLUE_BG = "\u001b[44m"
    PURPLE_BG = "\u001b[45m"
    CYAN_BG = "\u001b[46m"
    WHITE_BG = "\u001b[47m"


    # Reset color
    RESET = "\u001b[0m"

# Tests for each color
print(colors.BLACK + "BLACK" + colors.RESET)
print(colors.RED + "RED" + colors.RESET)
print(colors.GREEN + "GREEN" + colors.RESET)
print(colors.YELLOW + "YELLOW" + colors.RESET)
print(colors.BLUE + "BLUE" + colors.RESET)
print(colors.PURPLE + "PURPLE" + colors.RESET)
print(colors.CYAN + "CYAN" + colors.RESET)
print(colors.WHITE + "WHITE" + colors.RESET)

# tests for each background color
print(colors.BLACK_BG + "BLACK_BG" + colors.RESET)
print(colors.RED_BG + "RED_BG" + colors.RESET)
print(colors.GREEN_BG + "GREEN_BG" + colors.RESET)
print(colors.YELLOW_BG + "YELLOW_BG" + colors.RESET)
print(colors.BLUE_BG + "BLUE_BG" + colors.RESET)
print(colors.PURPLE_BG + "PURPLE_BG" + colors.RESET)
print(colors.CYAN_BG + "CYAN_BG" + colors.RESET)
print(colors.WHITE_BG + "WHITE_BG" + colors.RESET)

# tests for combining colors and background colors
print(colors.RED + colors.BLUE_BG + "RED + BLUE_BG" + colors.RESET)
print(colors.GREEN + colors.YELLOW_BG + "GREEN + YELLOW_BG" + colors.RESET)
print(colors.YELLOW + colors.GREEN_BG + "YELLOW + GREEN_BG" + colors.RESET)
print(colors.BLUE + colors.RED_BG + "BLUE + RED_BG" + colors.RESET)
print(colors.PURPLE + colors.CYAN_BG + "PURPLE + CYAN_BG" + colors.RESET)
print(colors.CYAN + colors.PURPLE_BG + "CYAN + PURPLE_BG" + colors.RESET)
print(colors.WHITE + colors.BLACK_BG + "WHITE + BLACK_BG" + colors.RESET)
print(colors.BLACK + colors.WHITE_BG + "BLACK + WHITE_BG" + colors.RESET)

