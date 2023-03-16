# Simple program to read in bytes from UART and write out to file
# Default file name is LED_values.txt
# Baud rate defaults to 115200
# SJG for CS6780 Mar2023

from datetime import datetime
import serial


def read_data(path, baud_rate, port_name):
    # Open file
    now = datetime.now()
    f = open(path + "LED_values.txt", "a", encoding="ascii")
    f.write("Trial " + now.strftime("%d/%m/%Y_%H:%M:%S") + "\n")

    # Configure + open serial instance
    ser = serial.Serial(port='/dev/ttyAMA0', baudrate=115200)
    ser.open()

    # Idiot check
    if ser.is_open:
        print("Successfully opened port to Disco \n")
        byte = ser.readline()
        print("Read a byte\n")
        f.write(byte)
    else:
        print("Could not interface with Disco... shutting down \n")
        f.write("Could not successfully open serial communication with port " + port_name + "at rate " + baud_rate)

    # Close port and file
    f.close()
    ser.close()


if __name__ == '__main__':
    dir = "/home/whiskers/Documents/"
    br = 115200
    pn = "/dev/ttyAMA0"
    read_data(dir, br, pn)
