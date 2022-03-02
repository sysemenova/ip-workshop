#!/usr/bin/env python3

# Code to send a packet!

import socket
import sys

# REPLACE THIS WITH YOUR LOCAL IP ADDRESS
# On Linux and Mac, running hostname -I will give your IP quickly.
# On Windows, ifconfig should do the trick.
UDP_IP = "172.30.138.96"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"

# If we enter an argument, change message
if (len(sys.argv) >= 2):
    MESSAGE = bytes(sys.argv[1], 'ascii')

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

# Creates socket, and sends
sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
