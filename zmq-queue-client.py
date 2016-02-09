import zmq
import sys
import random

port = "5559"
context = zmq.Context()
print "connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" & port)
client_id = random.randrange(1,10005)

#make 10 requests and wait for response on each

for request in range(1,10):
	print "Sending request ", request, "..."
	socket.send("Client %s sending request", % client_id)
	#on reply
	message = socket.recv()
	print "Received reply", request, "[", message,"]"