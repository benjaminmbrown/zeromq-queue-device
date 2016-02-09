import zmq

def main():

	try:
		context = zmq.Context(1)
		#sockets that face clients
		frontend = context.socket(zmq.XREP) #XREP = response deivce
		frontend.bind("tcp://*:5559")

		#sockets that face services
		backend = context.socket(zmq.XREQ)
		backend.bind("tcp://*:5560")

		zmq.device(zmq.QUEUE, frontend, backend)
	except Exception, e:
		print e
		print "destroying zmq queue device"
	finally:
		pass
		frontend.close()
		backend.close()
		context.term()

if __name__ == "__main__":
	main()