# UDPClient.py

from socket import *
import sys

args = sys.argv
if len(args) != 3:
    print ("Usage: python3 UDPClient.py hostname port")
    exit()
hostname = args[1]
port = int(args[2])

# Create client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get input from user
clientSentence = input('Client ready for input\n')

# Send to server
clientSocket.sendto(clientSentence.encode(), (hostname, port))
print ('TO SERVER:', clientSentence)

# Receive from server
serverSentence, serverAddress = clientSocket.recvfrom(2048)
serverSentence = serverSentence.decode()
print ('FROM SERVER:', serverSentence)

# close the socket
clientSocket.close()
