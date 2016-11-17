import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_ftp_server(ip,port):
    authorizer = DummyAuthorizer()
    user = "master"
    passw = "pass"
    print("Servidor FTP iniciado con usuario/clave: master/pass")
    authorizer.add_user(user,passw,os.getcwd(),perm='elradmwM')
    authorizer.add_anonymous(os.getcwd())
    handler = FTPHandler
    handler.authorizer = authorizer
    direccion = (ip,port)
    global servidor
    servidor = FTPServer(direccion,handler)
    servidor.max_cons = 256
    servidor.max_cons_per_ip = 5
    try:
        servidor.serve_forever(timeout=1)
    except KeyboardInterrupt:
        servidor.close_all()
        print("Se ha cancelado el servidor FTP")
        ins = input("Presiona <enter> para continuar")

def apaga_servidor():
    servidor.close_all()
