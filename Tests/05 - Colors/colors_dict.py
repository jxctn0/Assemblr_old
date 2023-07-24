colors = {
    "foreground": {
        "black": "\u001b[30m",
        "red": "\u001b[31m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33m",
        "blue": "\u001b[34m",
        "purple": "\u001b[35m",
        "cyan": "\u001b[36m",
        "white": "\u001b[37m"
    },
    "background": {
        "black": "\u001b[40m",
        "red": "\u001b[41m",
        "green": "\u001b[42m",
        "yellow": "\u001b[43m",
        "blue": "\u001b[44m",
        "purple": "\u001b[45m",
        "cyan": "\u001b[46m",
        "white": "\u001b[47m"
    },
    "formatting": {
        "reset": "\u001b[0m",
        "bold": "\u001b[1m",
        "italic": "\u001b[3m",
        "underline": "\u001b[4m",
        "blink": "\u001b[5m",
        "reversed": "\u001b[7m"
}

}

# Tests for foreground color
print(colors["foreground"]["black"] + "BLACK" + colors["formatting"]["reset"])
print(colors["foreground"]["red"] + "RED" + colors["formatting"]["reset"])

# Tests for background color
print(colors["background"]["black"] + "BLACK" + colors["formatting"]["reset"])
print(colors["background"]["red"] + "RED" + colors["formatting"]["reset"])

# Tests for formatting
print(colors["formatting"]["bold"] + "BOLD" + colors["formatting"]["reset"])
print(colors["formatting"]["italic"] + "ITALIC" + colors["formatting"]["reset"])

# Tests for combining colors and background colors
print(colors["foreground"]["red"] + colors["background"]["blue"] + "RED + BLUE_BG" + colors["formatting"]["reset"])
print(colors["foreground"]["green"] + colors["background"]["yellow"] + "GREEN + YELLOW_BG" + colors["formatting"]["reset"])

# Tests for combining colors and formatting
print(colors["foreground"]["red"] + colors["formatting"]["bold"] + "RED + BOLD" + colors["formatting"]["reset"])
print(colors["foreground"]["green"] + colors["formatting"]["italic"] + "GREEN + ITALIC" + colors["formatting"]["reset"])

# Tests for combining background colors and formatting
print(colors["background"]["red"] + colors["formatting"]["bold"] + "RED_BG + BOLD" + colors["formatting"]["reset"])
print(colors["background"]["green"] + colors["formatting"]["italic"] + "GREEN_BG + ITALIC" + colors["formatting"]["reset"])

# Tests for combining colors, background colors, and formatting
print(colors["foreground"]["red"] + colors["background"]["blue"] + colors["formatting"]["bold"] + "RED + BLUE_BG + BOLD" + colors["formatting"]["reset"])
print(colors["foreground"]["green"] + colors["background"]["yellow"] + colors["formatting"]["italic"] + "GREEN + YELLOW_BG + ITALIC" + colors["formatting"]["reset"])
print(colors["foreground"]["yellow"] + colors["background"]["green"] + colors["formatting"]["bold"] + "YELLOW + GREEN_BG + BOLD" + colors["formatting"]["reset"])
print(colors["foreground"]["blue"] + colors["background"]["red"] + colors["formatting"]["italic"] + "BLUE + RED_BG + ITALIC" + colors["formatting"]["reset"])

# tests for random colors and formatting
import random
print(random.choice(list(colors["foreground"].values())) + random.choice(list(colors["background"].values())) + random.choice(list(colors["formatting"].values())) + "RANDOM" + colors["formatting"]["reset"])
print(random.choice(list(colors["foreground"].values())) + random.choice(list(colors["background"].values())) + random.choice(list(colors["formatting"].values())) + "RANDOM" + colors["formatting"]["reset"])
print(random.choice(list(colors["foreground"].values())) + random.choice(list(colors["background"].values())) + random.choice(list(colors["formatting"].values())) + "RANDOM" + colors["formatting"]["reset"])