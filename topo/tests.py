import time

def testbase(net):
	serv1 = net.get("serv1")
	serv1.sendCmd("python ../server.py &")

	net.get("c4").sendCmd("python ../loadBalanceNode.py n &")

	print("--> Starting load with one client - for base performance")

	net.get("c3").cmd("python ../client.py local")

        time.sleep(4)
	
	net.get("c4").monitor()
	print("---> Done")
	return

def testload(net):
	serv1 = net.get("serv1")
	serv1.sendCmd('python ../server.py &')

	net.get("c4").sendCmd("python ../loadBalanceNode.py n &")

	print("--> Starting load with three client - for testing performance under extensive load")
	
	net.get("c1").sendCmd("python ../client.py c1-load &")
	net.get("c2").sendCmd("python ../client.py c2-load &")
	net.get("c3").sendCmd("python ../client.py c3-load")

	time.sleep(20)

	net.get("c1").monitor()
	net.get("c2").monitor()
	net.get("c3").monitor()
	net.get("c4").monitor()

    	print("---> Done")
	return

def testloadbal(net):
        serv1 = net.get("serv1")
	serv2 = net.get("serv2")
        serv1.sendCmd('python ../server.py &')
	serv2.sendCmd('python ../server.py &')

        net.get("c4").sendCmd("python ../loadBalanceNode.py bal &")

        print("--> Starting load balance and three client - for testing performance")

        net.get("c1").sendCmd("python ../client.py c1-bal &")
        net.get("c2").sendCmd("python ../client.py c2-bal &")
        net.get("c3").sendCmd("python ../client.py c3-bal")

        time.sleep(20)

        net.get("c1").monitor()
        net.get("c2").monitor()
        net.get("c3").monitor()
        net.get("c4").monitor()

        print("---> Done")
        return
