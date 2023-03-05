# Simple program to read in bytes from UART and write out to file
# Default file name is LED_values.txt
# Baud rate defaults to 115200
# SJG for CS6780 Mar2023

from datetime import datetime
import serial

# Functioning command:
# screen /dev/ttyUSB0 115200


def read_data(path, baud_rate, port_name):
    # Open file
    now = datetime.now()
    f = open(path + "LED_values.txt", "a", encoding="ascii")
    f.write("Trial " + now.strftime("%d/%m/%Y_%H:%M:%S") + "\n")

    # Configure + open serial instance
    ser = serial.Serial(port=port_name, baudrate=baud_rate)

    if ser.is_open:
        print("Successfully opened port to Disco \n")
        byte = ser.read()
        print("Read a byte\n")
        f.write('{}'.format(int.from_bytes(byte,"big")))
    else:
        print("Could not interface with Disco... shutting down \n")
        f.write("Could not successfully open serial communication with port " + port_name + "at rate " + baud_rate)

    # Close port and file
    f.close()
    ser.close()


if __name__ == '__main__':
    dir = "/home/whiskers/Documents/"
    br = 115200
    pn = "/dev/ttyUSB0"
    read_data(dir, br, pn)
