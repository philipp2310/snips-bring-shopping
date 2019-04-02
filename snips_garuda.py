#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Garuda (Sanskrit à¤—à¤°à¥�à¤¡ garuá¸�a, m.) ist in der indischen Mythologie ein 
schlangentötendes, halb mensch-, halb adlergestaltiges Reittier (Vahana) des Vishnu, 
Sohn des Kashyapa und der Vinata. 
In der asiatischen Mythologie hat der Garuda zugleich die Bedeutung eines Götterboten, 
der den Menschen Nachrichten und Anweisungen der Götter überbringt.

--->

Vereinfachte Form von Hermes.
Weniger Möglichkeiten, dafür wird aber mit Passwort Unterstützung!
"""
import io
import sys
import paho.mqtt.client as mqtt
import toml
import json


DM_END_SESSION = "hermes/dialogueManager/endSession"
DM_CONTINUE_SESSION = "hermes/dialogueManager/continueSession"
class Garuda():
    
    #performed on connect    
    def subscribe_topics(self, client, userdata, flags, rc):
        self.client.subscribe(self.subs)
        for call in self.callbacks:
            self.client.message_callback_add(call[0], call[1])
    
    #add topics to subs list -> not possible after connect!
    def subscribe(self, topic, callback):
        self.subs.append((topic, 0))
        self.callbacks.append((topic, callback))
        
    def connect(self):
        self.client.connect(self.mqtt_host, self.mqtt_port, 60)
        self.client.loop_forever()

    def publish_end_session(self, sessid, text):
        self.client.publish(DM_END_SESSION, json.dumps({'text': text, 'sessionId': sessid}))

    def publish_continue_session(self, sessid, text, intentFilter=""):
        self.client.publish(DM_CONTINUE_SESSION, json.dumps({'text': text, 'sessionId': sessid, 'intentFilter' : intentFilter}))
    
    def set_password(self, snips_toml):
        if 'mqtt_username' in snips_toml['snips-common'] and 'mqtt_password' in snips_toml['snips-common']:
                self.client.username_pw_set(snips_toml['snips-common']['mqtt_username'], snips_toml['snips-common']['mqtt_password'])

    def get_host(self, snips_toml):
        if 'mqtt' in snips_toml['snips-common']:
                self.mqtt_host, port = snips_toml['snips-common']['mqtt'].split(':')
                self.mqtt_port = int(port)
    
    def get_slot(self, payload, slot):
        return [x['value']['value'] for x in payload['slots'] if x['slotName'] == slot ]
        
    #def get_tls(self, snips_toml):
        ## MQTT TLS configuration
        # mqtt_tls_hostname = ""
        # mqtt_tls_disable_root_store = false
        # mqtt_tls_cafile = ""
        # mqtt_tls_capath = ""
        # mqtt_tls_client_cert = ""
        # mqtt_tls_client_key = ""
        #tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLS, ciphers=None)
        #self.client.tls_set("C:/Windows/system32/config/systemprofile/Desktop/attachments/server iot.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
        #self.client.tls_insecure_set(True)
                
    def __init__(self):
        self.mqtt_host = 'localhost'
        self.mqtt_port = 1883
        self.subs = []
        self.callbacks = []
        
        self.client = mqtt.Client()
        self.client.on_connect = self.subscribe_topics
        
        try:        
            with open("/etc/snips.toml") as toml_file:
                snips_toml = toml.load(toml_file)
        
            if 'snips-common' in snips_toml:
                self.set_password(snips_toml)
                self.get_host(snips_toml) 
            
        except toml.decoder.TomlDecodeError:
            print("Decoding TOML did not work. Using defaults localhost:1883")
                    
        