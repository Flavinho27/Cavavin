import http.server

PORT = 80
server_address = ("", PORT)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

print("Serveur actif sur le port :", PORT)
print("http://localhost:80/index.py")

httpd = server(server_address, handler)
httpd.serve_forever()
