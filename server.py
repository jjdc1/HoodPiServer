import socket
HOST, PORT = '', 2000
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT

while(True):
  client_connection, client_address = listen_socket.accept()
  http_response = """\
HTTP/1.1 200 OK

"""+"Success"
  client_connection.sendall(http_response)
  client_connection.close()
