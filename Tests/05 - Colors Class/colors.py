# Create colors class to color text
class colors:
    class foreground:
        # Colors for text
        BLACK = "\u001b[30m"
        RED = "\u001b[31m"
        GREEN = "\u001b[32m"
        YELLOW = "\u001b[33m"
        BLUE = "\u001b[34m"
        PURPLE = "\u001b[35m"
        CYAN = "\u001b[36m"
        WHITE = "\u001b[37m"

    class background:
        # Colors for background
        BLACK = "\u001b[40m"
        RED = "\u001b[41m"
        GREEN = "\u001b[42m"
        YELLOW = "\u001b[43m"
        BLUE = "\u001b[44m"
        PURPLE = "\u001b[45m"
        CYAN = "\u001b[46m"
        WHITE = "\u001b[47m"

    class formatting:
        # Reset color
        RESET = "\u001b[0m"
        # Formatting
        BOLD = "\u001b[1m"
        ITALIC = "\u001b[3m"
        UNDERLINE = "\u001b[4m"
        BLINK = "\u001b[5m"
        REVERSED = "\u001b[7m"

"""
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
print(colors.BLACK + "BLACK" + colors.RESET)
print(colors.RED + "RED" + colors.RESET)
print(colors.GREEN + "GREEN" + colors.RESET)
print(colors.YELLOW + "YELLOW" + colors.RESET)
print(colors.BLUE + "BLUE" + colors.RESET)
print(colors.PURPLE + "PURPLE" + colors.RESET)
print(colors.CYAN + "CYAN" + colors.RESET)
print(colors.WHITE + "WHITE" + colors.RESET)

# tests for combining colors and background colors
print(colors.RED + colors.BLUE + "RED + BLUE" + colors.RESET)
print(colors.GREEN + colors.YELLOW + "GREEN + YELLOW" + colors.RESET)
print(colors.YELLOW + colors.GREEN + "YELLOW + GREEN" + colors.RESET)
print(colors.BLUE + colors.RED + "BLUE + RED" + colors.RESET)
print(colors.PURPLE + colors.CYAN + "PURPLE + CYAN" + colors.RESET)
print(colors.CYAN + colors.PURPLE + "CYAN + PURPLE" + colors.RESET)
print(colors.WHITE + colors.BLACK + "WHITE + BLACK" + colors.RESET)
print(colors.BLACK + colors.WHITE + "BLACK + WHITE" + colors.RESET)
"""
# tests to figure out all codes from 1-100
for i in range(0, 100):
    print(colors.foreground.BLACK + colors.background.RED +" \u001b[" + str(i) + "m" + str(i) + " ", colors.formatting.RESET)