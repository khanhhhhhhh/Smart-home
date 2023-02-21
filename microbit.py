from pydoc import cli

import serial.tools.list_ports
import time


def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort
    # return "COM4"
isMicrobitConnected = False
if getPort()!="None":
    ser = serial.Serial( port=getPort(), baudrate=115200)
    isMicrobitConnected = True

def processData(data, client):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    try:
        if splitData[1] == "TEMPERATURE":
            client.publish("cambien1", splitData[2])
        elif splitData[1] == "HUMIDITY":
            client.publish("cambien2", splitData[2])
        elif splitData[1] == "LIGHT":
            client.publish("cambien3", splitData[2])
    except:
        pass
mess = ""
read_splitdata = ""
def readSerial(client):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            # global read_splitdata
            read_splitdata = processData(mess[start:end + 1], client)
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

def writeData(data):
    ser.write(str(data).encode())


