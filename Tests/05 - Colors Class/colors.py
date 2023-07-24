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

# Tests for each color
print(colors.color.BLACK + "BLACK" + colors.formatting.RESET)
print(colors.color.RED + "RED" + colors.formatting.RESET)
print(colors.color.GREEN + "GREEN" + colors.formatting.RESET)
print(colors.color.YELLOW + "YELLOW" + colors.formatting.RESET)
print(colors.color.BLUE + "BLUE" + colors.formatting.RESET)
print(colors.color.PURPLE + "PURPLE" + colors.formatting.RESET)
print(colors.color.CYAN + "CYAN" + colors.formatting.RESET)
print(colors.color.WHITE + "WHITE" + colors.formatting.RESET)

