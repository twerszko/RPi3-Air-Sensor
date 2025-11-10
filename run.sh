#!/bin/bash

sudo pip3 install py-sds011 urlopen

> /home/pi/air_sensor.log
python3 -u air_sensor.py 2>&1 | ts '[%Y-%m-%d %H:%M:%S]' >> /home/pi/air_sensor.log
