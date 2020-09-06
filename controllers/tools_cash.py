# -*- coding: utf-8 -*-

def recalc_cash_out():
    cash_id = request.args(0)
    if not cash_id:
        return '/[cash_id]'
    
    cash = db.cash [ cash_id ]
    if not cash:
        return 'cash not found'
    
    res = 0
    for rec in db(db.man_bals.cash_id==cash_id).select():
        res += rec.bal
    
    cash.update_record(own_bal = -res)
    
    return cash.name + (' %s' % res)

def del_twin_accs():
    ids = []
    cnt = 0
    for rec in db(db.man_accs).select():
        if rec.id in ids:
            continue
            
        for rec_twin in db((db.man_accs.acc == rec.acc)
                           & (db.man_accs.bal_id == rec.bal_id)).select():
            if rec_twin.id == rec.id:
                continue
            ids.append(rec_twin.id)
            cnt += 1

    for id in ids:
        del db.man_accs[id]

    return '%s' % cnt

def index(): return dict(message="hello from tools_cash.py")
