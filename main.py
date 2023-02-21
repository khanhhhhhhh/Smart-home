import random
import time
import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ["cambien1", "cambien2","cambien3"]
AIO_USERNAME = "NgocKhanh07"
AIO_KEY = "aio_FSlB72FeffFWu0Q3dOgamD2Ceptr"

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe("cambien1")
    client.subscribe("cambien2")
    client.subscribe("cambien3")


def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)


client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    valueTemp = random.randint(0,100)
    valueHumid = random.randint(0,100)
    valueLight = random.randint(0,100)
    print("Temp: ", valueTemp)
    print("Humid: ", valueHumid)
    print("Light: ", valueLight)
    client.publish("cambien1", valueTemp)
    client.publish("cambien2", valueHumid)
    client.publish("cambien3", valueLight)
    time.sleep(1)
