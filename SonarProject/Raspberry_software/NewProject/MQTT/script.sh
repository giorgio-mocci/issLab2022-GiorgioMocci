#!/bin/sh
#usage ControllerMQTT, distanzaLimite, Indirizzo broker, indirizzo radar, porta radar
python ControllerMQTT.py 20 192.168.1.12 192.168.1.9 6666 &
sleep 0.1
#usage ledMQTT, indirizzo broker
python ledMQTT.py 192.168.1.12  &
sleep 0.1
#usage sonarMQTT indirizzo broker
python sonarMQTT.py 192.168.1.12
