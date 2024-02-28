import socket

class Device:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        try:
            # Connect to the device
            self.socket.connect((self.ip, self.port))
            print("Connected to device.")
        except Exception as e:
            print("An error occurred while connecting:", e)
    
    def send_message(self, message):
        try:
            # Send the message
            self.socket.sendall(message.encode())
            print("Message sent.")
        except Exception as e:
            print("An error occurred while sending message:", e)
    
    def receive_acknowledgement(self):
        try:
            # Wait for acknowledgement
            ack = self.socket.recv(1024)
            print("Acknowledgement:", ack.decode())
        except Exception as e:
            print("An error occurred while receiving acknowledgement:", e)
    
    def close_connection(self):
        try:
            # Close the socket
            self.socket.close()
            print("Connection closed.")
        except Exception as e:
            print("An error occurred while closing connection:", e)

def main():
    # Define the IP address and port of the Raspberry Pi Pico
    PICO_IP = '192.168.0.64'  # Replace this with the actual IP address of your Raspberry Pi Pico
    PICO_PORT = 12345  # Choose a port number
    
    # Create a Device object
    device = Device(PICO_IP, PICO_PORT)
    
    try:
        # Connect to the device
        device.connect()
        
        while True:
            code = None
            # get code to send message
            while not code:
                code = int(input("Enter code to transmit: "))
                if code in range(-1,10):
                    break
                else:
                    print("Invalid code")
                    code = None
            # Get user input for the message
            message = input("Enter message to transmit: ")

            # Add the code to the message
            message = str(code) + message
            
            # Send the message to the device
            device.send_message(message)
            
            # Wait for acknowledgement from the device
            device.receive_acknowledgement()
    
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    
    finally:
        # Close the connection
        device.close_connection()

if __name__ == "__main__":
    main()
