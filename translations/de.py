#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###
# German Translation
# Add inside of the brackets any possible sentence - but be aware: every combination might occure!
###
### Intents
INTENT_ADD_ITEM = "Philipp:addItem_bringshop"
INTENT_DEL_ITEM = "Philipp:deleteItem_bringshop"
INTENT_READ_LIST = "Philipp:readList_bringshop"
INTENT_CHECK_LIST = "Philipp:checkList_bringshop"

# {XXX, XXX, XXX} und XXX
GENERAL_LIST = ["{first} und {last}",
                "{first} so wie {last}"]


### Read List
### Sentences that can fit a list (GENERAL_LIST) or a single value
READ_ANY = ["Auf deiner Einkaufsliste steht {list}"]
### Sentences that can fit only a single value
READ_ONE = READ_ANY+["Du hast nur {list} auf deiner Einkaufsliste stehen",
                    "Ausser {list} steht nichts auf dem Einkaufszettel"]
### Sentences that can fit a list (GENERAL_LIST)
READ_MULTI = READ_ANY+["Du hast {list} auf deiner Einkaufsliste stehen",
                       "{list} stehen auf deiner Einkaufsliste"]
### Response for no list
READ_NONE = ["Du hast nichts auf deiner Einkaufsliste",
             "Deine Einkaufsliste ist leer",
             "Es steht nichts auf der Einkaufsliste",
             "Du hast noch nichts auf deiner Einkaufsliste"]


### Add items
### Sentences that can fit a list (GENERAL_LIST) or a single value
ADD_ANY = ["Ok, ich schreibe {} auf den Einkaufszettel",
           "Ich habe {} auf den Einkaufszettel geschrieb"]
### Sentences that can fit only a single value
ADD_ONE = ADD_ANY + ["{} wurde auf die Einkaufsliste geschrieben",
                     "{} wurde hinzugefügt"]
### Sentences that can fit a list (GENERAL_LIST)
ADD_MULTI = ADD_ANY + ["{} wurden auf die Einkaufsliste geschrieben",
                       "Ich schreibe folgendes auf die Einkaufsliste: {}"]

#close sentence off for correct pronounciation, eg "." or "!"
#This has to be separate and is only used if no connection is required!
ADD_CLOSE = [".", "!"]
### Connector between ADD and ADD_F
ADD_CONN = ["{} , aber {}"]

### Sentences that can fit a list (GENERAL_LIST) or a single value
ADD_F_ANY = ["{} steht schon auf der Liste"]
### Sentences that can fit only a single value
ADD_F_ONE = ADD_F_ANY+["{} ist bereits vorhanden",
                       "{} steht schon auf der Liste"]
### Sentences that can fit a list (GENERAL_LIST)
ADD_F_MULTI = ADD_F_ANY+["{} sind bereits vorhanden",
                         "{} standen schon auf der Liste",
                         "{} stehen schon auf deiner Einkaufsliste"]

### fallback - should not happen
ADD_WHAT = ["Ich weiß nicht was ich auf die Einkaufsliste schreiben soll",
            "Ich habe nichts auf den Einkaufszettel geschrieben"]


### Remove Items
### Sentences that can fit a list (GENERAL_LIST) or a single value
REM_ANY = ["Ich habe {} von der Einkaufsliste gestrichen"]
### Sentences that can fit only a single value
REM_ONE = REM_ANY+["Ok, {} ist von der Liste gestrichen worden",
                   "{} wurde von der Einkaufsliste gestrichen"]
### Sentences that can fit a list (GENERAL_LIST)
REM_MULTI = REM_ANY+["Ok, {} sind von der Liste gestrichen worden",
                     "{} wurden von der Einkaufsliste gestrichen"]

#close sentence off for correct pronounciation, eg "." or "!"
#This has to be separate and is only used if no connection is required!
REM_CLOSE = [".", "!"]
### Connector between ADD and ADD_F
REM_CONN = ["{} , aber {}"]

### Sentences that can fit a list (GENERAL_LIST) or a single value
REM_F_ANY = ["ich konnte {} nicht finden."]
### Sentences that can fit only a single value
REM_F_ONE = REM_F_ANY+["{} stand nicht auf der Liste."]
### Sentences that can fit a list (GENERAL_LIST)
REM_F_MULTI = REM_F_ANY+["{} standen nicht auf der Einkaufsliste."]
### fallback - should not happen
REM_WHAT = ["Ich weiß nicht was ich von der Einkaufsliste streichen soll.",
            "Ich habe nichts vom Einkaufszettel gelöscht."]


### Check Items
### Sentences that can fit a list (GENERAL_LIST) or a single value
CHK_ANY = ["Ich habe {} auf der Einkaufsliste gefunden"]
### Sentences that can fit only a single value
CHK_ONE = CHK_ANY+["{} steht auf der Einkaufsliste",
                   "{} befindet sich auf dem Einkaufszettel"]
### Sentences that can fit a list (GENERAL_LIST)
CHK_MULTI = CHK_ANY+["{} stehen auf der Einkaufsliste",
                     "{} stehen auf deinem Einkaufszettel"]

#close sentence off for correct pronounciation, eg "." or "!"
#This has to be separate and is only used if no connection is required!
CHK_CLOSE = [".", "!"]
### Connector between ADD and ADD_F
CHK_CONN = ["{} , aber {}"]

### Sentences that can fit a list (GENERAL_LIST) or a single value
CHK_F_ANY = ["ich konnte {} nicht finden."]
### Sentences that can fit only a single value
CHK_F_ONE = CHK_F_ANY+["{} steht nicht auf der Liste."]
### Sentences that can fit a list (GENERAL_LIST)
CHK_F_MULTI = CHK_F_ANY+["{} stehen nicht auf der Einkaufsliste.",
                         "{} stehen nicht auf deinem Einkaufszettel"]
### fallback - should not happen
CHK_WHAT = ["Ich weiß nicht was ich auf der Einkaufsliste suchen soll.",
            "Ich weiß nicht was ich auf dem Zettel suchen soll."]


### DON'T EDIT!
#Only for technical purpose!
ADD = ["ONE":ADD_ONE,"MULTI":ADD_MULTI]
ADD_F = ["ONE":ADD_F_ONE,"MULTI":ADD_F_MULTI]
REM = ["ONE":REM_ONE,"MULTI":REM_MULTI]
REM_F = ["ONE":REM_F_ONE,"MULTI":REM_F_MULTI]
CHK = ["ONE":CHK_ONE,"MULTI":CHK_MULTI]
CHK_F = ["ONE":CHK_F_ONE,"MULTI":CHK_F_MULTI]
READ = ["ONE":READ_ONE,"MULTI":READ_MULTI, "NONE":READ_NONE]
