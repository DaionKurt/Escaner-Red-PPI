import sys,os

def get_MAC_addr():
    if sys.platform == 'win32':
        for command in os.popen("ipconfig /all"):
            if command.lstrip().startswith("Direcci"):
                MAC_addr = command.split(':')[1].strip().replace('-',':')
                break
    else:
        for command in os.popen("/sbin/ifconfig"):
            if command.find('Ether') > -1:
                MAC_addr = command.split()[4]
                break
    return MAC_addr