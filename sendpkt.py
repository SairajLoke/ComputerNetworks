from scapy.all import send,sendp, IP, ICMP, Ether
from scapy.all import *

Test_ip = "127.0.0.1"

send(IP(src=Test_ip , dst=Test_ip)/TCP(dport=1234)/" ......oye.......  " )

# sendp(Ether(src='10:6f:d9:0d:36:2', dst='00:50:5d:1d:eb:73')/ICMP()/" ......maddy.......  " )

# c8:94:02:81:e3:3b mad
