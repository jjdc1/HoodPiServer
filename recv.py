import socket
import json

HOST, PORT = '', 2002
j=''
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
  client_connection, client_address = listen_socket.accept()
  request = client_connection.recv(1024)
  i=1;
  requestString=''
  while request[-i] != '\n':
    requestString=requestString+ request[-i]
    i=i+1
  requestString=requestString[::-1]
  requestJson=json.loads(requestString)
  print requestJson["rel1"]+"\t"+requestJson["rel2"]+"\t"+requestJson["rel3"]+"\t"+requestJson["rel4"]
  http_response = """\
HTTP/1.1 200 OK

"""+requestString
  client_connection.sendall(http_response)
  client_connection.close()
