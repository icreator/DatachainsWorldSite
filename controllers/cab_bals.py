# -*- coding: utf-8 -*-
# try something like

FULL_PROJECT_NAME = 'DATACHAINS.World blockchain 3.0 project'

CLRS_btn = '-tre btn-lg pull-right'
CLRS_btn2 = '-tre btn-lg pull-right'

def u(h, url, cls='col-sm-4'):
    return DIV(DIV(P(h, _class='btn_mc2'), _class='btn_mc1', _onclick="location.href='%s'" % url), _class='btn_mc ' + cls)


def deposit():
    return 'Only direct bitcoin bets used now'
def withdraw():
    return 'Only direct bitcoin bets used now'

import re
regular_phone = re.compile("\D")
def valid_phone(ph):
    if not ph:
        return
    str = regular_phone.sub("","%s" % ph)
    return str

def check_args(request, session, cash_system_id):
    man_id = session.man_id
    if not man_id:
        return 'session error 1', None, None, None
    man_bal_id = request.args(0)
    if not man_bal_id:
        return 'empty man_bal_id', None, None, None
    man_bal = db.man_bals[ man_bal_id ]
    if not man_bal:
        return 'empty man_bal', None, None, None
    if man_bal.man_id != man_id:
        return 'session error 2', None, None, None
    
    man = db.men[ man_bal.man_id ]
    if not man:
        return 'error man', None, None, None
    
    cash = db.cash[ man_bal.cash_id ]
    if not cash:
        return 'error cash', None, None, None
    
    if cash_system_id and cash.system_id != cash_system_id:
        return T('В разработке'), None, None, None
    
    return None, man, cash, man_bal


def send():
    error, man, cash, man_bal = check_args(request, session, cash_system_id = None)
    if error:
        return dict(h = H1(error))
    
    response.title=T('Передать ресурс')
    response.not_show_function = True
    
    if cash.unsend:
        return dict(h = DIV(H2(T('Этот актив невозможно передать!')), _class='container'))

    cash_system = db.cash_system[ cash.system_id ]
    h = CAT(
        H2(T('Вы хотите передать ресурс %s') % cash_system.name + ':' + cash.name),
        H4(T('Ваш текущий баланс'),': ', man_bal.bal)
        )
    
    form = FORM(H3(T('Задайте получателя по емайл или телефону или указателю')),
        LABEL(T('Емайл'),':'),' ', INPUT(_name='email', requires=IS_EMPTY_OR(IS_EMAIL())), BR(),
        P(T('Внимание! Если участник с таким емайл не найден, то считается что он еще не зарегистрировался и баланс для этого емайл будет пополнен и останется лежать до востребования. Участник просто должен зарегистрировать свой емайл и в личном кабинете у него будет уже пополненный баланс.')),
        LABEL(T('Телефон'),':'),' ', INPUT(_name='phone'), BR(),
            BR(),
        LABEL(T('Указатель участника'),':'),' ', INPUT(_name='ref_key'), BR(),
        SPAN('*',T('Реферальный код или счет блокчейн-среды')),
        H3(T('Сколько Вы хотите передать?')),
        LABEL(T('Количество'),':'),' ', INPUT(_name='amount'), BR(),
        H3(T('Весточка')),
        TEXTAREA(_name='mess'),
        INPUT(_type='submit', _class='btn btn-' + CLRS_btn))

    h += form

    if form.accepts(request, session, keepvalues=True):
        email = form.vars.email
        phone = form.vars.phone
        phone = valid_phone(phone)
        ref_key = form.vars.ref_key
        mess = form.vars.mess
        # заменить все не цифры и проверить длинну

        if mess and len(mess) > 200:
            mess = mess[:200]
        if email:
            find_by = 'email'
            man_in = db(db.men.email == email ).select().first()
            if not man_in:
                import random
                import string
                while True:
                    ref_key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(10))
                    if not db(db.men.ref_key == ref_key).select().first():
                        break

                man_in_id = db.men.insert(email = email, ref_key = ref_key )
                db.commit()
                man_in = db.men[ man_in_id ]
        elif phone:
            find_by = 'phone'
            man_in = db(db.men.phone == phone ).select().first()
        elif ref_key:
            find_by = 'ref_key'
            if len(ref_key) > 20:
                ## AS BLOCKCHAIN ACCOUNT
                man_in = db((db.man_accs.acc == ref_key)
                           & (db.man_bals.id == db.man_accs.bal_id)
                           & (db.man_bals.man_id == db.men.id)).select().first()
                man_in = man_in and man_in.men
            else:
                man_in = db(db.men.ref_key == ref_key ).select().first()
        else:
            man_in = None
            find_by = 'phone'
        

        if not man_in:
            mess = T('Такой участник не найден')
            response.flash = mess
            form.errors[find_by] = mess
            return dict(h = DIV(h, _class='container'))
        
        amount = form.vars.amount
        try:
            amount = Decimal(amount)
        except:
            response.flash = T('Ошибка в величине')
            return dict(h = DIV(h, _class='container'))
        
        if man.id == man_in.id:
            response.flash = T('Сам себе')
            
        if amount <= 0:
            response.flash = T('Ошибка в величине')
        else:
            import account
            response.flash = account.try_send(db, man, cash, man_bal, man_in, amount, request.now, mess)
            
    elif form.errors:
        response.flash = CENTER('Check errors')
    else:
        ##response.flash = CENTER('please fill the form')
        pass
    
    return dict(h = DIV(h, _class='container'))

def in_btc_rules():
    h=CAT(
        H4(T('Оплаты крипто-имуществом (криптовалютой)')),
        UL(
            SPAN(T('Используйте клиент-кошелек для биткоинов'),
                A(B(' MultiBit.org '), _href='http://MultiBit.org', _target='_blank', _class='white'), ' ', T('или'), ' ',
                T('любой другой "лёгкий" или "тонкий" кошелек с официального сайта'),
                A(B(' Bitcoin.org '), _href='http://bitcoin.org/choose-your-wallet', _target='_blank', _class='white'),
                '-', T('такие кошельки не требуют больших ресурсов диска и памяти, достаточно 100Мб  дискового пространства.')),
            SPAN(T('Купите биткоины например на сервисе'),
                A(B(' 7Pay.in'), _href='http://7pay.in/to_buy', _target='_blank', _class='white')),
            SPAN(T('Нажмите на зелененькую стрелочку с кругляшком ниже и на открывшейся странице оплаты выберите "Получить адрес для платежа". После чего в запустившемся клиенте биткоина совершить платеж.')),
            SPAN(T('Вернитесь сюда обратно, нажав на "Заказ" на странице оплаты.')),
            )
        )
    return h

def in_btc():
    man_id = session.man_id
    if not man_id:
        return 'session error 1'
    man_bal_id = request.args(0)
    if not man_bal_id:
        return 'empty man_bal_id'
    man_bal = db.man_bals[ man_bal_id ]
    if not man_bal:
        return 'empty man_bal'
    if man_bal.man_id != man_id:
        return 'session error 2'
    
    man = db.men[ man_bal.man_id ]
    if not man:
        return 'error man'
    
    cash = db.cash[ man_bal.cash_id ]
    if not cash:
        return 'error cash'
    
    if cash.system_id != myconf.take('cash.bitcoin_id', cast=int):
        return T('В разработке')

    if not man_bal.dep_bill or len(man_bal.dep_bill) < 2:
        ## make a bill on LITE.cash
        
        url = 'http://lite.cash/api_bill/make.json/325?order=%s' % man.ref_key
        #print url
        #return url

        from gluon.tools import fetch
        resp = fetch(url)
        #print resp
        import gluon.contrib.simplejson as sj
        if not resp[:2].isdigit():
            # если тут не число - значит ошибка
            res = sj.loads(resp) # {'bill': bill_id }
            err = res.get('error')
            if err:
                return dict(err=err)

        ## bill_id, _, skey = resp.partition('.')
        man_bal.update_record(dep_bill = resp)

    redirect('http://lite.cash/bill/show/' + man_bal.dep_bill)

def out():
    man_id = session.man_id
    if not man_id:
        return 'session error 1'
    man_acc_id = request.args(0)
    if not man_acc_id:
        return 'empty man_acc_id'
    man_acc = db.man_accs[ man_acc_id ]
    if not man_acc:
        return 'empty man_acc'
    man_bal = db.man_bals[ man_acc.bal_id ]
    if not man_bal:
        return 'error man_bal'

    if man_bal.man_id != man_id:
        return 'session error 2'
    
    man = db.men[ man_bal.man_id ]
    if not man:
        return 'error man'
    
    cash = db.cash[ man_bal.cash_id ]
    if not cash:
        return 'error cash'
    
    response.title=T('Вывод средств')
    response.not_show_function = True

    if cash.system_id == myconf.take('cash.bitcoin_id', cast=int):
        return dict(h = DIV(H2(T('В разработке')), _class='container'))
    elif cash.system_id == myconf.take('cash.datachain_id', cast=int):
        h = CAT(H2(T('Вывод долей по проекту')),
                P(T('Доли по проекту распределяются в генесиз блоке при запуске среды в соответствии с общим числом подписчиков и их вложений. Управляющие единицы (правовые единицы) начиляются автоматически и Вы становитесь привилегированным участником среды с правом собирать (майнить, форжить) блоки с частотой, соответствующей Вашей величине доли в проекте.')),
               )
        return dict(h = DIV(h, _class='container'))
    elif cash.system_id != myconf.take('cash.datachain_id_id', cast=int):
        return dict(h = DIV(H2(T('В разработке')), _class='container'))


    return dict(h = DIV(H2(T('В разработке')), _class='container'))

def in_erm():
    error, man, cash, man_bal = check_args(request, session, cash_system_id = None)
    if error:
        return dict(h = H1(error))
    
    response.title=T('Пополнение баланса')
    response.not_show_function = True
    
    return dict(h = DIV(H2(T('В разработке')),
                        _class='container'))

    h = CAT(H1(T('Пополнение %s') % cash.name),
            P(XML(cash.descr))
           )
    return dict(h = DIV(h, _class='container'))

def in_wait():
    response.title=T('Пополнение баланса')
    response.not_show_function = True

    return dict(h = DIV(H2(T('В разработке')), 
                        _class='container'))

    error, man, cash, man_bal = check_args(request, session, cash_system_id = None)
    if error:
        return dict(h = H1(error))
    
    h = CAT(H1(T('Пополнение %s') % cash.name),
            P(XML(cash.descr))
           )
    return dict(h = DIV(h, _class='container'))


def exchange():
    error, man, cash_from, man_bal_from = check_args(request, session, cash_system_id = None)
    if error:
        return dict(h = H1(error))
    
    response.title=T('Обмер ресурса')
    response.not_show_function = True
    
    if cash_from.as_goods:
        return dict(h = DIV(H2(T('Этот актив невозможно обменять!')), _class='container'))

    img_system_path = cash_from.img or cash_from.name
    img_system_path = img_system_path and img_system_path + '.png'
    

    h = CAT(H1(T('Вы желаете обменять %s') % cash_from.name),
            P(XML(cash_from.descr)),
            H3(T('Ваш баланс'),': ', man_bal_from.bal, img_system_path and IMG(_src=URL('static', 'images/currs/' + img_system_path), _style='height:40px') or '')
           )
    cash_select = []
    for item in db((db.cash_system.used==True)
                   & (db.cash_system.id==db.cash.system_id)
                   & (db.cash.used==True)
                   & (db.rates.cash1_id == cash_from.id)
                   & (db.rates.cash2_id == db.cash.id)
                  ).select(orderby = db.cash.name):
        if item.cash.id == cash_from.id:
            continue
        ##print item
        cash_select.append(OPTION(SPAN(item.cash_system.name, ': ', item.cash.name, ' ',
                     ' x', item.rates.val,
                     not item.cash.unlimited and (' < %s' % item.cash.own_bal) or ''), _value = item.cash.id))
    
    form_exch = FORM( #H3(T('Выберите направление обмена')),
                    LABEL(T('Сколько отдаёте'), ' ', cash_from.name, ':'),' ',
                    INPUT(_name='amo_from', requires=IS_NOT_EMPTY()), BR(),
                    LABEL(T('Что Вам нужно'),':'),' ', SELECT(cash_select, _name='cash_to_id'), BR(),
                    INPUT(_type='submit', _class='btn btn-' + CLRS_btn))

    h += form_exch

    if form_exch.accepts(request, session, keepvalues=True):
        try:
            amo_from = Decimal(form_exch.vars.amo_from)
        except:
            response.flash = T('ошибка в количестве')
            return dict(h = DIV(h, _class='container'))
            
        if amo_from > man_bal_from.bal:
            response.flash = CENTER('Превышен баланс средств')
            return dict(h = DIV(h, _class='container'))
            
        cash_to_id = form_exch.vars.cash_to_id
        cash_to = db.cash[ cash_to_id ]
        if not cash_to:
            response.flash = CENTER('cash out error')
            return dict(h = DIV(h, _class='container'))
            
        ##print cash_in.id, cash_out.id
        ## SEEK ANEW!
        rate = db((db.rates.cash1_id == cash_from.id)
                & (db.rates.cash2_id == cash_to.id)).select().first()
        if not rate:
            response.flash = T('Курс не найден, попробуйте позже')
        elif rate.val == None or rate.val <= 0:
            response.flash = T('Обмен уже невозможен')
        else:
            rate_val = rate.val
            man_bal_to = db((db.man_bals.man_id == man.id)
                    & (db.man_bals.cash_id == cash_to_id)).select().first()
            if not man_bal_to:
                man_bal_to_id = db.man_bals.insert( man_id = man.id, cash_id = cash_to_id)
                man_bal_to = db.man_bals[ man_bal_to_id ]
            amo_to = rate_val * amo_from
            if not cash_to.unlimited and amo_to > cash_to.own_bal:
                amo_to = cash_to.own_bal
                amo_from = amo_to / rate_val
            import account
            account.update_bal_exchange(db, man_bal_from, amo_from, man_bal_to, amo_to, request.now)
            response.flash = T('Купили %s[%s] по курсу %s за %s[%s]') % (amo_to, cash_to.name, rate_val, amo_from, cash_from.name)
            
    elif form_exch.errors:
        response.flash = CENTER('Check errors')
    else:
        ##response.flash = CENTER('please fill the form')
        pass

    return dict(h = DIV(h, _class='container'))

def index():
    response.title=T('Балансы ресурсов')
    response.not_show_function = True

    man_id = session.man_id
    if not man_id:
        redirect(URL('cabinet','index'))
        
    man = db.men[ man_id ]
    if not man:
        redirect(URL('cabinet','index'))
        
    datachain_id = myconf.take('cash.datachain_id', cast=int)
    bitcoin_id = myconf.take('cash.bitcoin_id', cast=int)

    icon_gift = XML('<i class="fa fa-gift", style="color:#b00092;"></i>')
    icon_income = XML('<i class="fa fa-circle", style="color:#77ea00;"></i><i class="fa fa-share", style="margin-left: -1.5em;"></i>')
    icon_exchange = XML('<i class="fa fa-random", style=""></i>')
    icon_send = XML('<i class="fa fa-play-circle", style=""></i>')
    icon_outcome = XML('<i class="fa fa-circle", style="color:#77ea00;"></i><i class="fa fa-share", style="margin-left:-0.4em;"></i>')
    
    h = CAT(H1(T('Балансы')))
    h += P('*', T('Посмотрите инструкцию по работе с балансами на'), ' ',
                  A('YouTube.com', TAG.i(_class='fa fa-youtube-play', _style='font-size:1.5em'),
                    _href='https://youtu.be/Qkt7eC8SDxI', _class='white', _target='blank'),
                   ' ', T('или загрузить как файл в хорошем качестве'),' ',
                  A('tutor-bals.wmv', _href=URL('static', 'video/tutor-bals.wmv'), _class='white'),
                 '.')

    odd = True
    viewed = {}
    max_rec_count = 5
    rec_count = 0
    for rec in db(
            (
                (man_id == db.man_bals.man_id)
                & (db.man_bals.id == db.man_bal_txs.in_id )
            ) | (
                (man_id == db.man_bals.man_id)
                & (db.man_bals.id == db.man_bal_txs.out_id )
            )
            ).select(orderby=~db.man_bal_txs.created_on, limitby=(0, max_rec_count*2 + 1)):
        
        if rec.man_bal_txs.id in viewed:
            # not show duplicates
            continue
            
        if rec_count > max_rec_count:
            # duplicates ignore in counter
            break
        rec_count += 1
        
        viewed[rec.man_bal_txs.id] = True
        odd = not odd
        out_id = rec.man_bal_txs.out_id
        in_id = rec.man_bal_txs.in_id
        acc_id = rec.man_bal_txs.acc_id
        if not out_id:
            if rec.man_bal_txs.amo_out == -1:
                ## GIFT
                type_text = icon_gift
                out_text = ''
            else:
                type_text = icon_income
                out_text = rec.man_bal_txs.op_id or ''
                
            amo_in = rec.man_bal_txs.amo_in
            man_bal_in = db.man_bals[ in_id ]
            cash_in = db.cash [ man_bal_in.cash_id ]
            system_in = db.cash_system [ cash_in.system_id ]
            in_text = ('+%s ' % amo_in) + system_in.name + ': ' + cash_in.name

        elif not in_id or acc_id:
            ## withdraw
            type_text = icon_outcome
            amo_out = rec.man_bal_txs.amo_out
            man_bal_out = db.man_bals[ out_id ]
            cash_out = db.cash [ man_bal_out.cash_id ]
            system_out = db.cash_system [ cash_out.system_id ]
            acc = db.man_accs[ acc_id ]
            out_text = ('+%s ' % amo_out) + system_out.name + ': ' + cash_out.name
            out_text = (acc and acc.acc or '') + ' ' + (rec.man_bal_txs.op_id or '')
        else:
            amo_out = rec.man_bal_txs.amo_out
            man_bal_out = db.man_bals[ out_id ]
            cash_out = db.cash [ man_bal_out.cash_id ]
            system_out = db.cash_system [ cash_out.system_id ]
            amo_in = rec.man_bal_txs.amo_in
            man_bal_in = db.man_bals[ in_id ]
            if man_bal_out.cash_id == man_bal_in.cash_id:
                # SEND same CASH
                type_text = icon_send
                if man_bal_in.man_id == man_id:
                    ## ME IN
                    man_out = db.men [ man_bal_out.man_id ]
                    out_text = man_out.ref_key
                    in_text = (amo_in and ('+%s ' % amo_in) or '') + system_out.name + ': ' + cash_out.name
                else:
                    ## ME OUT
                    man_in = db.men [ man_bal_in.man_id ]
                    out_text = (amo_out and ('-%s ' % amo_out) or '') + system_out.name + ': ' + cash_out.name
                    in_text = man_in.ref_key
            else:
                # EXCHANGE
                type_text = icon_exchange
                cash_in = db.cash [ man_bal_in.cash_id ]
                system_in = db.cash_system [ cash_in.system_id ]
                out_text = ('-%s ' % amo_out) + system_out.name + ': ' + cash_out.name
                in_text = ('+%s ' % amo_in) +system_in.name + ': ' + cash_in.name
        h += DIV(
            DIV(type_text, SPAN(rec.man_bal_txs.created_on, _style='font-size:14px; font-family:initial;'), _class='col-sm-2'),
            DIV(out_text, _class='col-sm-5'),
            DIV(in_text, _class='col-sm-5'),
            _class='row' + (odd and ' odd' or ''))
        mess = rec.man_bal_txs.mess
        if mess and len(mess) > 0:
            h += DIV(
                DIV(mess, _class='col-sm-12'),
                _class='row' + (odd and ' odd' or ''))
    bals_tab = CAT()
    for cash_system in db(db.cash_system).select():
        cash_system_id = cash_system.id
        img_system_path = cash_system.img
        img_system_path = img_system_path and img_system_path + '.png'
        bals_tab += H2(cash_system.name, img_system_path and IMG(_src=URL('static', 'images/currs/' + img_system_path), _style='height:40px') or '', _id=cash_system.name)
        bals_tab += P(XML(cash_system.descr))

        for cash in db((db.cash.system_id == cash_system_id)
                          & (db.cash.used == True)
                      ).select():
            cash_id = cash.id
            
            man_bal = db((db.man_bals.man_id == man_id)
                          & (db.man_bals.cash_id == cash_id)).select().first()
            if not man_bal:
                man_bal_id = db.man_bals.insert(man_id = man_id, cash_id = cash_id)
                man_bal = db.man_bals[ man_bal_id ]

            if cash_system_id == myconf.take('cash.bitcoin_id', cast=int):
                fnct = 'in_btc'
                bals_tab += DIV(H4(T('Как сделать взнос биткоинами'),' - ',
                                A(B(T('ОПИСАНИЕ')), _href=URL('cab_bals','in_btc_rules'), _class='white', cid='in_btc_rules')),
                            _id='in_btc_rules')

            elif cash_system.inside:
                fnct = 'in_erm'
            else:
                fnct = 'in_wait'

            img_path = cash.img or cash.name
            img_path = img_path and img_path + '.png'

            bals_tab += DIV(
                DIV(H4(img_path and SPAN(IMG(_src=URL('static', 'images/currs/' + img_path), _style='height:40px'), ' ') or '', cash.name),
                    _class='col-sm-4'),
                DIV(
                    bitcoin_id == cash.system_id and 
                    A(icon_income,
                        _href=URL('cab_bals', fnct, args=[man_bal.id]),
                        _title=T('Пополнить'),
                        _class='btn btn-blue2 btn-fa',
                        _style='padding: 0em 0.6em;',
                        _onclick='$(this).addClass("disabled");$(this).children("i").addClass("fa-spin");'
                    ) or '',
                    cash.as_goods != True and A(icon_exchange,
                         _href=URL('cab_bals', 'exchange', args=[man_bal.id]),
                         _title=T('Обменять'),
                         _class='btn btn-for btn-fa',
                         _onclick='$(this).addClass("disabled");$(this).children("i").addClass("fa-spin");'
                    ) or '',
                    cash.unsend != True and A(icon_send,
                         _href=URL('cab_bals', 'send', args=[man_bal.id]),
                         _title=T('Послать'),
                         _class='btn btn-tre btn-fa',
                         _onclick='$(this).addClass("disabled");$(this).children("i").addClass("fa-spin");'
                    ) or '',
                    _class='col-sm-5'),
                DIV(H4(man_bal.bal > 0 and SPAN(' ', man_bal.bal) or ''), _class='col-sm-3'),
                _style='background-color: aliceblue;',
                _class='row'
                )
            bals_tab += P(XML(cash.descr))
            if cash.ref_gift and cash.ref_gift > 0:
                if cash.ref_gift < 1:
                    bals_tab += P('*', T('Реферальная награда'), ': ', cash.ref_gift * 100, '%')
                else:
                    bals_tab += P('*', T('Реферальная награда'), ': ', cash.ref_gift)


            accs = {}
            for acc in db(db.man_accs.bal_id == man_bal.id).select():

                accs[acc.acc] = acc

            if len(accs) > 0: # or cash.inside:

                accs_bals = CAT()
                for k, v in accs.iteritems():
                    sun_view = ''
                    #print k, v
                    sun = db((v.id == db.man_acc_goods.man_acc_id)
                             & (db.goods.id == 1)
                             & (db.goods.id == db.man_acc_goods.good_id)).select().first()
                    if sun:
                        sun_view = XML('<i class="fa fa-star" style="font-size:22px; color:#ff9100"></i>')

                    accs_bals += DIV(
                        DIV(INPUT(_name=k, _value=k, _style='width:22em;'), sun_view, _class='col-sm-8'),
                        DIV(
                            datachain_id == cash.system_id and 
                            A(icon_outcome,
                                 _href=URL('cab_bals', 'out', args=[v.id]),
                                 _title=T('Вывести'),
                                 _class='btn btn-fiv btn-fa',
                                 _onclick='$(this).addClass("disabled");$(this).children("i").addClass("fa-spin");'
                                ) or '',
                        _class='col-sm-1'),
                        DIV(v.amo_outcomed, _class='col-sm-3'),

                        HR(),
                        _style='background-color: blanchedalmond;',
                        _class='row')


                bals_tab += accs_bals

    h += bals_tab
    
    #h += DIV(H4(T('Как сделать взнос биткоинами'),' - ',
    #            A(B(T('ОПИСАНИЕ')), _href=URL('cab_bals','in_btc_rules'), _class='blue', cid='in_btc_rules')), _id='in_btc_rules')
    
    return dict( h = DIV(h, _class='container') )
