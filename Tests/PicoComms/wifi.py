# wifi.py

import network  # Import the network module
import time

def connect(WIFI_SSID, WIFI_PASSWORD, oled=None):
    wlan = network.WLAN(network.STA_IF)  # Create a WLAN object
    wlan.active(True)  # Activate the WLAN interface

    if not wlan.isconnected():  # Check if not already connected
        print('Connecting to WiFi...', end=".")
        if oled:
            oled.println("Connecting to WiFi...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)  # Connect to the WiFi network

        while not wlan.isconnected():  # Wait until connected
            time.sleep(0.5)
            print(".", end="")
        print()

    print('WiFi connected!')
    print('Network config:', wlan.ifconfig())  # Print network configuration

    if oled:
        # Display WiFi information on the OLED display
        oled.clear()  # Clear the display
        oled.println("WiFi Name: ")  # Display WiFi name
        oled.println(WIFI_SSID)
        oled.println("IP: " + wlan.ifconfig()[0])  # Display IP address
        oled.println("Connected")  # Display "Connected" message
