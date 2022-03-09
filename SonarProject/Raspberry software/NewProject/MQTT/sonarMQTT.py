import RPi.GPIO as GPIO
import time
import sys
import socket
from paho.mqtt.client import Client
client = Client("Publisher_test")


TRIG = 17
ECHO = 27

def setup():
    GPIO.setmode(GPIO.BCM)

#    print ("Setup In Progress")
    #Settings GPIO
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)


def on_connect(client, userdata, flags, rc):
    print("Connesso con successo")

def getCM():
    GPIO.output(TRIG, False)
    #print ("Waiting For Sensor To Settle")
    time.sleep(0.1)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
       pulse_start = time.time()
    while GPIO.input(ECHO)==1:
       pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
#    print ("Distance: ",distance,"cm")
    return distance




def StartPublishing():

    while True:
        cm = getCM()
        #print(cm)
        client.publish(topic = "sonar", payload = str(cm))
        time.sleep(0.1)

setup()
client.connect(sys.argv[1])
client.on_connect = on_connect
StartPublishing()
