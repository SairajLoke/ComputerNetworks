from scapy.all import * 
import psutil

from atm_bank_layermsgs import *

DIP = "10.203.3.114"

myATM  = ATM(bank_ip="127.0.0.1", bank_port=1234,atm_ip="127.0.0.1")


# pkt1 = IP(dst="127.0.0.1")/ TCP(dport=1234)/ SP(name="Alpha")
# pkt2 = IP(dst="127.0.0.1")/ TCP(dport=5678)/ SP(name="Beta")
# pkts = [pkt1,pkt2]
# wrpcap("custom_pkts.pcap",pkts)
def run_client():
    interval_slp = 1.5

    print("\nRrunning client")
    bind_layers(TCP,AuthenticationPacket) 

    myATM.authenticate(username="A",passwd="passA")

    # while(sniff ATM empty ): loop
    # myATM.query_atm_balance()
    # time.sleep(interval_slp)

    # myATM.query_user_balance()
    # time.sleep(interval_slp)

    # myATM.withdraw_amount(amount=100)
    # myATM.query_user_balance()

    # myATM.credit_amount(amount=100)
    # myATM.query_user_balance()


    
    # Bank_ATM.check_authentication(username="Alpha",passwd="Beta")




if __name__ == "__main__":
    
    for i in range(0,10):
        run_client()
        time.sleep(1)
    

    # Bank_ATM.query_atm_balance()
    # Bank_ATM.query_user_balance()
    # Bank_ATM.
    # sniff(filter= 'dst port 1234')

















