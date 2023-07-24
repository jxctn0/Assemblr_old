# Create colors class to color text
class colors:
    class fg:
        # Colors for text
        black = "\u001b[30m"
        red = "\u001b[31m"
        green = "\u001b[32m"
        yellow = "\u001b[33m"
        blue = "\u001b[34m"
        purple = "\u001b[35m"
        cyan = "\u001b[36m"
        white = "\u001b[37m"

    class bg:
        # Colors for bg
        black = "\u001b[40m"
        red = "\u001b[41m"
        green = "\u001b[42m"
        yellow = "\u001b[43m"
        blue = "\u001b[44m"
        purple = "\u001b[45m"
        cyan = "\u001b[46m"
        white = "\u001b[47m"

    class fmt:
        """
        0	Reset all attributes
        1	Bold (increased intensity)
        2	Dim (decreased intensity)
        3	Italic
        4	Underline
        5	Slow Blink
        6	Rapid Blink
        7	Swap fg and bg colors (reverse format)
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

# Tests for all colors and fmt

# fg colors
print(colors.fg.black + "BLACK" + colors.fmt.reset)
print(colors.fg.red + "RED" + colors.fmt.reset)
print(colors.fg.green + "GREEN" + colors.fmt.reset)
print(colors.fg.yellow + "YELLOW" + colors.fmt.reset)
print(colors.fg.blue + "BLUE" + colors.fmt.reset)
print(colors.fg.purple + "PURPLE" + colors.fmt.reset)
print(colors.fg.cyan + "CYAN" + colors.fmt.reset)
print(colors.fg.white + "WHITE" + colors.fmt.reset)

# bg colors
print(colors.bg.black + "BLACK" + colors.fmt.reset)
print(colors.bg.red + "RED" + colors.fmt.reset)
print(colors.bg.green + "GREEN" + colors.fmt.reset)
print(colors.bg.yellow + "YELLOW" + colors.fmt.reset)
print(colors.bg.blue + "BLUE" + colors.fmt.reset)
print(colors.bg.purple + "PURPLE" + colors.fmt.reset)
print(colors.bg.cyan + "CYAN" + colors.fmt.reset)
print(colors.bg.white + "WHITE" + colors.fmt.reset)

# fmt
print(colors.fmt.bold + "BOLD" + colors.fmt.reset)
print(colors.fmt.dim + "DIM" + colors.fmt.reset)
print(colors.fmt.italic + "ITALIC" + colors.fmt.reset)
print(colors.fmt.underline + "UNDERLINE" + colors.fmt.reset)
print(colors.fmt.slow_blink + "SLOW_BLINK" + colors.fmt.reset)
print(colors.fmt.rapid_blink + "RAPID_BLINK" + colors.fmt.reset)
print(colors.fmt.reverse + "REVERSE" + colors.fmt.reset)
print(colors.fmt.hide + "HIDE" + colors.fmt.reset)
print(colors.fmt.strikethrough + "STRIKETHROUGH" + colors.fmt.reset)

# tests for combining fg colors and bg colors
print(colors.fg.red + colors.bg.blue + "RED + BLUE_BG" + colors.fmt.reset)
print(colors.fg.green + colors.bg.yellow + "GREEN + YELLOW_BG" + colors.fmt.reset)
print(colors.fg.yellow + colors.bg.green + "YELLOW + GREEN_BG" + colors.fmt.reset)
print(colors.fg.blue + colors.bg.red + "BLUE + RED_BG" + colors.fmt.reset)

# tests for combining fg colors and fmt
print(colors.fg.red + colors.fmt.bold + "RED + BOLD" + colors.fmt.reset)
print(colors.fg.green + colors.fmt.italic + "GREEN + ITALIC" + colors.fmt.reset)
print(colors.fg.yellow + colors.fmt.underline + "YELLOW + UNDERLINE" + colors.fmt.reset)
print(colors.fg.blue + colors.fmt.slow_blink + "BLUE + SLOW_BLINK" + colors.fmt.reset)
print(colors.fg.purple + colors.fmt.rapid_blink + "PURPLE + RAPID_BLINK" + colors.fmt.reset)
print(colors.fg.cyan + colors.fmt.reverse + "CYAN + REVERSE" + colors.fmt.reset)
print(colors.fg.white + colors.fmt.hide + "WHITE + HIDE" + colors.fmt.reset)
print(colors.fg.black + colors.fmt.strikethrough + "BLACK + STRIKETHROUGH" + colors.fmt.reset)

# tests for combining bg colors and fmt
print(colors.bg.red + colors.fmt.bold + "RED_BG + BOLD" + colors.fmt.reset)
print(colors.bg.green + colors.fmt.italic + "GREEN_BG + ITALIC" + colors.fmt.reset)
print(colors.bg.yellow + colors.fmt.underline + "YELLOW_BG + UNDERLINE" + colors.fmt.reset)
print(colors.bg.blue + colors.fmt.slow_blink + "BLUE_BG + SLOW_BLINK" + colors.fmt.reset)
print(colors.bg.purple + colors.fmt.rapid_blink + "PURPLE_BG + RAPID_BLINK" + colors.fmt.reset)
print(colors.bg.cyan + colors.fmt.reverse + "CYAN_BG + REVERSE" + colors.fmt.reset)
print(colors.bg.white + colors.fmt.hide + "WHITE_BG + HIDE" + colors.fmt.reset)
print(colors.bg.black + colors.fmt.strikethrough + "BLACK_BG + STRIKETHROUGH" + colors.fmt.reset)

# tests for combining fg colors, bg colors, and fmt
print(colors.fg.red + colors.bg.blue + colors.fmt.bold + "RED + BLUE_BG + BOLD" + colors.fmt.reset)
print(colors.fg.green + colors.bg.yellow + colors.fmt.italic + "GREEN + YELLOW_BG + ITALIC" + colors.fmt.reset)
print(colors.fg.yellow + colors.bg.green + colors.fmt.underline + "YELLOW + GREEN_BG + UNDERLINE" + colors.fmt.reset)
print(colors.fg.blue + colors.bg.red + colors.fmt.slow_blink + "BLUE + RED_BG + SLOW_BLINK" + colors.fmt.reset)
print(colors.fg.purple + colors.bg.cyan + colors.fmt.rapid_blink + "PURPLE + CYAN_BG + RAPID_BLINK" + colors.fmt.reset)
print(colors.fg.cyan + colors.bg.purple + colors.fmt.reverse + "CYAN + PURPLE_BG + REVERSE" + colors.fmt.reset)
print(colors.fg.white + colors.bg.black + colors.fmt.hide + "WHITE + BLACK_BG + HIDE" + colors.fmt.reset)
print(colors.fg.black + colors.bg.white + colors.fmt.strikethrough + "BLACK + WHITE_BG + STRIKETHROUGH" + colors.fmt.reset)


# Make "presets" for colors & fmt
class presets:
    screen = colors.fg.white + colors.bg.black + colors.fmt.reset