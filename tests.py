import time

def testbase(net):
	serv1 = net.get("serv1")
	serv1.sendCmd("python ./server.py 1 &")

	print("--> Starting load with one client - for base performance")

	net.get("c4").cmd("python ./client.py local")

	print("---> Done")
	return

def testload(net):
	serv1 = net.get("serv1")
	serv1.sendCmd('python ./server.py 1 &')
        
	print("--> Starting load with three client - for testing performance under extensive load")
	
	net.get("c1").sendCmd("python ./client.py c1 &")
	net.get("c2").sendCmd("python ./client.py c2 &")
	net.get("c3").cmd("python ./client.py c3")

	time.sleep(10)

	net.get("c1").monitor()
	net.get("c2").monitor()

    	print("---> Done")
	return
