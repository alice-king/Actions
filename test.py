from scapy.all import *
ans,unans=sr(IP(dst='3.3.3.3')/ICMP())
ans[0][1].show()