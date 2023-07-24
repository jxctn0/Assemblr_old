# Create colors class to color text
class colors:
    class foreground:
        # Colors for text
        black = "\u001b[30m"
        red = "\u001b[31m"
        green = "\u001b[32m"
        yellow = "\u001b[33m"
        blue = "\u001b[34m"
        purple = "\u001b[35m"
        cyan = "\u001b[36m"
        white = "\u001b[37m"

    class background:
        # Colors for background
        black = "\u001b[40m"
        red = "\u001b[41m"
        green = "\u001b[42m"
        yellow = "\u001b[43m"
        blue = "\u001b[44m"
        purple = "\u001b[45m"
        cyan = "\u001b[46m"
        white = "\u001b[47m"

    class formatting:
        """
        0	Reset all attributes
        1	Bold (increased intensity)
        2	Dim (decreased intensity)
        3	Italic
        4	Underline
        5	Slow Blink
        6	Rapid Blink
        7	Swap foreground and background colors (reverse format)
        8	Hide (do not display text)
        9	Strikethrough
        """
        reset = "\u001b[0m"
        bold = "\u001b[1m"
        dim = "\u001b[2m"
        italic = "\u001b[3m"
        underline = "\u001b[4m"
        slow_blink = "\u001b[5m"
        rapid_blink = "\u001b[6m"
        reverse = "\u001b[7m"
        hide = "\u001b[8m"
        strikethrough = "\u001b[9m"

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
    print(" \u001b[" + str(i) + "m" + str(i) + " " + "\u001b[0m")

"""
0	Reset all attributes
1	Bold (increased intensity)
2	Faint (decreased intensity)
3	Italicized
4	Underline
5	Slow Blink
6	Rapid Blink
7	Swap foreground and background colors
8	Hide (do not display text)
9	Crossed-out
"""

