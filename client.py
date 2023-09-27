#!/usr/bin/env python3
import socket

BYTES_TO_READ = 4096

def get(host,port):
    request = b"GET /HTTP1.1\nHost: " + host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket initialize
    s.connect((host,port)) #connect to google
    s.send(request) #request google homepage
    s.shutdown(socket.SHUT_WR) #I'm done sending the request
    result = s.recv(BYTES_TO_READ) # Continuously receiving the response
    while (len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)

    s.close() # We need to close the socket

# get("www.google.com", 80)
get("localhost", 8080)
 
