import serial
import time

# Configure the serial connection
arduino_port = "COM3"  # Replace with your Arduino's COM port
baud_rate = 115200
arduino = serial.Serial(arduino_port, baud_rate, timeout=1)

# Wait for Arduino to initialize
time.sleep(2)

# Function to send commands to Arduino
def send_command(command):
    if arduino.is_open:
        arduino.write(command.encode())
        time.sleep(0.1)  # Allow time for Arduino to process
        while arduino.in_waiting > 0:
            response = arduino.readline().decode('utf-8').strip()
            print("Arduino response:", response)

# Example usage
try:
    send_command('F')  # Move forward
    time.sleep(2)
    send_command('L')  # Turn left
    time.sleep(2)
    send_command('S')  # Stop
except KeyboardInterrupt:
    print("Stopping communication")
finally:
    arduino.close()
