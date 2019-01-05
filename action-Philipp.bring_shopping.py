#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import sys

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()

def subscribe_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    action_wrapper(hermes, intentMessage, conf)


def action_wrapper(hermes, intentMessage, conf):
    """ Write the body of the function that will be executed once the intent is recognized. 
    In your scope, you have the following objects : 
    - intentMessage : an object that represents the recognized intent
    - hermes : an object with methods to communicate with the MQTT bus following the hermes protocol. 
    - conf : a dictionary that holds the skills parameters you defined. 
      To access global parameters use conf['global']['parameterName']. For end-user parameters use conf['secret']['parameterName'] 
     
    Refer to the documentation for further details. 
    """
    myKeep = Keep(conf['secret']['gkeep_user'],conf['secret']['gkeep_app_password'])
    if intentMessage.intent.intent_name == "Philipp:addItem_bringshop":
        hermes.publish_end_session(intentMessage.session_id, addItem(hermes,intentMessage,conf))
    elif intentMessage.intent.intent_name == "Philipp:deleteItem_bringshop":
        hermes.publish_end_session(intentMessage.session_id, deleteItem(hermes,intentMessage,conf))
        
def addItem(hermes,intentMessage,conf):
    return "wurde zur Einkaufsliste hinzugefügt!"

def deleteItem(hermes,intentMessage,conf):
    return "wurde von der Einkaufsliste gelöscht!"

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    with Hermes("localhost:1883") as h:
        h.subscribe_intents(subscribe_intent_callback).start()
