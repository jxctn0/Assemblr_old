# Tkinter GUI:
# Green background, white text in consolas font, 12px
# Red, green, yellow, and blue LEDs with buttons to "toggle" between on and off

import tkinter as tk

root = tk.Tk()
root.title("Test GUI")
root.geometry("800x600")
root.config(bg="green")

# Red LED
red_led = tk.Label(root, text="R", bg="red", fg="white", font=("consolas", 12), width=10, height=2)
red_led.pack()

# Green LED
green_led = tk.Label(root, text="G", bg="green", fg="white", font=("consolas", 12), width=10, height=2)
green_led.pack()

# Yellow LED
yellow_led = tk.Label(root, text="Y", bg="yellow", fg="white", font=("consolas", 12), width=10, height=2)
yellow_led.pack()

# Blue LED
blue_led = tk.Label(root, text="B", bg="blue", fg="white", font=("consolas", 12), width=10, height=2)
blue_led.pack()

# Functionality for the red LED button to make it toggle between on and off
def red_led_click():
    if red_led["bg"] == "red":
        red_led.config(bg="gray")
    else:
        red_led.config(bg="red")

red_led_button = tk.Button(root, text="Toggle Red LED", command=red_led_click)
red_led_button.pack()

# Functionality for the green LED button to make it toggle between on and off
def green_led_click():
    if green_led["bg"] == "green":
        green_led.config(bg="gray")
    else:
        green_led.config(bg="green")

green_led_button = tk.Button(root, text="Toggle Green LED", command=green_led_click)
green_led_button.pack()

# Functionality for the yellow LED button to make it toggle between on and off
def yellow_led_click():
    if yellow_led["bg"] == "yellow":
        yellow_led.config(bg="gray")
    else:
        yellow_led.config(bg="yellow")

yellow_led_button = tk.Button(root, text="Toggle Yellow LED", command=yellow_led_click)
yellow_led_button.pack()

# Functionality for the blue LED button to make it toggle between on and off
def blue_led_click():
    if blue_led["bg"] == "blue":
        blue_led.config(bg="gray")
    else:
        blue_led.config(bg="blue")

blue_led_button = tk.Button(root, text="Toggle Blue LED", command=blue_led_click)
blue_led_button.pack()

root.mainloop()