# Convert a colour from hex/rgb/hsl to display in the terminal
# Usage: python3 colours.py

# Comment Conventions:
#! - Critical to code / may cause errors
#? - Explains code / may be useful
#^ - Additional information
#* - Example usages
#$ - Important variable
#TODO: - Something to do
#~ - Deprecated line
# FIX - A fix to a previous problem




import colorsys

def color(hex, layer=0):
    # Convert hex to rgb
    hex = hex.lstrip('#')
    rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    # convert rgb to a terminal colour
    r = int(rgb[0] / 255 * 5)
    g = int(rgb[1] / 255 * 5)
    b = int(rgb[2] / 255 * 5)
    
    # if layer is 0, return the colour as fg colour
    if layer == 0:
        return f'\033[38;5;{16 + 36*r + 6*g + b}m'
    # if layer is 1, return the colour as bg colour
    elif layer == 1:
        return f'\033[48;5;{16 + 36*r + 6*g + b}m'

def main():
    # print a rainbow of colours
    for i in range(0, 360, 10):
        h = i / 360
        r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
        print(f'{color(f"{r:02x}{g:02x}{b:02x}")} ', end='')

    # reset the terminal colour
    print('\033[0m')

if __name__ == '__main__':
    
    main()