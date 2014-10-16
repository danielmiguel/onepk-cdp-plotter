#!/usr/bin/python


import logging
from onep.element import NetworkElement
from onep.element import NetworkApplication
from onep.element import SessionConfig
from onep.element import SessionHandle
from onep.element import SessionStatistics
from onep.element import SessionProperty
from onep.core.exception import OnepException
from onep.core.util import tlspinning

from onep.topology import TopologyListener
from onep.topology import TopologyEvent
from onep.topology import TopologyClass
from onep.topology import TopologyFilter
from onep.topology import Edge

import matplotlib.pyplot as plt
from networkx import nx

nodes = {'router1': { 'ip': '10.10.10.110'}, 'router2': { 'ip': '10.10.10.120'}, \
	'router3': {'ip': '10.10.10.130'}}

class Create_Ne:
    def __init__(self,name,ca,ip):
        self.app_name = name
        self.ca_path = ca
        self.ip = ip
    def config(self):
        session_config = SessionConfig(SessionConfig.SessionTransportMode.TLS)
        session_config.ca_certs = self.ca_path
        return session_config
    def get_ne(self):
        network_application = NetworkApplication.get_instance()
        network_application.name = self.app_name
        network_element = network_application.get_network_element(self.ip)
        return network_element

def get_data(dict ,username='evelio',password='vila',transport='tls'\
            ,root_cert_path = 'ca.pem',aplicationName='cdp-plotter'):
    ''' return remote hosts '''

    for key,values in dict.items():
        # creating network element
        cdp_plotter = Create_Ne(aplicationName,root_cert_path,values['ip'])
                
        ne = cdp_plotter.get_ne()
        session_config = cdp_plotter.config()
                
        session_handle = ne.connect(username, password, session_config)
        
        if session_handle:    
            topology = TopologyClass(ne, TopologyClass.TopologyType.CDP)
            graph = topology.get_graph()

            yield {key:  graph.get_edge_list(Edge.EdgeType.UNDIRECTED) }
            

        else:
            print "Unable to connect to network element {} .".format(values['ip'])
            continue

        if ne.is_connected():
            try:
                ne.disconnect()
            except:
                print 'Unable to disconnect from network element {}'.format(values['ip'])    



if __name__ == '__main__':

    Graph = nx.MultiGraph()
    
    for edges in get_data(nodes):
        edgelist= edges.values()[0]
        for edge in edgelist:
           Graph.add_node(edge.head_node.name)
           Graph.add_edge(edge.head_node.name,edge.tail_node.name)
    nx.draw_networkx(Graph)
    plt.savefig('graph.png')
