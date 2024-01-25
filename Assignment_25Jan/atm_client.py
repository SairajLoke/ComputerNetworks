from scapy.all import * 
import psutil
#Packet , StrField, bind_layers

DIP = "10.203.3.114"
Test_sip = "127.0.0.1"
Test_dip = "127.0.0.1"


user_dict = {"Alpha": "Beta"}

class SP(Packet):
    name = "Name"
    fields_desc = [
        StrField("name", ""),
    ]

class AuthenticationPacket(Packet):
    
    n = "Alpha"
    p = "Beta"
    fields_desc = [
        StrField("n",""),
        # StrField("n",""),
        StrField("p","")
    ]

class AuthenticationCheckPkt(Packet):
    
    status = "Auth Unsuccessful"
    fields_desc = [
        StrField("status",""),
    ]

class ATMBAlPkt(Packet):
    atm_bal = 1000

    fields_desc = [
        StrField("atm_balance",""),
    ]

class Transactions:
    def authenticate(self,username, passwd):
        print("trying authenticate")
        authPkt = AuthenticationPacket()
        authPkt.n = username
        authPkt.p = passwd

        # apkt = IP(dst="127.0.0.1")/ TCP(dport=1234)/ SP()
        pkt = IP(src=Test_sip,dst=Test_dip)/ TCP(dport=1234)/ authPkt
        send(pkt)

        wrpcap("atm.pcap",pkt)#add to a particular location
        print("done authentication attempt")

    def check_authentication(self,username,passwd):

        statusPkt = AuthenticationCheckPkt()
        # print(user_dict[username].lower()) #check why lower() isnt working
        
        if(username in user_dict and user_dict[username].lower()  ==passwd):
            statusPkt.status = "Successful Authentification"
            print("here")

        pkt = IP(src="127.0.0.1",dst="127.0.0.1")/ TCP(dport=1234)/ statusPkt
        # send(IP(src="127.0.0.1" , dst="127.0.0.1")/TCP(dport=1234)/authpkt)
        # send(apkt)
        wrpcap("status.pcap",pkt)

            
# pkt1 = IP(dst="127.0.0.1")/ TCP(dport=1234)/ SP(name="Alpha")
# pkt2 = IP(dst="127.0.0.1")/ TCP(dport=5678)/ SP(name="Beta")
# pkts = [pkt1,pkt2]
# wrpcap("custom_pkts.pcap",pkts)
def run_client():
    print("running client")
    bind_layers(TCP,AuthenticationPacket) 


    Bank_ATM = Transactions() 
    Bank_ATM.authenticate(username="ALpha",passwd="Pi")
    # Bank_ATM.check_authentication(username="Alpha",passwd="Beta")




if __name__ == "__main__":

    for i in range(0,10):
        run_client()
        time.sleep(1)
    

    # Bank_ATM.query_atm_balance()
    # Bank_ATM.query_user_balance()
    # Bank_ATM.
    # sniff(filter= 'dst port 1234')

















