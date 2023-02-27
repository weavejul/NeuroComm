from tkinter import N
import serial
import time
import os
from multiprocessing import Process

# Start serial log

arduino = serial.Serial(port = 'COM3', baudrate = 9600, timeout = .1)

# Threshold values
threshold = 70
isThresholdPassed = False

# Read Arduino Serial Data
def read():
    data = arduino.readlines()
    return data

def countdown():
    print("Concentrate for yes, read the text for no.")
    input("Press enter to start.")
    os.system("cls")
    time.sleep(3)
    print("15 seconds")
    time.sleep(1)
    print("14 seconds")
    time.sleep(1)
    print("13 seconds")
    time.sleep(1)
    print("12 seconds")
    time.sleep(1)
    print("11 seconds")
    time.sleep(1)
    print("10 seconds")
    time.sleep(1)
    print("9 seconds")
    time.sleep(1)
    print("8 seconds")
    time.sleep(1)
    print("7 seconds")
    time.sleep(1)
    print("6 seconds")
    time.sleep(1)
    print("5 seconds")
    time.sleep(1)
    print("4 seconds")
    time.sleep(1)
    print("3 seconds")
    time.sleep(1)
    print("2 seconds")
    time.sleep(1)
    print("1 seconds")
    time.sleep(1)
    print("Getting value")

# Check for attention threshold from the serial data
while True:
    countdown()
    valueFound = False
    while not valueFound:
        value = read()[-1]
        if value:
            try:
                value = value.decode().strip()
                if not value.isspace() and len(value) > 1:
                    #print(value.split(","))
                    currentBrainValue = int(value.split(",")[1])
                    print(currentBrainValue)
                    print("This corresponds to", "YES." if currentBrainValue > threshold else "NO.")
                    valueFound = True
            except:
                print("value error found.")

def yesOrNo():
    while True:
        time.sleep(5)
        if isThresholdPassed:
            print("yes")
        else:
            print("no")

processlist = []
processlist.append(Process(target=constantCheck))
processlist.append(Process(target=yesOrNo))

for t in processlist:
    t.start()
for t in processlist:
    t.join()