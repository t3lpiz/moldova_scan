import netaddr
import socket

ip_list = netaddr.IPNetwork('5.56.64.0/18')

for x in ip_list:
    if 'host-static' in socket.gethostbyaddr(str(x))[0]:
        pass
    else:
        print(socket.gethostbyaddr(str(x)))
        with open('rezultat.txt', 'a') as f:
            f.write(socket.gethostbyaddr(str(a)))
            f.close()
