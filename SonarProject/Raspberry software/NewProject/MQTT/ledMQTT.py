import RPi.GPIO as GPIO
import time
import sys
import socket
from paho.mqtt.client import Client

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25,GPIO.OUT)

client = Client(client_id = "LEDCLIENT")



def on_connect(client, userdata, flags, rc):
    print("LED Connesso con successo")

def on_message(client, userdata, message):
    print(message.topic +  message.payload.decode() )
    if message.payload.decode() == "ON":
        print ("LED on")
        GPIO.output(25,GPIO.HIGH)
    else :
        print ("LED off")
        GPIO.output(25,GPIO.LOW)

client.on_connect = on_connect
client.on_message = on_message


def StartListening():

    client.connect(sys.argv[1])
    client.subscribe("led")


    client.loop_forever()



StartListening()
