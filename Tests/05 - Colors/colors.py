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

# Tests for all colors and formatting

# foreground colors
print(colors.foreground.black + "BLACK" + colors.formatting.reset)
print(colors.foreground.red + "RED" + colors.formatting.reset)
print(colors.foreground.green + "GREEN" + colors.formatting.reset)
print(colors.foreground.yellow + "YELLOW" + colors.formatting.reset)
print(colors.foreground.blue + "BLUE" + colors.formatting.reset)
print(colors.foreground.purple + "PURPLE" + colors.formatting.reset)
print(colors.foreground.cyan + "CYAN" + colors.formatting.reset)
print(colors.foreground.white + "WHITE" + colors.formatting.reset)

# background colors
print(colors.background.black + "BLACK" + colors.formatting.reset)
print(colors.background.red + "RED" + colors.formatting.reset)
print(colors.background.green + "GREEN" + colors.formatting.reset)
print(colors.background.yellow + "YELLOW" + colors.formatting.reset)
print(colors.background.blue + "BLUE" + colors.formatting.reset)
print(colors.background.purple + "PURPLE" + colors.formatting.reset)
print(colors.background.cyan + "CYAN" + colors.formatting.reset)
print(colors.background.white + "WHITE" + colors.formatting.reset)

# formatting
print(colors.formatting.bold + "BOLD" + colors.formatting.reset)
print(colors.formatting.dim + "DIM" + colors.formatting.reset)
print(colors.formatting.italic + "ITALIC" + colors.formatting.reset)
print(colors.formatting.underline + "UNDERLINE" + colors.formatting.reset)
print(colors.formatting.slow_blink + "SLOW_BLINK" + colors.formatting.reset)
print(colors.formatting.rapid_blink + "RAPID_BLINK" + colors.formatting.reset)
print(colors.formatting.reverse + "REVERSE" + colors.formatting.reset)
print(colors.formatting.hide + "HIDE" + colors.formatting.reset)
print(colors.formatting.strikethrough + "STRIKETHROUGH" + colors.formatting.reset)

# tests for combining foreground colors and background colors
print(colors.foreground.red + colors.background.blue + "RED + BLUE_BG" + colors.formatting.reset)
print(colors.foreground.green + colors.background.yellow + "GREEN + YELLOW_BG" + colors.formatting.reset)
print(colors.foreground.yellow + colors.background.green + "YELLOW + GREEN_BG" + colors.formatting.reset)
print(colors.foreground.blue + colors.background.red + "BLUE + RED_BG" + colors.formatting.reset)

# tests for combining foreground colors and formatting
print(colors.foreground.red + colors.formatting.bold + "RED + BOLD" + colors.formatting.reset)
print(colors.foreground.green + colors.formatting.italic + "GREEN + ITALIC" + colors.formatting.reset)
print(colors.foreground.yellow + colors.formatting.underline + "YELLOW + UNDERLINE" + colors.formatting.reset)
print(colors.foreground.blue + colors.formatting.slow_blink + "BLUE + SLOW_BLINK" + colors.formatting.reset)
print(colors.foreground.purple + colors.formatting.rapid_blink + "PURPLE + RAPID_BLINK" + colors.formatting.reset)
print(colors.foreground.cyan + colors.formatting.reverse + "CYAN + REVERSE" + colors.formatting.reset)
print(colors.foreground.white + colors.formatting.hide + "WHITE + HIDE" + colors.formatting.reset)
print(colors.foreground.black + colors.formatting.strikethrough + "BLACK + STRIKETHROUGH" + colors.formatting.reset)

# tests for combining background colors and formatting
print(colors.background.red + colors.formatting.bold + "RED_BG + BOLD" + colors.formatting.reset)
print(colors.background.green + colors.formatting.italic + "GREEN_BG + ITALIC" + colors.formatting.reset)
print(colors.background.yellow + colors.formatting.underline + "YELLOW_BG + UNDERLINE" + colors.formatting.reset)
print(colors.background.blue + colors.formatting.slow_blink + "BLUE_BG + SLOW_BLINK" + colors.formatting.reset)
print(colors.background.purple + colors.formatting.rapid_blink + "PURPLE_BG + RAPID_BLINK" + colors.formatting.reset)
print(colors.background.cyan + colors.formatting.reverse + "CYAN_BG + REVERSE" + colors.formatting.reset)
print(colors.background.white + colors.formatting.hide + "WHITE_BG + HIDE" + colors.formatting.reset)
print(colors.background.black + colors.formatting.strikethrough + "BLACK_BG + STRIKETHROUGH" + colors.formatting.reset)

# tests for combining foreground colors, background colors, and formatting
print(colors.foreground.red + colors.background.blue + colors.formatting.bold + "RED + BLUE_BG + BOLD" + colors.formatting.reset)
print(colors.foreground.green + colors.background.yellow + colors.formatting.italic + "GREEN + YELLOW_BG + ITALIC" + colors.formatting.reset)
print(colors.foreground.yellow + colors.background.green + colors.formatting.underline + "YELLOW + GREEN_BG + UNDERLINE" + colors.formatting.reset)
print(colors.foreground.blue + colors.background.red + colors.formatting.slow_blink + "BLUE + RED_BG + SLOW_BLINK" + colors.formatting.reset)
print(colors.foreground.purple + colors.background.cyan + colors.formatting.rapid_blink + "PURPLE + CYAN_BG + RAPID_BLINK" + colors.formatting.reset)
print(colors.foreground.cyan + colors.background.purple + colors.formatting.reverse + "CYAN + PURPLE_BG + REVERSE" + colors.formatting.reset)
print(colors.foreground.white + colors.background.black + colors.formatting.hide + "WHITE + BLACK_BG + HIDE" + colors.formatting.reset)
print(colors.foreground.black + colors.background.white + colors.formatting.strikethrough + "BLACK + WHITE_BG + STRIKETHROUGH" + colors.formatting.reset)

