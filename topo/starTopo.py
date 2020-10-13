import time
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
import sys
from tests import *

def MyNetwork():

    net = Mininet( topo=None,
                   build=False,
		   link=TCLink,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    con1=net.addController(name='con1',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    c4 = net.addHost('c4', cls=Host, ip='10.0.0.4', defaultRoute=None, cpu=0.02)
    
    c3 = net.addHost('c3', cls=Host, ip='10.0.0.3', defaultRoute=None, cpu=0.02)
    c2 = net.addHost('c2', cls=Host, ip='10.0.0.2', defaultRoute=None, cpu=0.02)
    c1 = net.addHost('c1', cls=Host, ip='10.0.0.1', defaultRoute=None, cpu=0.02)
   
    serv1 = net.addHost('serv1', cls=Host, ip='10.0.0.5', defaultRoute=None)
    serv2 = net.addHost('serv2', cls=Host, ip='10.0.0.6', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(c3, s1, bw=1)
    net.addLink(c2, s1, bw=1)
    net.addLink(c1, s1, bw=1)
    net.addLink(c4, s1, bw=10)
    net.addLink(s1, serv1, bw=4)
    net.addLink(s1, serv2, bw=4)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([con1])

    info( '*** Post configure switches and hosts\n')

    net.pingAll()
    net.iperf()

    if len(sys.argv) >= 2:		
    	if sys.argv[1] == "base":
		testbase(net)
    	elif sys.argv[1] == "load":
		testload(net)
	elif sys.argv[1] == "bal":
		testloadbal(net)
   	else:
		print("Unregonised test")
    else:
	print("No test specified")
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    MyNetwork()

