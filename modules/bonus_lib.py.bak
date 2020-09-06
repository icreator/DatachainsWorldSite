#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from gluon import *

def calc_referals(db, r):
    ref_bonus = 0
    ref_count = 0
    
    if r.ref_key:
        for referal in db(db.men.ref_man == r.ref_key).select():
            ref_count +=1
            if referal.bonus:
                ref_bonus +=1
    else:
        print 'ref_key = None - ', r.email
    
    return ref_count, ref_bonus

def calc_referals_bonus(ref_bonus):

    if ref_bonus == 0:
        ref_bonus = 0
    elif ref_bonus <= 3 :
        ref_bonus = 1
    elif ref_bonus <= 10:
        ref_bonus = 2
    elif ref_bonus <= 33:
        ref_bonus = 3
    elif ref_bonus <= 100:
        ref_bonus = 4
    elif ref_bonus <= 333:
        ref_bonus = 5
    else:
        ref_bonus = 6
        
    return ref_bonus
