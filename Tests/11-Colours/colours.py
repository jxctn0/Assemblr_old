class Color:
    def __init__(self, _name: str, _r: int =0, _g: int =0, _b: int =0, _hex: str ="", _h: float =0, _s: float =0, _v: float =0, _c: int =0, _y: int =0, _m: int =0, _k: int =0):
        #^ RGB
        arguments = [_r, _g, _b, _hex, _h, _s, _v, _c, _m, _y, _k]
        if sum([1 for arg in arguments if arg != 0]) > 1:
            raise ValueError("Only one colour model can be used at a time")
        
        if _r and _g and _b:
            # check if the values are within the range
            if _r > 255 or _r < 0 or _g > 255 or _g < 0 or _b > 255 or _b < 0:
                raise ValueError("RGB values must be between 0 and 255")
            self.r = _r
            self.g = _g
            self.b = _b

        elif _hex:
            self.r, self.g, self.b = self.hex_to_rgb(_hex)


    def hex_to_rgb(self, hex: str) -> tuple:
        hex = hex.lstrip("#")
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    
    def hsv_to_rgb(self, h: float, s: float, v: float) -> tuple:
        h = h / 360
        s = s / 100
        v = v / 100
        c = v * s
        x = c * (1 - abs((h * 6) % 2 - 1))
        m = v - c
        if h < 1/6:
            r, g, b = c, x, 0
        elif h < 2/6:
            r, g, b = x, c, 0
        elif h < 3/6:
            r, g, b = 0, c, x
        elif h < 4/6:
            r, g, b = 0, x, c
        elif h < 5/6:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x
        return (int((r + m) * 255), int((g + m) * 255), int((b + m) * 255))
    
    def cmyk_to_rgb(self, c: int, m: int, y: int, k: int) -> tuple:
        r = 255 * (1 - c) * (1 - k)
        g = 255 * (1 - m) * (1 - k)
        b = 255 * (1 - y) * (1 - k)
        return (int(r), int(g), int(b))
    
    def __str__(self) -> str:
        return f"{self.name}: RGB({self.r}, {self.g}, {self.b})"
    
    def __repr__(self) -> str:
        return f"{self.name}: RGB({self.r}, {self.g}, {self.b})"
    
    def value(self) -> str:
        #? return a colour to be printed in the terminal
        return f"\033[38;2;{self.r};{self.g};{self.b}m{self.name}\033[0m"
    

#? Create a list of random colours to test the class
test_colours = [
    #? RGB
    Color("Red", _r=255),