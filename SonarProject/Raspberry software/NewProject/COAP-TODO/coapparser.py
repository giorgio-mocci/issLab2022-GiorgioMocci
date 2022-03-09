from coapthon.serializer import Serializer
from coapthon.messages.message import Message
from coapthon.messages.option import Option
import time
import serial


class ErrorAtParsing(Exception):
    pass


def construct_message(method, path, msgid, token = None, payload = None):
    # method to construct the message based on the input field.
    # It feeds the input parameters into a warper message class
    msg = Message()
    msg.type = 0
    msg.mid = msgid
    msg.token = token
    msg.payload = payload
    o = Option()
    o.value = bytearray(path)
    o.number = 11
    msg.add_option(o)
    msg.destination = (None, None) # This field needs to be present
    if method == "GET":
        msg.code = 1
    elif method == "POST":
        msg.code = 2
    elif method == "PUT":
        msg.code = 3
    elif method == "DELETE":
        msg.code = 4
    else:
        return None
    msg.version = 1
    return msg


def read_serial(ser):  # method to handle reading on serial. It will read until a complete message is received.
    resp = []
    timeout = 3
    start = time.time()
    end = time.time()
    while end - start < timeout:
        seg = ser.read()
        if seg != "":
            start = time.time()
            resp.append(seg)
        end = time.time()
    return "".join(resp)


def msgobject_to_string(msgObj): # parse msgObj to actual string msg
    serializer = Serializer()
    msg = serializer.serialize(msgObj)
    return msg


def msgstring_to_formatted_output(msg):  # format msg string to structured output, which breaks down the message body
    serializer = Serializer()
    return serializer.deserialize(msg, (None, None)).pretty_print()


def interpret_msgobject(msgObj):  # interpret the message object to structured output
    return msgObj.pretty_print()


def receive_result(ser, msg, msgObj):  # method to handle receiving result
    # this method also does token and id checking to find the correct the response
    serializer = Serializer()
    gap = 1
    while 1:  # it will perform resend if the received message is undesired
        ser.write(msg)
        data = read_serial(ser)
        responseObj = serializer.deserialize(data, (None, None))
        try:
            if msgObj.token == responseObj.token and msgObj.mid == responseObj.mid:  # validate token match
                break
        except:
            print "Message intepretation failure. Re-attempt."
        time.sleep(gap)
        gap *= 2
        if gap == 16:
            break
    return responseObj

