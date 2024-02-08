from scapy.all import * 
from atm_bank_layermsgs import *

from collections import Counter


## Create a Packet Counter
packet_counts = Counter()
import binascii


user_dict = {"A": "passA"}


class Info:
    user = "U"
    pwd = "p"


def check_user(info):
    if info.user in user_dict and user_dict[info.user]== info.pwd:
        return 1
    else:
        return 0


# https://thepacketgeek.com/scapy/sniffing-custom-actions/part-1/

def custom_action(packet):
    # Create tuple of Src/Dst in sorted order
    key = tuple(sorted([packet[0][1].src, packet[0][1].dst]))
    packet_counts.update([key])
    # packet.show()

    msg = bytes(packet[TCP].payload).decode()

    info = {}
    
    i = 0
    while(msg[i] != '-' ):
        i += 1 

    info = Info()
    info.user = msg[:i]
    info.pwd = msg[i+1:]
            
    print(info.user, info.pwd)
    if check_user(info) == 1:
        print("\nValid User")
        # send()
    



    print(len(packet), len(packet[0]))



    return f"Packet #{sum(packet_counts.values())}: {packet[0][1].src} ==> {packet[0][1].dst}"


def onrecv_pkt(packet):
    print(packet.payload)

    # myBank.check_authentication(username=un,passwd=pw,atm_ip=myATM.ip)

    
myBank = Bank_Server(user_dict=user_dict, bank_ip="127.0.0.1",bank_port=1234)

def run_server():
    print("\nServer is sniffing")
    
    try:        
        sniff(iface="lo",filter = f"port {myBank.bank_port}", count=-1,prn= custom_action) #see if we can store u + p in same pkt
    except(KeyboardInterrupt):
        print("Server stopped by Keyboard interupt")
        pass


if __name__ == "__main__":
    run_server()