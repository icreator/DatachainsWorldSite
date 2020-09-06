#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from gluon import *

### IN ->
def update_bal_exchange(db, man_bal_from, amo_from, man_bal_to, amo_to, on_date):
    db.man_bal_txs.insert( in_id = man_bal_to.id, amo_in = amo_to,
                           out_id = man_bal_from.id, amo_out = amo_from, created_on = on_date)
    man_bal_from.update_record( bal = man_bal_from.bal - amo_from)
    man_bal_to.update_record( bal = man_bal_to.bal + amo_to)
    
    ## for own servise balances - negate
    cash_from = db.cash[ man_bal_from.cash_id ]
    cash_from.update_record( own_bal = cash_from.own_bal + amo_from)
    cash_to = db.cash[ man_bal_to.cash_id ]
    cash_to.update_record( own_bal = cash_to.own_bal - amo_to)

    ## reference man take GIFT
    man_from = db.men[ man_bal_from.man_id ]
    if man_from.ref_man and len(man_from.ref_man) > 5:
        ref_man = db(db.men.ref_key == man_from.ref_man).select().first()
        if ref_man and cash_to.ref_gift and cash_to.ref_gift > 0:
            if cash_to.ref_gift < 1:
                gift_amo = cash_to.ref_gift * amo_to
                gift_mess = 'KOEFF(%s) * AMO(%s)' % (cash_to.ref_gift, amo_to)
            else:
                gift_amo = cash_to.ref_gift
                gift_mess = 'GIFT(%s) by AMO(%s)' %  (cash_to.ref_gift, amo_to)
            
            ref_man_bal = db((db.man_bals.man_id == ref_man.id)
                    & (db.man_bals.cash_id == cash_to.id)).select().first()

            update_bal_gift(db, ref_man_bal, cash_to, gift_amo, on_date, 'Gift by ref.man[' + man_from.ref_key + ']: ' + gift_mess)
    
    return

### as GIFT for men
def update_bal_gift(db, man_bal, cash, amo, on_date, mess):
    cash = cash or db.cash[ man_bal.cash_id ]
    ## amo_out = -1 -> for GIFT icon
    db.man_bal_txs.insert( in_id = man_bal.id, amo_in = amo, amo_out = -1, created_on = on_date, mess = mess)
    man_bal.update_record( bal = man_bal.bal + amo, dep_incomed = man_bal.dep_incomed + amo)

def update_bal_local(db, man_bal_out, man_bal_in, amo, on_date, mess):
    db.man_bal_txs.insert( out_id = man_bal_out.id, in_id = man_bal_in.id, amo_out = amo, amo_in = amo, created_on = on_date, mess = mess)
    man_bal_out.update_record( bal = man_bal_out.bal - amo)
    man_bal_in.update_record( bal = man_bal_in.bal + amo)
    return

def update_bal_total(db, man_bal, man_acc, amo, op_id, on_date, mess = ''):
    cash = db.cash[ man_bal.cash_id ]
    if amo > 0:
        # INCOME
        db.man_bal_txs.insert( in_id = man_bal.id, amo_in = amo, op_id = op_id, created_on = on_date, mess = mess)
        ## INCOMED update too!
        man_bal.update_record( bal = man_bal.bal + amo, dep_incomed = man_bal.dep_incomed + amo)
        cash.update_record( bal = cash.bal + amo)
    else:
        # OUTCOME
        db.man_bal_txs.insert( out_id = man_bal.id, acc_id = man_acc.id, amo_out = amo, op_id = op_id, created_on = on_date)
        man_acc.update_record(amo_outcomed = man_acc.amo_outcomed - amo) ## negate
        man_bal.update_record( bal = man_bal.bal + amo)
        cash.update_record( bal = cash.bal + amo)

    return

def try_send(db, man, cash, man_bal_out, man_in, amount, on_date, mess):
    if man_bal_out.bal < amount:
        return 'not enougth balance'
    if amount <= 0:
        return 'wrong amount'
    
    # SEEK man_bal IN
    man_bal_in = db((db.man_bals.man_id == man_in.id)
                    & (db.man_bals.cash_id == cash.id)).select().first()
    if not man_bal_in:
        man_bal_in_id = db.man_bals.insert(man_id = man_in.id, cash_id = cash.id)
        man_bal_in = db.man_bals[ man_bal_in_id ]

    update_bal_local(db, man_bal_out, man_bal_in, amount, on_date, mess)
    db.commit()
    
    return 'sended'
