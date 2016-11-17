import IPScanner,os
from FTPServer import start_ftp_server as iniciaFTP
from HTTPServer import start_http_server as iniciaHTTP
from TelnetServer import start_telnet_server as iniciaTelnet
from PortScanner import scan_ports as escanea

def get_principal_menu():
    os.system("cls")
    print('''Herramienta de Análisis y Servicios en Red
-------------------------------------------------\n
    1) Iniciar servicios
    2) Escaneo sobre la red
    3) Salir
    ''')
    return int(input("intro> "))

def get_scanner_menu(IP):
    os.system("cls")
    print('''Menú de Operaciones sobre la red
-------------------------------------------------\n
IP actual: '''+IP+'''
    1) Escaneo de puertos abiertos de la IP actual
    2) Información de la IP actual
    3) Cambiar IP actual
    4) Regresar
    ''')
    return int(input("intro> "))

def get_services_menu():
    os.system("cls")
    print('''Menú de Servicios
-------------------------------------------------\n
Cuál de los siguientes servicios deseas iniciar:
    1) HTTP
    2) FTP
    3) Telnet
    4) Salir
    ''')
    return int(input("intro> "))

if __name__=='__main__':
    continuar = True
    while(continuar):
        try:
            flag = True
            while (flag):
                try:
                    opc = get_principal_menu()
                    flag = False
                except:
                    print("No es una opción válida, intenta de nuevo")
            if opc==1:
                while (True):
                    flag = True
                    actu = ""
                    while (flag):
                        try:
                            opt1 = get_services_menu()
                            flag = False
                        except:
                            print("No es una opción válida, intenta de nuevo")
                    if opt1 == 1:
                        actu = "HTTP"
                        try:
                            iniciaHTTP(IPScanner.getMyIpAddress(), 80,False)
                        except:
                            pass
                    elif opt1 == 2:
                        actu = "FTP"
                        iniciaFTP(IPScanner.getMyIpAddress(), 20)
                    elif opt1 == 3:
                        actu = "Telnet"
                        iniciaTelnet(IPScanner.getMyIpAddress(), 23)
                    elif opt1 == 4:
                        break;
                    else:
                        print("No es una opción válida, intenta de nuevo")
                    print("El servidor",actu,"ha sido apagado")
                    ins = input("Presiona <enter> para continuar")
            elif opc==2:
                global current
                try:
                    try:
                        print("Ya existe una IP de trabajo: ",current.ip)
                        print("1) Desea seguir usándola\n"
                              "2) Escanear la red de nuevo:")
                        tgr = int(input("intro>"))
                        if tgr==1:
                            pass
                        elif tgr==2:
                            current, list = IPScanner.__initial__()
                    except NameError:
                        print("No hay IP seleccionada\nSe producederá a elegir una")
                        current, list = IPScanner.__initial__()
                    while (True):
                        opt1 = get_scanner_menu(current.ip)
                        if opt1 == 1:
                            flag = True
                            while(flag):
                                try:
                                    bottom = int(input("Dame puerto inferior: "))
                                    up = int(input("Dame puerto superior: "))
                                    flag = False
                                    escanea(current.ip, bottom, up)
                                except:
                                    print("No es un valor de puertos válidos, intenta de nuevo")
                        elif opt1 == 2:
                            print("IP actual:     ", current.ip)
                            print("Dirección MAC: ", current.mac)
                            print("Nombre de red: ", current.name)
                            print("Clasificación: ", current.classification)
                            ins = input("Presiona <enter> para continuar")
                        elif opt1 == 3:
                            IPScanner.print_actives(list)
                            current = IPScanner.get_ip(list)
                        elif opt1 == 4:
                            break;
                        else:
                            print("No es una opción válida, intenta de nuevo")
                except KeyboardInterrupt:
                    print("\nSe ha cancelado la operación")
                    ins = input("Presiona <enter> para continuar")
            elif opc==3:
                break;
            else:
                print("No es una opción válida, intenta de nuevo")
        except:
            continuar = True
