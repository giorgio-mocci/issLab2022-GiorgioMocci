import RPi.GPIO as GPIO
import time
import sys
import socket

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25,GPIO.OUT)





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

            stato = connection.recv(16)
            stato = stato.decode("utf-8")
            print("received request "+ str(stato))
            if stato == "ON":
                print ("LED on")
                GPIO.output(25,GPIO.HIGH)
            else :
                print ("LED off")
                GPIO.output(25,GPIO.LOW)



        finally:
            # Clean up the connection
            connection.close()



StartListening()
