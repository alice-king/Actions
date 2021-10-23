from scapy.all import *
pkg=IP(dst='195.133.10.119',ttl=255)/ICMP(type=11)/IPerror(src='195.133.10.119',dst='3.3.3.3',ttl=1)/ICMPerror()
send(pkg)