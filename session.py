#!/usr/bin/python

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

element_hostname = '10.10.10.110'
username = 'evelio'
password = 'vila'
transport = "tls"
network_element = None
session_handle = None
root_cert_path = 'ca.pem'
aplicationName = 'cdp-plotter'

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


if __name__ == '__main__':
	cdp_plotter = Create_Ne(aplicationName,root_cert_path,element_hostname)
	ne = cdp_plotter.get_ne()
	session_config = cdp_plotter.config()
	session_handle = ne.connect(username, password, session_config)

