import socket

salir = 0

msgFromClient       = "Hello UDP Server"


serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket
while(salir == 0):
    messageFromClient = input(":")
    if(messageFromClient == "exit"):
        salir = 1
    bytesToSend         = str.encode(messageFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
 

# msg = "Message from Server {}".format(msgFromServer[0])

# print(msg)