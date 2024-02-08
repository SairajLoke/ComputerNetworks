# from scapy.all import send,sendp, IP, ICMP, Ether
# from scapy.all import *

# Test_ip = "127.0.0.1"

# #network levels
# # send(IP(src=Test_ip , dst=Test_ip)/TCP(dport=1234)/" ......oye.......  " )

# sendp(Ether(src='10:6f:d9:0d:36:25', dst='c8:94:02:81:e3:3b')/ICMP()/" ......maddy.......  " )



from scapy.all import Ether, ARP, Raw, sendp, wrpcap

def send_arp_packet(target_ip, target_mac, message):
    # Craft the ARP request packet with Raw layer to include the message
    arp_request = Ether(dst=target_mac)/ARP(pdst=target_ip, hwdst=target_mac, op='who-has')/Raw(load=message)
    print(arp_request)
    # packet=[arp_request]
    # packets = [packet]# Save the packets to a pcap file
    # wrpcap("custom_packets.pcap", packets)
    # Send the ARP request packet
    sendp(arp_request, verbose=1)

# Replace '10.203.1.45' with the target IP address, '10:6f:d9:0d:36:25' with the target MAC address,
# and 'Hello, Sai!' with your desired message
for i in range (1,1000):
    send_arp_packet('10.203.3.165', 'c8:94:02:81:e3:3b', 'Hello, Mad!')