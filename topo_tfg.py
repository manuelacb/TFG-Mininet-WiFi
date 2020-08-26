#!/usr/bin/python

'This example shows how to create wireless link between two APs'
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, mesh, ITSLink
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference


def topology():
    "Create a network."
    net = Mininet_wifi(controller=Controller, link=wmediumd,
                       wmediumd_mode=interference)

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:01', IP='10.0.0.1/8', position='10,80,0')
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:02', IP='10.0.0.2/8', position='20,80,0')
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:03', IP='10.0.0.3/8', position='30,80,0')
    ap1 = net.addAccessPoint('ap1', wlans=2, ssid='ssid1,,,', position='20,100,0')

    sta4 = net.addStation('sta4', wlans=3, mac='00:00:00:00:00:04', IP='10.0.0.4/8', position='50,80,0')
    sta5 = net.addStation('sta5', wlans=2, mac='00:00:00:00:00:05', IP='10.0.0.5/8', position='40,65,0')
    sta6 = net.addStation('sta6', wlans=2, mac='00:00:00:00:00:06', IP='10.0.0.6/8', position='50,50,0')
    sta7 = net.addStation('sta7', wlans=2, mac='00:00:00:00:00:07', IP='10.0.0.7/8', position='60,65,0')
    ap2 = net.addAccessPoint('ap2', wlans=2, ssid='ssid2,', position='50,90,0')

    sta8 = net.addStation('sta8', mac='00:00:00:00:00:08', IP='10.0.0.8/8', position='25,40,0')
    sta9 = net.addStation('sta9', wlans=3, mac='00:00:00:00:00:09', IP='10.0.0.9/8', position='35,40,0')
    sta10 = net.addStation('sta10', mac='00:00:00:00:00:10', IP='10.0.0.10/8', position='30,30,0')
    sta11 = net.addStation('sta11', mac='00:00:00:00:00:11', IP='10.0.0.11/8', position='40,30,0')
    ap3 = net.addAccessPoint('ap3', wlans=2, ssid='ssid3,', position='30,50,0')


    c0 = net.addController('c0')

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating Stations\n")
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    net.addLink(sta3, ap1)

    net.addLink(sta4, ap2)
    net.addLink(sta4, channel=10, cls=ITSLink)
    net.addLink(sta4, channel=25, cls=ITSLink)
    net.addLink(sta5, channel=10, cls=ITSLink)
    net.addLink(sta5, channel=15, cls=ITSLink)
    net.addLink(sta6, channel=15, cls=ITSLink)
    net.addLink(sta6, channel=20, cls=ITSLink)
    net.addLink(sta7, channel=20, cls=ITSLink)
    net.addLink(sta7, channel=25, cls=ITSLink)

    net.addLink(sta8, ap3)
    net.addLink(sta9, ap3)
    net.addLink(sta9, channel=30, cls=ITSLink)
    net.addLink(sta10, channel=30, cls=ITSLink)
    net.addLink(sta9, channel=35, cls=ITSLink)
    net.addLink(sta11, channel=35, cls=ITSLink)

    net.addLink(ap1, intf='ap1-wlan2', cls=mesh, ssid='mesh-ssid', channel=5)
    net.addLink(ap2, intf='ap2-wlan2', cls=mesh, ssid='mesh-ssid', channel=5)
    net.addLink(ap3, intf='ap3-wlan2', cls=mesh, ssid='mesh-ssid', channel=5)

    net.plotGraph(max_x=110, max_y=110)

    info("*** Starting network\n")
    net.build()
    c0.start()
    ap1.start([c0])
    ap2.start([c0])
    ap3.start([c0])

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
