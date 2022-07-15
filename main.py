from scapy import layers, sessions
from scapy.all import *
from scapy.layers.http import *

# sniffs packets on port 80 with a timeout of 10 seconds. 
p = sniff(filter="port 80", timeout=10)

# loops through the packets in p and displays them if they have the HTTPRequest layer and only shows that layer.
for packet in p:
    if packet.haslayer(HTTPRequest):
        layer = packet.getlayer(HTTPRequest)
        print(layer.show())