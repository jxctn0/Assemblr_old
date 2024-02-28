import socket
import time
import wifi  # Import the wifi module
from oled import I2C_Display  # Import the I2C_Display class from the i2c_display module


class Transmitter:
    def __init__(self, pc_ip, pc_port, wifi_ssid, wifi_password, display):
        self.pc_ip = pc_ip
        self.pc_port = pc_port
        self.wifi_ssid = wifi_ssid
        self.wifi_password = wifi_password
        self.display = display
        self.connection = None

        self.codes = {"kill": 0, "execute": 1, "pause": 2, "resume": 3}

    def connect_wifi(self):
        wifi.connect(self.wifi_ssid, self.wifi_password, oled=self.display)

    def aknowledge(self):
        self.connection.sendall(b"Acknowledged")

    def execute_control_code(self, control_code):
        if control_code == "kill":
            print("Killing the program")
            # Kill the program
            pass
        elif control_code == "execute":
            print("Executing the program")
            # Execute the program
            pass
        elif control_code == "pause":
            print("Pausing the program")
            # Pause the program
            pass
        elif control_code == "resume":
            print("Resuming the program")
            # Resume the program
            pass

    def start_transmitter(self):
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Bind the socket to the IP address and port
            s.bind((self.pc_ip, self.pc_port))

            # Listen for incoming connections
            s.listen(1)

            print("Waiting for connection from PC...")

            # Accept the connection
            self.connection, addr = s.accept()
            print("Connected to PC:", addr)

            while True:
                # Receive data from PC
                data = self.connection.recv(1024)
                if not data:
                    break

                # handle control characters
                if data[0] == "\ue0100":
                    # Handle the following control codes:

                    # Get the control code
                    control_code = data[1:]

                    # Print the control code
                    print("Control Code Recieved:", control_code)

                    # Send acknowledgement to PC
                    self.aknowledge()

                    # Execute the control code
                    if control_code in codes:
                        # Execute the control code
                        print("Executing Control Code:", control_code)
                        execute_control_code(control_code)

                    else:
                        print("Invalid Control Code")

                # Print received message
                print("Received message:", data.decode())

                # Send acknowledgement to PC
                conn.sendall(b"Acknowledged")

        except Exception as e:
            print("An error occurred:", e)

        finally:
            # Close the connection
            conn.close()
            # Close the socket
            s.close()


def main():
    try:
        # Create an instance of the I2C_Display class
        display = I2C_Display(width=128, height=64, scl_pin=1, sda_pin=0)

        # Define the IP address and port of the PC
        PC_IP = "0.0.0.0"  # Replace this with the actual IP address of your PC
        PC_PORT = 12345  # Make sure it's the same port as in PC_side.py

        # Define the WiFi credentials
        WIFI_SSID = "VM5831942"
        WIFI_PASSWORD = "bmztKvw8fXr5aiyn"

        # Create Transmitter instance
        transmitter = Transmitter(PC_IP, PC_PORT, WIFI_SSID, WIFI_PASSWORD, display)

        # Connect to WiFi
        transmitter.connect_wifi()

        # Start the transmitter
        transmitter.start_transmitter()

    except Exception as e:
        print("Something Happened:", e)
        # Clear the display
        I2C_Display(width=128, height=64, scl_pin=1, sda_pin=0).clean()
