# -*- coding: utf-8 -*-
# попробовать что-либо вида

if request.ajax:
    if not request.is_local:
        raise HTTP(501, 'error')
else:
    if not IS_LOCAL:
        raise HTTP(501, 'error')


CASH_STAR_A = 20

def getList():
    res = {}
    
    for rec in  db((db.man_bals.bal > 0)
             & (db.man_bals.cash_id == CASH_STAR_A)).select():
        acc = db(db.man_accs.bal_id == rec.id).select().first()
        if acc and acc.acc and len(acc.acc) > 25:
            res[acc.acc] = int(rec.bal)

    return '%s' % res

def bonus_to_star():
    h = CAT()
    cntr = 0
    adds = 0
    import bonus_lib
    for r in db(db.men).select():
        # found referals
        _, ref_bonus = bonus_lib.calc_referals(db, r)
        ref_bonus = bonus_lib.calc_referals_bonus(ref_bonus)
            
        bonus = (r.bonus or 0) + ref_bonus

        if bonus == 0:
            continue

        cntr +=1

        man_bal = db((db.man_bals.man_id == r.id)
                     & (db.man_bals.cash_id == CASH_STAR_A)).select().first()
        
        if not man_bal:
            adds +=1
            db.man_bals.insert(man_id = r.id, cash_id = CASH_STAR_A, bal = bonus)
        else:
            man_bal.update_record(bal = bonus)
        
            
    
    h += H3('updated: ', cntr, ' added: ', adds)
    
    return dict(h = DIV(h, _class='container'))
    

def soc_bonus_add():
    man = db.men[ request.args(0) ]
    if not man:
        return 'error'
        
    bonus_up = 1
    if request.args(1) == '1':
        man.update_record(social1 = ('+%s' % bonus_up) + ': ' + man.social1, bonus = man.bonus + bonus_up)
    else:
        man.update_record(social2 = ('+%s' % bonus_up) + ': ' + man.social2, bonus = man.bonus + bonus_up)
        
    return 'DONE +%s' % bonus_up

def soc_bonus_nul():
    man = db.men[ request.args(0) ]
    if not man:
        return 'error'
        
    if request.args(1) == '1':
        man.update_record(social1 = None)
    else:
        man.update_record(social2 = None)
        
    return 'NULL'

def soc_bonus():
    h = CAT(H3(A('bonuses to STAR RUB', _href=URL('bonus_to_star'), _class='white')))
    
    for r in db(db.men).select():
        if not r.social1 and not r.social2:
            continue
        if r.bonus > 1:
            # for URL not add bonuses
            continue
        if r.social1 and r.social2 and r.social1[0:1] == '+' and r.social2[0:1] == '+':
            continue

            
        h += H3(r.name,' ', r.email)
        if r.social1 and r.social1[0:1] != '+':
            h += DIV(P(A(B(r.social1), _href=r.social1, _target='blank', _class='white')),
                 P(
                    A('ADD BONUS', _onclick = 'ajax("soc_bonus_add/%s/1", [], "%s")' % (r.id, '1_' + r.ref_key), _class='blue'), ' ',
                    A('NULL URL', _onclick = 'ajax("soc_bonus_nul/%s/1", [], "%s")' % (r.id, '1_' + r.ref_key), _class='blue')
                ),
                     _id='1_' + r.ref_key)
        if r.social2 and r.social2[0:1] != '+':
            h += DIV(P(A(B(r.social2), _href=r.social2, _target='blank', _class='white')),
                 P(
                    A('ADD BONUS', _onclick = 'ajax("soc_bonus_add/%s/2", [], "%s")' % (r.id, '2_' + r.ref_key), _class='blue'), ' ',
                    A('NULL URL', _onclick = 'ajax("soc_bonus_nul/%s/2", [], "%s")' % (r.id, '2_' + r.ref_key), _class='blue')
                ),
                     _id='2_' + r.ref_key)
        
        h += HR()
    return dict(h = DIV(h, _class='container'))

def index(): return dict(message="hello from tools_soc.py")
