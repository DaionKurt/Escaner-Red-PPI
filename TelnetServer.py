import socket,sys

BUFFER_SIZE = 10

s = None

def start_telnet_server(host,port):
    global s
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.bind((host,port))
        except socket.error as error:
            print(error[0]," : ",error[1])
            sys.exit()
        s.listen(1)
        print("Se ha iniciado el servidor Telnet en el puerto 23")
        conn,addr = s.accept()
        print("Conectado con: ",addr[0],":",str(addr[1]))
        var = "Se ha conectado al servidor echo via Telnet en el puerto 23\r\n"
        conn.sendall(var.encode())
        var = ""
        while True:
            try:
                data = conn.recv(BUFFER_SIZE)
                mark = data.decode().find('\n')
                if not data: break
                var+=data.decode()
                if mark == 1:
                    print("Servidor recibio: ", var,end="")
                    var ="Servidor recibio: " + var
                    conn.sendall(var.encode())
                    var = ""
            except UnicodeDecodeError:
                pass
    except KeyboardInterrupt:
        print("Conexión cerrada")
        s.close()
    except WindowsError:
        print("DA")

def apaga_servidor():
    global s
    s.close()
