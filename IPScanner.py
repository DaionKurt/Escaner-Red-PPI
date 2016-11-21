import subprocess,ipaddress,re,socket,MACScanner

info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

class Net:
    def __init__(self,ip,mac,classification,name):
        self.ip = ip
        self.mac = mac
        self.classification = classification
        self.name = name
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, " destruido")
    def displayCount(self):
        print()

def getMyIpAddress():
    return socket.gethostbyname(socket.gethostname())

def getNetIpAddress(ip):
    split_ip = ip.split('.', 3)
    net_address = ""
    for e in range(len(split_ip) - 1):
        net_address += split_ip[e]
        net_address += '.'
    net_address += '0'
    net_address += '/'
    net_address += '24'
    return net_address

def get_ip_net():
    return ipaddress.ip_network(getNetIpAddress(getMyIpAddress()))

def get_all_hosts(hosts):
    return list(hosts)

def get_active_hosts(z,t):
    ip_net = get_ip_net()
    all_hosts = list(ip_net.hosts())
    actives = []
    n = 1
    for i in range(len(all_hosts)):
        output = subprocess.Popen(['ping', '-n', z, '-w', t, str(all_hosts[i])], stdout=subprocess.PIPE,startupinfo=info,).communicate()[0]
        IP = str(all_hosts[i])
        print("Escaneando actualmente a: ", IP)
        if "Respuesta desde " in output.decode('ISO-8859-1') and "TTL=" in output.decode('ISO-8859-1'):
            from subprocess import Popen, PIPE
            pid = Popen(["arp", "-n", IP], stdout=PIPE)
            s = pid.communicate()[0]
            comando = "arp -a " + IP
            resultado = subprocess.check_output(comando, shell=True)
            MAC_addr = str(resultado).replace('-', ':')
            p = re.compile(r'([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
            mac = re.findall(p, MAC_addr)
            nombre = socket.getfqdn(IP)
            n += 1
            if nombre.startswith("192.") and not nombre.endswith(".1") and not nombre.endswith(".254"):
                clasificaciones = "[Dispositivo móvil]"
            elif nombre.endswith(".254") or nombre.endswith(".1"):
                clasificaciones = "[Módem raiz]"
            else:
                clasificaciones = "[Laptop/Desktop]"
            if len(mac) <= 0:
                mac = MACScanner.get_MAC_addr()
            current = Net(IP, mac, clasificaciones, nombre)
            actives.append(current)
    return actives

def get_ip(activos):
    while True:
        numIp = int(input("Ingrese número de la IP a la cual realizar escaneo ")) - 1
        if numIp >= 0 and numIp < len(activos):
            return activos[numIp]
        else:
            print("Opción de IP no válida")


def begin():
    print("Tu estás conectado a una red\nRed detectada ubicada en: ", get_ip_net())
    print("1. Escaneo rápido")
    print("2. Escaneo normal")
    print("3. Escaneo profundo")
    print("4. Cancelar")
    rigth = True
    while (rigth):
        rigth = False
        opc = int(input("Selecciona tipo de escaneo: "))
        if opc == 1:
            z = '1'
            t = '50'
        elif opc == 2:
            z = '2'
            t = '50'
        elif opc == 3:
            z = '3'
            t = '200'
        elif opc == 4:
            raise KeyboardInterrupt
        else:
            rigth = True
    return z,t

def print_actives(actives):
    print("Conexiones activas en esta red:")
    for i in range(len(actives)):
        print(i+1,end=") ")
        print(actives[i].ip,end=" | ")
        print(actives[i].mac,end=" | ")
        print(actives[i].classification,end=" | ")
        print(actives[i].name)

def __initial__():
    z,t = begin()
    actives = get_active_hosts(z,t)
    print_actives(actives)
    active_net = get_ip(actives)
    print("IP de trabajo: ",active_net.ip)
    return active_net,actives

def __initial__q(actives):
    print_actives(actives)
    active_net = get_ip(actives)
    print("IP de trabajo: ",active_net.ip)
    return active_net,actives