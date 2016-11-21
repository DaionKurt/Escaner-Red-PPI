import socket,sys,re
from datetime import datetime


def scan_ports(remote_server,bottom,up):
    import socket;
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    puertos_abiertos = []
    t1 = datetime.now()
    try:
        for port in range(bottom, up):
            print("Estoy en el puerto: ", port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remote_server, port))
            if result == 0:
                puertos_abiertos.append(port)
            sock.close()
    except socket.error:
        print("No se pudo conectar")
    t2 = datetime.now()
    total = t2 - t1
    print("Escaneo completo en ", total)
    return puertos_abiertos,total
'''
def scan_ports(remote_server,bottom,up):
    print(remote_server)
    remote_server_ip = socket.gethostbyname(remote_server)
    print(remote_server_ip)
    t1 = datetime.now()
    puertos_abiertos = []
    try:
        for port in range(bottom,up):
            print("Estoy en el puerto: ",port)
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result = sock.connect_ex((remote_server_ip,port))
            if result == 0:
                puertos_abiertos.append(port)
                print("Port {}:     Open".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("Presionaste Ctrl+C")
        sys.exit()
    except socket.gaierror:
        print("Hostname no se pudo resolver")
        sys.exit()
    except socket.error:
        print("No se pudo conectar")
        sys.exit()
    t2 = datetime.now()
    total = t2 - t1
    print("Escaneo completo en ",total)
    return puertos_abiertos,total'''