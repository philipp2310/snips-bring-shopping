#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###
# English Translation
# Add inside of the brackets any possible sentence - but be aware: every combination might occure!
###
### Intents
INTENT_ADD_ITEM = "Philipp:addItem_bringshop"
INTENT_DEL_ITEM = "Philipp:deleteItem_bringshop"
INTENT_READ_LIST = "Philipp:readList_bringshop"
INTENT_CHECK_LIST = "Philipp:checkList_bringshop"

# {XXX, XXX, XXX} und XXX
GENERAL_LIST = ["{first} and {last}"]
                
# Auf deiner Einkaufsliste steht {XXX, XXX und XXX}
READ_LOT = ["You got {list} on your shopping list",
            "There is {list} on your shopping list",
            "{list} is on your shopping list"]
READ_ONE = ["There is only {list} on your shopping list",
            "{list} is the only entrance on your shopping list",
            "There is nothing but {list} on your shopping list"]

READ_NONE = ["Your shopping list is empty",
             "The shopping list is empty",
             "There is nothing on your shopping list"]

### Add items
# {first} und {last} wurden zur Einkaufsliste hinzugefügt
# {XXX, XXX} und XXX wurden zur Einkaufsliste hinzugefügt
ADD_START_LOT = ["{first} and {last} were"]
# {first} wurde zur Einkaufsliste hinzugefügt
# XXX wurde zur Einkaufsliste hinzugefügt
ADD_START_ONE = ["{first} was"]

ADD_END = ["added to your shopping list",
           "written on the shopping list"]

#. (close sentence off for correct pronounciation, eg "." or "!")
#not inserted if sentence continues with exclusions:
ADD_CLOSE = [".", "!"]

#, aber YYY, YYY und YYY waren bereits vorhanden
ADD_F_START = [", but"]
ADD_F_START_LOT = ["{first} and {last} were"]
ADD_F_START_ONE = ["{first} was"]
ADD_F_END = ["already on your shopping list",
             "already on the list"]

ADD_WHAT = ["I don't know what I should add to your shopping list"]

### Remove Items
# XXX, XXX und XXX wurden von der Einkaufsliste gestrichen
REM_START_LOT = ["{first} and {last} were"]
REM_START_ONE = ["{first} was"]
REM_END = ["removed from the shopping list",
           "deleted",
           "deleted from your shopping list"]

#, aber YYY, YYY und YYY waren nicht vorhanden
REM_F_START = [", but"]
REM_F_START_LOT = ["{first} and {last} were"]
REM_F_START_ONE = ["{first} was"]
REM_F_END = ["not on the list",
             "not on your shopping list"]

#. (close sentence off for correct pronounciation, eg "." or "!")
REM_CLOSE = [".", "!"]

REM_WHAT = ["I don't know what I should remove from your shopping list"]

### Check items
# {first} und {last} sind auf der  Einkaufsliste vorhanden
# {XXX, XXX} und XXX sind auf der Einkaufsliste vorhanden
CHK_START_LOT = ["{first} and {last} are"]
# {first} ist auf der Einkaufsliste vorhanden
# XXX wurde zur Einkaufsliste hinzugefügt
CHK_START_ONE = ["{first} is"]

CHK_END = ["on your shopping list",
           "written on your list"]

#. (close sentence off for correct pronounciation, eg "." or "!")
#not inserted if sentence continues with exclusions:
CHK_CLOSE = [".", "!"]

#, aber YYY, YYY und YYY waren bereits vorhanden
CHK_F_START = [", but"]
CHK_F_START_LOT = ["{first} and {last} are"]
CHK_F_START_ONE = ["{first} is"]
CHK_F_END = ["not on the list.",
             "not on your shopping list."]
