from scapy.all import * 
#Packet , StrField, bind_layers

'''
Has Custom packets for Transport layer 
using TCP 
'''


#constants
authSucc  = "Auth Successful"
authUnSucc = "Auth Unsuccessful"




class SP(Packet):
    name = "Name"
    fields_desc = [
        StrField("name", ""),
    ]

class AuthenticationPacket(Packet):
    
    topic = "AuthServ"
    n = "Alpha"
    p = "Beta"
    fields_desc = [
        # StrField("topic",topic),
        # StrField("sep","-"),
        StrField("n",""),
        StrField("sep","-"),
        StrField("p","")
    ]

class WithdrawPkt(Packet):
    
    topic = "Withdraw"
    amnt = 0
    fields_desc = [
        StrField("topic",topic),
        IntField("amnt",0)
    ]


class AuthenticationCheckPkt(Packet):
    status = "Auth Unsuccessful"
    fields_desc = [
        StrField("status",""),
    ]

class WithdrawCheckPkt(Packet):
    status = "Withdrawl Unsuccessful"
    fields_desc = [
        StrField("status",""),
    ]



class ATMBAlPkt(Packet):
    atm_bal = 1000
    topic = "BalServ"

    fields_desc = [
        StrField("atm_balance",""),
    ]

class ATMBAlPkt(Packet):
    atm_bal = 1000
    topic = "BalServ"

    fields_desc = [
        StrField("atm_balance",""),
    ]



class Bank_Server:

    def __init__(self, user_dict, bank_ip,bank_port):
        '''
        bank_ip = "127.0.0.1"
        bank_port = 1234
        '''
        self.user_dict = user_dict
        self.bank_ip = bank_ip
        self.bank_port = bank_port



    def check_authentication(self,username,passwd, atm_ip):

        statusPkt = AuthenticationCheckPkt()
        # print(user_dict[username].lower()) #check why lower() isnt working
        
        if(username in self.user_dict and self.user_dict[username]  == passwd):
            statusPkt.status = "Successful Authentification"
            print("checking authentication")

        pkt = IP(src=self.bank_ip ,dst=atm_ip)/ TCP(dport=self.bank_port)/ statusPkt
        # send(IP(src="127.0.0.1" , dst="127.0.0.1")/TCP(dport=1234)/authpkt)
        # send(apkt)
        wrpcap("status.pcap",pkt)


        


class ATM:
    def __init__(self, bank_ip, bank_port, atm_ip):
        '''
        atm_ip =  "127.0.0.1"
        bank_ip = "127.0.0.1"
        bank_port = 1234
        '''
        self.atm_ip = atm_ip
        self.bank_ip = bank_ip
        self.bank_port = bank_port

    def authenticate(self,username, passwd):
        print("\nTrying to authenticate....")
        authPkt = AuthenticationPacket()
        authPkt.n = username
        authPkt.p = passwd

        # apkt = IP(dst="127.0.0.1")/ TCP(dport=1234)/ SP()
        pkt = IP(src=self.atm_ip,dst=self.bank_ip)/ TCP(dport=self.bank_port)/ authPkt
        send(pkt)
        # print(pkt.n)

        wrpcap("atm.pcap",pkt)#add to a particular location
        print("sent authentication attempt")

    

            