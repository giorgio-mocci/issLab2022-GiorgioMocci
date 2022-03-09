#!/bin/sh
#usage led, host, port
python ledTCP.py localhost 6661 &
sleep 0.1
#usage sonarhost, port
python sonarTCP.py localhost 6660 &
sleep 0.1
#usage Controller Dlimit hostSonar, portSonar hostLed portLed hostSonar portSonar
python ControllerTCP.py 20 localhost 6660 localhost 6661 192.168.1.9 6666




