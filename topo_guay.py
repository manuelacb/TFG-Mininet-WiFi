#!/usr/bin/python

'This example shows how to create wireless link between two APs'

import sys

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, mesh, ITSLink
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import OVSBridgeAP
from mn_wifi.wmediumdConnector import interference


def topology(stp):
    "Create a network."
    net = Mininet_wifi(controller=Controller, link=wmediumd,
                       wmediumd_mode=interference)

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:01', IP='10.0.0.1/8',
                          position='10,80,0', range=50)
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:02', IP='10.0.0.2/8',
                          position='20,80,0', range=50)
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:03', IP='10.0.0.3/8',
                          position='30,80,0', range=50)
    sta4 = net.addStation('sta4', mac='00:00:00:00:00:04', ip='10.0.0.4/8',
                          position='100,101,0')
    sta5 = net.addStation('sta5', mac='00:00:00:00:00:05', ip='10.0.0.5/8',
                          position='50,101,0')
    sta6 = net.addStation('sta6', mac='00:00:00:00:00:06', ip='10.0.0.6/8',
                          position='50,51,0')
    sta7 = net.addStation('sta7', mac='00:00:00:00:00:07', ip='10.0.0.7/8',
                          position='100,51,0')
    # sta8 = net.addStation('sta8', mac='00:00:00:00:00:08', IP='10.0.0.8/8',
    #                       position='20,30,0', channel='1')
    # sta9 = net.addStation('sta9', mac='00:00:00:00:00:09', IP='10.0.0.9/8',
    #                       position='50,20,0', channel='1')
    # sta10 = net.addStation('sta10', mac='00:00:00:00:00:10', IP='10.0.0.10/8',
    #                       position='30,5,0', channel='1')
    # sta11 = net.addStation('sta11', mac='00:00:00:00:00:11', IP='10.0.0.11/8',
    #                       position='70,5,0', channel='1')
    if stp:
        ap4 = net.addAccessPoint('ap4', ssid='new-ssid4', mode='g', channel='1',
                                 failMode="standalone", position='100,100,0',
                                 stp=True)
        ap5 = net.addAccessPoint('ap5', ssid='new-ssid5', mode='g', channel='1',
                                 failMode="standalone", position='50,100,0',
                                 stp=True)
        ap6 = net.addAccessPoint('ap6', ssid='new-ssid6', mode='g', channel='1',
                                 failMode="standalone", position='50,50,0',
                                 stp=True)
        ap7 = net.addAccessPoint('ap7', ssid='new-ssid7', mode='g', channel='1',
                                 failMode="standalone", position='100,50,0',
                                 stp=True)
        # ap8 = net.addAccessPoint('ap8', ssid='new-ssid8', mode='g', channel='1',
        #                          failMode="standalone", position='25,40,0',
        #                          stp=True)
        # ap9 = net.addAccessPoint('ap9', ssid='new-ssid9', mode='g', channel='1',
        #                          failMode="standalone", position='35,40,0',
        #                          stp=True)
        # ap10 = net.addAccessPoint('ap10', ssid='new-ssid10', mode='g', channel='1',
        #                          failMode="standalone", position='30,30,0',
        #                          stp=True)
        # ap11 = net.addAccessPoint('ap11', ssid='new-ssid11', mode='g', channel='1',
        #                          failMode="standalone", position='40,30,0',
        #                          stp=True)
    else:
        ap4 = net.addAccessPoint('ap4', ssid='new-ssid4', mode='g', channel='1',
                                 failMode="standalone", position='100,100,0')
        ap5 = net.addAccessPoint('ap5', ssid='new-ssid5', mode='g', channel='1',
                                 failMode="standalone", position='50,100,0')
        ap6 = net.addAccessPoint('ap6', ssid='new-ssid6', mode='g', channel='1',
                                 failMode="standalone", position='50,50,0')
        ap7 = net.addAccessPoint('ap7', ssid='new-ssid7', mode='g', channel='1',
                                 failMode="standalone", position='100,50,0')
    # ap8 = net.addAccessPoint('ap8', ssid='new-ssid8', channel='1', position='20,30,0')
    # ap9 = net.addAccessPoint('ap9', ssid='new-ssid9', channel='1', position='50,20,0')
    # ap10 = net.addAccessPoint('ap10', ssid='new-ssid10', channel='1', position='30,5,0')
    # ap11 = net.addAccessPoint('ap11', ssid='new-ssid11', channel='1', position='70,5,0')

    sta8 = net.addStation('sta8', mac='00:00:00:00:00:08', IP='10.0.0.8/8', position='40,60,0')
    # ap8 = net.addAccessPoint('ap8', wlans=2, ssid='ssid8,', mode='g', failMode="standalone", position='25,40,0')
    sta9 = net.addStation('sta9', mac='00:00:00:00:00:09', IP='10.0.0.9/8', position='35,40,0')
    ap9 = net.addAccessPoint('ap9', wlans=4, ssid='ssid9,,,', mode='g', failMode="standalone", position='30,40,0', stp=True)
    sta10 = net.addStation('sta10', mac='00:00:00:00:00:10', IP='10.0.0.10/8', position='30,30,0')
    ap10 = net.addAccessPoint('ap10', wlans=2, ssid='ssid10,', mode='g', failMode="standalone", position='30,35,0', stp=True)
    sta11 = net.addStation('sta11', mac='00:00:00:00:00:11', IP='10.0.0.11/8', position='40,30,0')
    # ap11 = net.addAccessPoint('ap11', wlans=2, ssid='ssid11,', mode='g', failMode="standalone", position='40,30,0', stp=True)

    ap1 = net.addAccessPoint('ap1', wlans=3, ssid='ssid1,,', position='20,100,0', channel='1')
    ap2 = net.addAccessPoint('ap2', wlans=3, ssid='ssid2,,', position='40,100,0', channel='1')
    ap3 = net.addAccessPoint('ap3', wlans=3, ssid='ssid3,,', position='40,80,0', channel='1')



    c0 = net.addController('c0')

    net.setPropagationModel(model="logDistance", exp=5)


    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating Stations\n")
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    net.addLink(sta3, ap1)

    net.addLink(ap4, sta4)
    net.addLink(ap5, sta5)
    net.addLink(ap6, sta6)
    net.addLink(ap7, sta7)

    net.addLink(ap3, sta8)
    net.addLink(ap9, sta9)
    net.addLink(ap10, sta10)
    net.addLink(ap9, sta11)

    net.addLink(ap4, ap5)
    net.addLink(ap5, ap6)
    net.addLink(ap6, ap7)
    net.addLink(ap7, ap4)
    net.addLink(ap2, ap4)

    net.addLink(ap9, ap10)
    # net.addLink(ap9, ap11)
    # net.addLink(ap3, ap8)
    net.addLink(ap3, ap9)

    net.addLink(ap1, intf='ap1-wlan3', cls=mesh, ssid='mesh-ssid', channel='5')
    net.addLink(ap2, intf='ap2-wlan3', cls=mesh, ssid='mesh-ssid', channel='5')
    net.addLink(ap3, intf='ap3-wlan3', cls=mesh, ssid='mesh-ssid', channel='5')

    net.plotGraph(max_x=150, max_y=150)


    info("*** Starting network\n")
    net.build()
    c0.start()
    ap1.start([c0])
    ap2.start([c0])
    ap3.start([c0])
    ap4.start([c0])
    ap5.start([c0])
    ap6.start([c0])
    ap7.start([c0])
    # ap8.start([c0])
    ap9.start([c0])
    ap10.start([c0])
    # ap11.start([c0])


    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    stp = True if '-s' in sys.argv else False
    topology(stp)
