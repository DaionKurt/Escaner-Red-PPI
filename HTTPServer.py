import http.server

def start_http_server(bind,port,cgi):
    if cgi == True:
        try:
            http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler, port=port, bind=bind)
        except KeyboardInterrupt:
            print("Se ha cancelado el servidor HTTP")
            pass
    else:
        try:
            http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=port, bind=bind)
        except KeyboardInterrupt:
            print("Se ha cancelado el servidor HTTP")
            pass

def apaga_servidor():
    raise KeyboardInterrupt