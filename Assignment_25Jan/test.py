from scapy.all import * 
#Packet , StrField, bind_layers


class SP(Packet):
    name = "Sai"
    fields_desc = [
        StrField("name", ""),
    ]


bind_layers(TCP,SP)



pkt1 = IP(dst="127.0.0.1")/ TCP(dport=1234)/ SP(name="Alpha")
pkt2 = IP(dst="127.0.0.1")/ TCP(dport=5678)/ SP(name="Beta")


pkts = [pkt1,pkt2]

wrpcap("custom_pkts.pcap",pkts)






















