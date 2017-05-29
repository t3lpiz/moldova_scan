import netaddr
import socket

ip_list = netaddr.IPNetwork('5.56.64.0/18')

for x in ip_list:
    if 'host-static' in socket.gethostbyaddr(str(x))[0]:
        pass
    else:
        try:
            print(socket.gethostbyaddr(str(x)))
            #print(type(socket.gethostbyaddr(str(x))[0]))
            #print(type(socket.gethostbyaddr(str(x))[2][0]))
            with open('rezultat.txt', 'a') as f:
                f.write("IP: %s nume server: %s" %(socket.gethostbyaddr(str(x))[2][0],
                socket.gethostbyaddr(str(x))[0]))
                f.write('\n')
                f.close()
        except Exception as e:
            print(e)
            pass
