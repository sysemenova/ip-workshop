#!/usr/bin/env python3

# Code for receiving packets

import socket

# The set up
# REPLACE THIS IP ADDRESS WITH YOUR LOCAL IP ADDRESS
# See send.py for help with commands
UDP_IP = "172.30.138.96"
UDP_PORT = 5005

# Sets up socket
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# Receives data and prints address + port and data
while True:
    data, addr = sock.recvfrom(1024) 
    print("address:", addr)
    print("received message: %s" % data)
