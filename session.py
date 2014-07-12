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
root_cert_path = 'ca.pem'
aplicationName = 'cdp-plotter'

network_application = NetworkApplication.get_instance()
network_application.name = applicationName
network_element = network_application.get_network_element(element_hostname)

session_config = SessionConfig(SessionConfig.SessionTransportMode.TLS)
session_config.ca_certs = root_cert_path

session_handle = network_element.connect(username, password, session_config)


