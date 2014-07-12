!/usr/bin/python

#Cnx and session handling

import logging
from onep.element import NetworkElement
from onep.element import NetworkApplication
from onep.element import SessionConfig
from onep.element import SessionHandle
from onep.element import SessionStatistics
from onep.element import SessionProperty
from onep.core.exception import OnepException
from onep.core.util import tlspinning

element_hostname = '10.0.2.17'
username = 'evelio'
password = 'vila'
transport = "tls"
network_element = None
session_handle = None
root_cert_path = './ca.pem'
aplicationName = 'cdp-plotter'

class Create_Ne(name,ca,ip):

    def __init__(self,name):
        self.app_name = name
        self.ca_path = ca
        self.ip = ip
            
    def config(self):
        self.session_config = SessionConfig(SessionConfig.SessionTransportMode.TLS)
        self.session_config.ca_certs = self.ca_path

    def get_ne(self,ip):
        network_application = NetworkApplication.get_instance()
        network_application.name = self.app_name
        network_element = network_application.get_network_element(self.ip)
        return network_element


if __name__ == '__main__':

    cdp-plotter = Create_Ne(aplicationName,root_cert_path)
    ne = cdp_plotter.get_ne(element_hostname)
    session_config = ne.config()
    session_handle = network_element.connect(username, password, session_config)




