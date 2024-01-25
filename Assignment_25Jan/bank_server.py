from scapy.all import * 

user_dict = {"ALpha": "Gamma"}

# https://thepacketgeek.com/scapy/sniffing-custom-actions/part-1/
def check_authentication(self,username,passwd):

        statusPkt = AuthenticationCheckPkt()
        # print(user_dict[username].lower()) #check why lower() isnt working
        
        if(username in user_dict and user_dict[username].lower()  ==passwd):
            statusPkt.status = "Successful Authentification"
            print("here")

        # pkt = IP(src="127.0.0.1",dst="127.0.0.1")/ TCP(dport=1234)/ statusPkt
        # send(IP(src="127.0.0.1" , dst="127.0.0.1")/TCP(dport=1234)/authpkt)
        # send(apkt)
        wrpcap("status.pcap",pkt)

# 
def call_bck(packet):
    print(packet.payload)
    
     
def run_server():
    print("server is sniffing")
    try:
        
        sniff(iface="lo",filter = "port 1234", count=1,prn= call_bck) #prn
        # print("Printp)
    except(KeyboardInterrupt):
        pass


if __name__ == "__main__":
    
    # for i in range(0,10):
    run_server()