# -*- coding: utf-8 -*-

def index():

    ##bill_id = request.vars.get('bill')
    ##if not bill_id:
    ##    return '?bill='
    order_id = request.vars.get('order')
    if not order_id:
        return '?order='

    man = db(db.men.ref_key == order_id).select().first()
    if not man:
        return 'man not found'

    rec = db((db.man_bals.man_id == man.id)
                 & (db.man_bals.cash_id == db.cash.id)
                 & (db.cash.system_id == myconf.take('cash.bitcoin_id', cast=int))
                 ).select().first()
    
    man_bal = rec and rec.man_bals
    if not man_bal:
        return 'man_bal not found'
    
    if not man_bal.dep_bill:
        return 'dep_bill empty'

    from gluon.tools import fetch
    url = 'http://lite.cash/api_bill/check.json/%s?status=HARD' % man_bal.dep_bill
    #print url
    resp = fetch(url)
    #print resp
    import gluon.contrib.simplejson as sj
    res = sj.loads(resp) # {'bill': bill_id }
    err = res.get('error')
    if err:
        return '%s' % err

    try:
        ## PRESICION not worked with floats
        ##import decimal
        ## not worked with floats
        ##decimal_context = decimal.Context(prec=8, rounding=decimal.ROUND_HALF_DOWN)
        ##decimal.setcontext(decimal_context)
        new_bal = Decimal('%s' % res['payed']) #, decimal_context)
    except:
        return 'bal value error'

    amo = new_bal - man_bal.dep_incomed
    if amo <0:
        return 'error value <'
    elif amo == 0:
        return 'same value'

    ##man_bal.update_record( dep_incomed = new_bal )
    import account
    # TODO need to get last txid from api_bill/info
    man_acc = None
    op_id = None
    account.update_bal_total(db, man_bal, man_acc, amo, op_id, request.now)
    
    return 'bal BTC stored for %s' % man_bal.id
