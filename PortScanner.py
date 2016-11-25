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