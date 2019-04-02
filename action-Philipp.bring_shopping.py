#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import configparser
import importlib
from BringApi.BringApi import BringApi
import io
import random
import sys
import json

from snips_garuda import Garuda

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, configparser.Error) as e:
        return dict()


def subscribe_intent_callback(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    conf = read_configuration_file(CONFIG_INI)
    if msg.topic == i18n.INTENT_ADD_ITEM:
        garuda.publish_end_session(payload["sessionId"], add_item(payload,conf))
    elif msg.topic == i18n.INTENT_DEL_ITEM:
        garuda.publish_end_session(payload["sessionId"], delete_item(payload,conf))
    elif msg.topic == i18n.INTENT_READ_LIST:
        garuda.publish_end_session(payload["sessionId"], read_list(conf))
    elif msg.topic == i18n.INTENT_CHECK_LIST:
        garuda.publish_end_session(payload["sessionId"], check_list(payload,conf))
    elif msg.topic == i18n.INTENT_DEL_LIST:
        garuda.publish_continue_session(payload["sessionId"], random.choice(i18n.CHK_DEL_ALL), [i18n.INTENT_CONF_DEL[14:],i18n.INTENT_NOCONF_DEL[14:]])
    elif msg.topic == i18n.INTENT_CONF_DEL:
        garuda.publish_end_session(payload["sessionId"], delete_complete_list(conf))
    elif msg.topic == i18n.INTENT_NOCONF_DEL:
        garuda.publish_end_session(payload["sessionId"], random.choice(i18n.NODEL_ALL))
      
def get_bring(conf):
    return BringApi(conf['secret']['uuid'],conf['secret']['bringlistuuid'])

def delete_complete_list(conf):
    bring = get_bring(conf)
    items = bring.get_items().json()['purchase']
    for item in items:
        bring.recent_item(item['name'])
    return random.choice(i18n.DEL_ALL)
    
def add_item_int(bring, items):
    list = bring.get_items().json()['purchase']
    added = []
    exist = []
    for item in items:
        if not any(entr['name'] == item for entr in list):
            bring.purchase_item(item, "")
            added.append(item)
        else:
            exist.append(item)
    return added, exist

def delete_item_int(bring, items):
    list = bring.get_items().json()['purchase']
    removed = []
    exist = []
    for item in items:
        if any(entr['name'] == item for entr in list):
            bring.recent_item(item)
            removed.append(item)
        else:
            exist.append(item)
    return removed, exist

def check_list_int(bring,check):
    list = bring.get_items().json()['purchase']
    found = []
    missing = []
    for c in check:
        if any(c == entr['name'] for entr in list):
            found.append(c)
        else:
            missing.append(c)
    return found, missing


### INTENTS ###
## Add item to list
def add_item(payload,conf):
    items = garuda.get_slot(payload, "Item")
    if len(items) > 0:
        added, exist = add_item_int(get_bring(conf), items)
        return combine_lists(i18n.ADD, i18n.ADD_CONN, i18n.ADD_END, i18n.ADD_F, added, exist)
    else:
        return random.choice(i18n.ADD_WHAT)

## Delete items from list
def delete_item(payload,conf):
    items = garuda.get_slot(payload, "Item")
    if len(items) > 0:
        removed, failed = delete_item_int(get_bring(conf), items)
        return combine_lists(i18n.REM, i18n.REM_CONN, i18n.REM_END, i18n.REM_F, removed, failed)
    else:
        return random.choice(i18n.REM_WHAT)

## check if item is in list
def check_list(payload,conf):
    items = garuda.get_slot(payload, "Item")
    if len(items) > 0:
        found, missing = check_list_int(get_bring(conf), items)
        return combine_lists(i18n.CHK, i18n.CHK_CONN, i18n.CHK_END, i18n.CHK_F, found, missing)
    else:
        return random.choice(i18n.CHK_WHAT)

# Du hast xxx, xxx und xxx auf deiner Einkaufsliste
def read_list(conf):
    items = get_bring(conf).get_items().json()['purchase']
    itemlist = [ l['name'] for l in items ]
    return get_text_for_list(i18n.READ, itemlist)


#### List/Text operations
### Combines two lists(if filled)
# first+CONN+second
# first+END
# second
def combine_lists(str_first, str_conn, str_end, str_second, first, second):
    strout = ""
    if first:
        strout = get_text_for_list(str_first, first)
    if second:
        backup = strout # don't overwrite added list... even if empty!
        strout = get_text_for_list(str_second,second)
    else:
        strout += random.choice(str_end)
    
    if first and second:
        strout = random.choice(str_conn).format(backup,strout)
    return strout

### Combine entries of list into wrapper sentence
def get_text_for_list(str,list):
    category, strout = get_default_list(list)
    return random.choice(str[category]).format(strout)

### Return if MULTI or ONE entry and creates list for multi ( XXX, XXX and XXX )
def get_default_list(items):
    if len(items) > 1:
        return "MULTI", random.choice(i18n.GENERAL_LIST).format(first=", ".join(items[:-1]), last=items[-1])
    elif len(items) == 1:
        return "ONE", items[0]
    else:
        return "NONE", ""

def subscribe_topics(garuda):
    garuda.subscribe(i18n.INTENT_ADD_ITEM, subscribe_intent_callback)
    garuda.subscribe(i18n.INTENT_DEL_ITEM, subscribe_intent_callback)
    garuda.subscribe(i18n.INTENT_READ_LIST, subscribe_intent_callback)
    garuda.subscribe(i18n.INTENT_CHECK_LIST, subscribe_intent_callback)
    garuda.subscribe(i18n.INTENT_DEL_LIST, subscribe_intent_callback)
    garuda.subscribe(i18n.INTENT_CONF_DEL, subscribe_intent_callback)
    garuda.subscribe(i18n.INTENT_NOCONF_DEL, subscribe_intent_callback)
        

if __name__ == "__main__":
    conf = read_configuration_file(CONFIG_INI)
    
    with open("/usr/share/snips/assistant/assistant.json") as json_file:
            language = json.load(json_file)["language"]
    i18n = importlib.import_module("translations." + language)
    
    garuda = Garuda()
    subscribe_topics(garuda) 
    garuda.connect()
    
