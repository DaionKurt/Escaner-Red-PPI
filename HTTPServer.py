import http.server
import socketserver
httpd = None

def start_http_server(bind,port,cgi):
    global httpd
    if cgi == True:
        try:
            handler = http.server.CGIHTTPRequestHandler
            httpd = socketserver.TCPServer((bind, port),handler)
            httpd.serve_forever()
        except:
            print("Se ha cancelado el servidor HTTP")
            pass
    else:
        try:
            handler = http.server.SimpleHTTPRequestHandler
            httpd = socketserver.TCPServer((bind,port),handler)
            httpd.serve_forever()
            #server = http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=port, bind=bind)
        except:
            print("Se ha cancelado el servidor HTTP")
            pass

def apaga_servidor():
    try:
        global httpd
        httpd.server_close()
    except:
        print("")
