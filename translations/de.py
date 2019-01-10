#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###
# German Translation
# Add inside of the brackets any possible sentence - but be aware: every combination might occure!
###
### Intents
INTENT_ADD_ITEM = "Philipp:addItem_bringshop"
INTENT_DEL_ITEM = "Philipp:deleteItem_bringshop"

# {XXX, XXX, XXX} und XXX
GENERAL_LIST = ["{first} und {last}",
                "{first} so wie {last}"]
                
# Auf deiner Einkaufsliste steht {XXX, XXX und XXX}
READ_LOT = ["Auf deiner Einkaufsliste steht {list}",
            "Du hast {list} auf deiner Einkaufsliste stehen",
            "{list} stehen auf deiner Einkaufsliste"]
READ_ONE = ["Auf deiner Einkaufsliste steht {list}",
            "Du hast nur {list} auf deiner Einkaufsliste stehen",
            "Ausser {list} steht nichts auf dem Einkaufszettel"]

READ_NONE = ["Du hast nichts auf deiner Einkaufsliste",
             "Deine Einkaufsliste ist leer",
             "Es steht nichts auf der Einkaufsliste",
             "Du hast noch nichts auf deiner Einkaufsliste"]
### Add items
# {first} und {last} wurden zur Einkaufsliste hinzugefügt
# {XXX, XXX} und XXX wurden zur Einkaufsliste hinzugefügt
ADD_START_LOT = ["{first} und {last} wurden",
                 "{first} so wie {last} wurden"]
# {first} wurde zur Einkaufsliste hinzugefügt
# XXX wurde zur Einkaufsliste hinzugefügt
ADD_START_ONE = ["{first} wurde"]

ADD_END = ["zur Einkaufsliste hinzugefügt",
           "hinzugefügt",
           "auf die Einkaufsliste gesetzt",
           "auf den Einkaufszettel geschrieben"]

#. (close sentence off for correct pronounciation, eg "." or "!")
#not inserted if sentence continues with exclusions:
ADD_CLOSE = [".", "!"]

#, aber YYY, YYY und YYY waren bereits vorhanden
ADD_F_START = [", aber"]
ADD_F_START_LOT = ["{first} und {last} waren"
                   "{first} so wie {last} waren"]
ADD_F_START_ONE = ["{first} war"]
ADD_F_END = ["bereits vorhanden.",
             "schon auf der Einkaufsliste.",
             "auf der Einkaufsliste schon vorhanden.",
             "bereits auf der Einkaufszettel vorhanden."]

ADD_WHAT = ["Ich weiß nicht was ich auf die Einkaufsliste schreiben soll",
            "Ich habe nichts auf den Einkaufszettel geschrieben"]

### Remove Items
# XXX, XXX und XXX wurden von der Einkaufsliste gestrichen
REM_START_LOT = ["{first} und {last} wurden",
                 "{first} so wie {last} wurden"]
REM_START_ONE = ["{first} wurde"]
REM_END = ["von der Einkaufsliste gestrichen",
           "entfernt",
           "von der Einkaufsliste genommen",
           "vom Einkaufszettel gelöscht"]

#, aber YYY, YYY und YYY waren nicht vorhanden
REM_F_START = [", aber"]
REM_F_START_LOT = ["{first} und {last} waren",
                   "{first} so wie {last} waren"]
REM_F_START_ONE = ["{first} war"]
REM_F_END = ["nicht vorhanden",
             "nicht auf der Liste",
             "nicht auf dem Einkaufszettel",
             "nicht auf meiner Einkaufsliste"]

#. (close sentence off for correct pronounciation, eg "." or "!")
REM_CLOSE = [".", "!"]

REM_WHAT = ["Ich weiß nicht was ich von der Einkaufsliste streichen soll.",
            "Ich habe nichts vom Einkaufszettel gelöscht."]