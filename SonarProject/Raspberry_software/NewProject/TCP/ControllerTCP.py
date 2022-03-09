import RPi.GPIO as GPIO
import time

import sys
import socket

Dlimit = float(sys.argv[1])





def UpdateLed(Stato):
    # Create a TCP/IP socket
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    HostLed = sys.argv[4] # Standard loopback interface address (localhost)
    PortLed = sys.argv[5] # Port to listen on (non-privileged ports are > 1023)
    server_address = (HostLed, int(PortLed))
    print("connecting to "+ str(server_address))
    sock2.connect(server_address)
    try:



        # Send data
        if Stato == True :
            message = 'ON'
        else :
            message = 'OFF'
        print("Sto inviando la richiesta al LED")
        sock2.sendall(str.encode(message))


    finally:
        print("closing socket")
        sock2.close()


def sendDistanceToRadar(distance):
    # Create a TCP/IP socket
    sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    HostRadar = sys.argv[6] # Standard loopback interface address (localhost)
    PortRadar = sys.argv[7] # Port to listen on (non-privileged ports are > 1023)
    server_address = (HostRadar, int(PortRadar))
    print("connecting to "+ str(server_address))
    sock3.connect(server_address)
    try:
            # Send data
            message = str(distance) + "\n"

            print("Ora invio al radar "+ message + str(type(message)))
            sock3.sendall(str.encode(str(message)))


    finally:
        print("closing socket3")
        sock3.close()

def getCmFromSonar():
    statoLed = False
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    HostSonar = sys.argv[2] # Standard loopback interface address (localhost)
    PortSonar = sys.argv[3] # Port to listen on (non-privileged ports are > 1023)
    server_address = (HostSonar, int(PortSonar))
    print("connecting to "+ str(server_address))
    sock.connect(server_address)
    try:

        while True:

            # Send data
            message = 'Request CM'
        #    print("Sto inviando la richiesta al SONAR")
            sock.sendall(str.encode(message))
            # Look for the response
            cm = sock.recv(16)
            cm = float(cm.decode("utf-8"))
            print(str(cm))
            sendDistanceToRadar(cm)
            if cm < Dlimit and statoLed == False:
                UpdateLed(True)
                statoLed = True
                print("Accendo il led")
            elif cm >= Dlimit and statoLed == True:
                UpdateLed(False)
                statoLed = False
                print("Spengo il led")
            #time.sleep(0.1)

    finally:
        print("closing socket")
        sock.close()


getCmFromSonar()
