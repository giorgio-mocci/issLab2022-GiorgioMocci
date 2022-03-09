import RPi.GPIO as GPIO
import time
import sys
import socket

TRIG = 17
ECHO = 27

def setup():
    GPIO.setmode(GPIO.BCM)

    print ("Setup In Progress")
    #Settings GPIO
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)


def getCM():
    GPIO.output(TRIG, False)
    print ("Waiting For Sensor To Settle")
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




def StartListening():
    Host = sys.argv[1] # Standard loopback interface address (localhost)
    Port = sys.argv[2] # Port to listen on (non-privileged ports are > 1023)
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (Host,int(Port))
    print("starting up on "+ str(server_address)+ " on port "+ str(Port))
    sock.bind(server_address)
    sock.listen(1)
    while True:

        connection, client_address = sock.accept()
        try:
            print("connection from" +str(client_address))

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print("received request "+ str(data))
                if data:
                    cm = getCM()
                    print("ho calcolato "+ str(cm))
                    connection.sendall(str.encode(str(cm)))
                else:
                    print("no more data from "+ str(client_address))
                    break

        finally:
            # Clean up the connection
            connection.close()


setup()
StartListening()
