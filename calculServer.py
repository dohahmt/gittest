from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print 'Server is Listening for incoming Client Requests!!!'
while True:
  connectionSocket, addr = serverSocket.accept()
  messagefromclient = connectionSocket.recv(1024)
  print 'Message from Client: ', messagefromclient
  messagefromclient = connectionSocket.recv(1024)
  print 'Message from Client: ', messagefromclient
  messagefromserver = str(int(messagefromclient)+int(messagefromclient)).encode()
  connectionSocket.send (messagefromserver)
  
  
  

