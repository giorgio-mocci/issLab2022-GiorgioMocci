import CoapParser
import random
import serial


def setupXbeeConnection():
    try:
        port = int(raw_input("Please enter the serial port number for Xbee: ").strip())
    except ValueError:
        print("Please check your input port. It needs to be an integer.")
        exit(1)
    try:
        baudrate = int(raw_input("Please enter the baudrate number of Xbee: ").strip())
    except ValueError:
        print("Please check your input integer baudrate.")
        exit(1)
    try:
        mySerial = serial.Serial(port='COM' + str(port), baudrate=baudrate, timeout=1)
    except:
        print "Please check your comport for xbee. It cannot open the input comport: " + str(port)
        exit(1)
    return mySerial


def obtainRequestedMessageObject():
    example = raw_input(
        "Do you want an auto-generated example <Press Y> or build your own <Press ANYKEY other than Y>: ").strip().upper()
    if example == 'Y':
        print "method: POST, uri: example, payload: hello world, token: test"
        method = "POST"
        uri = "example"
        payload = "hello world"
        token = "test"
    else:
        method = raw_input("Please enter the COAP method (GET, POST, PUT, DELETE): ").strip().upper()
        if method not in ["GET", "POST", "PUT", "DELETE"]:
            print("Please check your method input. It needs to be GET, POST, PUT or DELETE")
            exit(1)
        uri = None
        while uri == None or uri == "":
            uri = raw_input("Please enter the uri end path: ").strip()
            if uri == None or uri == "":
                print "URI cannot be None or empty"
        payload = None
        if (method == "PUT" or method == "POST"):
            while payload == None or payload == "":
                payload = raw_input("Please enter the payload content. And it cannot be empty: ")
        token = raw_input("Please enter the token: ")
    maxMsgID = 2 ** 16 - 1
    msgObj = CoapParser.construct_message(method, uri, random.randint(0, maxMsgID), token, payload)  # construct the
    # message object
    return msgObj


def main():
    mySerial = setupXbeeConnection()
    msgObj = obtainRequestedMessageObject()
    if not msgObj or type(msgObj) == int:
        print "Bad method"
        exit(1)
    outMsg = CoapParser.msgobject_to_string(msgObj)  # parse the object to a string format to send out
    print "\n##############################################\n"
    print "This is the send out message:"
    print CoapParser.msgstring_to_formatted_output(outMsg)
    responseObj = CoapParser.receive_result(mySerial, outMsg, msgObj)
    if type(responseObj) == int or type(responseObj) == None:
        print "The response is invalid. There may be a few reasons:\n1. Wrong baud rate.\n2. You are sending to a " \
              "server does not support COAP\n3. The target server does not understand your message\n4. Unexpected " \
              "data in response"
        exit(1)
    print "This is the received message"
    print CoapParser.interpret_msgobject(responseObj)
    exit(0)

if __name__ == "__main__":
    main()
