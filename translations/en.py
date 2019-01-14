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
GENERAL_LIST = ["{first} and {last}"]


### Read List
### Sentences that can fit a list (GENERAL_LIST) or a single value
READ_ANY = ["You got {} on your shopping list",
            "There is {} on your shopping list"]
### Sentences that can fit only a single value
READ_ONE = READ_ANY+["There is only {} on your shopping list",
                     "{} is the only entrance on your shopping list",
                     "There is nothing but {} on your shopping list"]
### Sentences that can fit a list (GENERAL_LIST)
READ_MULTI = READ_ANY+["{list} are on your shopping list"]
### Response for no list
READ_NONE = ["Your shopping list is empty",
             "The shopping list is empty",
             "There is nothing on your shopping list"]


### Add items
### Sentences that can fit a list (GENERAL_LIST) or a single value
ADD_ANY = ["Ok, I'll add {} to your shopping list",
           "I added {} to the shopping list"]
### Sentences that can fit only a single value
ADD_ONE = ADD_ANY + ["{} has been added to your shopping list",
                     "{} has been written on the shopping list"]
### Sentences that can fit a list (GENERAL_LIST)
ADD_MULTI = ADD_ANY + ["{} were written on your shopping list",
                       "I'll add {} for you on the shopping list"]

#close sentence off for correct pronounciation, eg "." or "!"
#This has to be separate and is only used if no connection is required!
ADD_END = [".", "!"]
### Connector between ADD and ADD_F
ADD_CONN = ["{} , but {}"]

### Sentences that can fit a list (GENERAL_LIST) or a single value
ADD_F_ANY = ["{} was already on your list.",
             "I didn't add {}, because it was already there."]
### Sentences that can fit only a single value
ADD_F_ONE = ADD_F_ANY+["{} was already on your list",
                       "{} is already on the shopping list"]
### Sentences that can fit a list (GENERAL_LIST)
ADD_F_MULTI = ADD_F_ANY+["{} were already on your shopping list"]

### fallback - should not happen
ADD_WHAT = ["I don't know what I should add to your list.",
            "I didn't write anything onto the shopping list."]


### Remove Items
### Sentences that can fit a list (GENERAL_LIST) or a single value
REM_ANY = ["Ok, I removed {} from the shopping list"]
### Sentences that can fit only a single value
REM_ONE = REM_ANY+["Ok, {} was removed from the shopping list",
                   "{} was removed from your list"]
### Sentences that can fit a list (GENERAL_LIST)
REM_MULTI = REM_ANY+["Ok, {} were removed from the list",
                     "{} were removed from your shopping list"]

#close sentence off for correct pronounciation, eg "." or "!"
#This has to be separate and is only used if no connection is required!
REM_END = [".", "!"]
### Connector between ADD and ADD_F
REM_CONN = ["{} , but {}"]

### Sentences that can fit a list (GENERAL_LIST) or a single value
REM_F_ANY = ["I could not find {}."]
### Sentences that can fit only a single value
REM_F_ONE = REM_F_ANY+["{} was not on the shopping list."]
### Sentences that can fit a list (GENERAL_LIST)
REM_F_MULTI = REM_F_ANY+["{} were not on the shopping list."]
### fallback - should not happen
REM_WHAT = ["I don't know what I should remove from the shopping list.",
            "I didn't remove anything from the shopping list."]


### Check Items
### Sentences that can fit a list (GENERAL_LIST) or a single value
CHK_ANY = ["I found {} on your shopping list"]
### Sentences that can fit only a single value
CHK_ONE = CHK_ANY+["{} is on your shopping list"]
### Sentences that can fit a list (GENERAL_LIST)
CHK_MULTI = CHK_ANY+["{} are on the shopping list"]

#close sentence off for correct pronounciation, eg "." or "!"
#This has to be separate and is only used if no connection is required!
CHK_END = [".", "!"]
### Connector between ADD and ADD_F
CHK_CONN = ["{} , but {}"]

### Sentences that can fit a list (GENERAL_LIST) or a single value
CHK_F_ANY = ["I couldn't find {}."]
### Sentences that can fit only a single value
CHK_F_ONE = CHK_F_ANY+["{} was not on your list.",
                       "{} was not written on the shopping list."]
### Sentences that can fit a list (GENERAL_LIST)
CHK_F_MULTI = CHK_F_ANY+["{} are not on your shopping list."]
### fallback - should not happen
CHK_WHAT = ["I don't know what I should look for on your shopping list"]


### DON'T EDIT!
#Only for technical purpose!
ADD = {"ONE":ADD_ONE,"MULTI":ADD_MULTI}
ADD_F = {"ONE":ADD_F_ONE,"MULTI":ADD_F_MULTI}
REM = {"ONE":REM_ONE,"MULTI":REM_MULTI}
REM_F = {"ONE":REM_F_ONE,"MULTI":REM_F_MULTI}
CHK = {"ONE":CHK_ONE,"MULTI":CHK_MULTI}
CHK_F = {"ONE":CHK_F_ONE,"MULTI":CHK_F_MULTI}
READ = {"ONE":READ_ONE,"MULTI":READ_MULTI, "NONE":READ_NONE}