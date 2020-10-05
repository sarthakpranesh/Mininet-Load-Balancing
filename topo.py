import time
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf

def MyNetwork():

    net = Mininet( topo=None,
                   build=False,
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
    c3 = net.addHost('c3', cls=Host, ip='10.0.0.3', defaultRoute=None, cpu=0.04)
    c2 = net.addHost('c2', cls=Host, ip='10.0.0.2', defaultRoute=None, cpu=0.03)
    c1 = net.addHost('c1', cls=Host, ip='10.0.0.1', defaultRoute=None, cpu=0.02)
   
    serv1 = net.addHost('serv1', cls=Host, ip='10.0.0.5', defaultRoute=None)
    serv2 = net.addHost('serv2', cls=Host, ip='10.0.0.6', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(c3, s1, params1={'bw': 10}, params2={'bw': 10})
    net.addLink(c2, s1, params1={'bw': 10}, params2={'bw': 10})
    net.addLink(c1, s1, params1={'bw': 10}, params2={'bw': 10})
    net.addLink(c4, s1, params1={'bw': 10}, params2={'bw': 10})
    net.addLink(s1, serv1)
    net.addLink(s1, serv2)

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
    TestNetwork(net)
    net.stop()

def TestNetwork(net):
    print("Ping All")
    net.pingAll()
    
    print("Network Performance (iPerf)")
    net.iperf()

    print("Controllers attached to switch")
    s1 = net.get("s1")
    print(s1.controllerUUIDs())

    print("Custom Load Testing Network")
    serv1 = net.get("serv1")
    serv2 = net.get("serv2")

    print("--> Starting Test Servers")
    serv1.sendCmd('python ./server.py &')
    serv2.sendCmd('python ./server.py &')

    print("--> Starting client scripts in client hosts in Parallel processes")
    net.get("c1").sendCmd("python ./client.py c1 &")
    net.get("c2").sendCmd("python ./client.py c2 &")
    net.get("c3").cmd("python ./client.py c3 &")

    time.sleep(10)

    net.get("c1").monitor()
    net.get("c2").monitor()
    #net.get("c3").monitor()
    print("Testing Network Complete")


if __name__ == '__main__':
    setLogLevel( 'info' )
    MyNetwork()

