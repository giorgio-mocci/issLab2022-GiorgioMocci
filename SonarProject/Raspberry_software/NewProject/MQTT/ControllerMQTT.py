import RPi.GPIO as GPIO
import time
from paho.mqtt.client import Client
import sys
import socket

statoLed = False
Dlimit = float(sys.argv[1])
client = Client(client_id = "Controller")
client.connect(sys.argv[2])
client.subscribe("sonar")

def on_connect(client, userdata, flags, rc):
    print("Connesso con successo")




def on_message(client, userdata, message):
    global statoLed
    print("ho ricevuto una nuova misurazione :" + message.payload.decode())
    cm = float(message.payload.decode())
    if cm < Dlimit and statoLed == False:
                client.publish(topic = "led", payload = "ON")
                statoLed = True
                print("Accendo il led")
    elif cm >= Dlimit and statoLed == True:
                client.publish(topic = "led", payload = "OFF")
                statoLed = False
                print("Spengo il led")

    client.publish(topic = "radar", payload = cm)





    #print(message.topic +  message.payload.decode() )

client.on_connect = on_connect
client.on_message = on_message



client.loop_forever()
