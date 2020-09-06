# -*- coding: utf-8 -*-
# попробовать что-либо вида

datachain_id = myconf.take('cash.datachain_id')


def index():

    SUN7B_ID = request.args(0) or 18
    SUN7F_ID = request.args(1) or 19

    session.forget(response)
    response.title=T('Зажги Солнце блокчейна')
    response.not_show_function = True

    datachains_cash_system = db.cash_system[datachain_id]
    cash_f = db.cash[SUN7F_ID]
    cash_b = db.cash[SUN7B_ID]

    man_id = session.man_id
    man = man_id and db.men[ man_id ]

    man_bal_f = man and db((db.man_bals.man_id == man_id)
                & (db.man_bals.cash_id == SUN7F_ID)).select().first()
    man_bal_b = man and db((db.man_bals.man_id == man_id)
                & (db.man_bals.cash_id == SUN7B_ID)).select().first()

    acc_not_setted = True
    
    hh = ''
    if man:
        if man_bal_f or man_bal_b:
            man_accs_f = man_bal_f and db(db.man_accs.bal_id == man_bal_f.id).select()
            man_accs_b = man_bal_b and db(db.man_accs.bal_id == man_bal_b.id).select()
            if man_accs_f and man_accs_b and (len(man_accs_f) > 0 or len(man_accs_b) > 0):
                hh = CAT(SPAN(BR(), '***', XML(T('<span class="orange_b">Кстати</span>, у Вас уже заданы счета')), ':', BR()))
                if man_accs_b and len(man_accs_b) > 0:
                    hh += SPAN(T('для программы'), ' ', B(cash_b.name), BR())
                    for rec in man_accs_b:
                        hh += SPAN((rec.acc), BR())
                if man_accs_f and len(man_accs_f) > 0:
                    hh += SPAN(T('для программы'), ' ', B(cash_f.name), BR())
                    for rec in man_accs_f:
                        hh += SPAN(rec.acc, BR())

                acc_not_setted = False
    ol = OL(
            [P(
               XML(T('Для этого <span class="orange_b">скачайте</span> и <span class="orange_b">запустите</span> программу-клиент нашей блокчейн среды')),': ', BR(),
               A(B(T('Загрузить')), _href=URL('cabinet','download'), _target='blank', _class='blue')),
            P(XML(T('Затем <span class="orange_b">получите</span> адрес любого счета в своем кошельке, как это сделать описано на странице загрузки программы')),': ', BR(),
               A(B(T('Счета, аккаунты')), _href=URL('cabinet','download#accounts'), _target='blank', _class='blue')),
            P(XML(T('После чего <span class="orange_b">внесите</span> выбранный счёт в своём личном кабинете в разделе "Добавить Счёт для вывода средств", выбрав например Систему Средств:')),
               ' ', B(datachains_cash_system.name, ': ', cash_b.name), ' ',  T('или'), ' ',
               B(datachains_cash_system.name, ': ', cash_f.name), BR(),
               A(B(T('Личный кабинет')), _href=URL('cabinet','index#pers'), _target='blank', _class='blue'), BR(),
               '***', T('В результате чего этот счёт появится на странице балансов в соответствующем разделе денег.'), BR(),
               B(T('Внимание! У Вас еще не задан счёт для этой программы!')) if man and acc_not_setted else hh,
               ),
            ])

    h = CAT()
    h += DIV(
        DIV(
            CENTER(H2(XML(T('Как вступить в программу %s') % A(cash_b.name, _href=URL('sun_a','index'), _class='white')))),
            H4(T('В первую очередь необходимо задать счёт в личном кабинете для начисления учётных единиц по этой программе'),':'),
            ol,
        _id='list2',
        _class='container'),
        _style='background-color:#fff; color:#222; padding-bottom:30px;')

    if acc_not_setted:
        pass

    
    h += DIV(
        H4(T('Теперь нужно оплатить взнос в выбранную программу:')),
        OL([
            P(XML(T('<span class="orange_b">Пополните</span> внутренний счёт биткоинами на странице "Балансы", - <span class="orange_b">найдите</span> это Денежное Средство и нажмите кнопку "Пополнить"')),
              XML('<i class="fa fa-circle" ,="" style="color:#77ea00;"></i><i class="fa fa-share" ,="" style="margin-left: -1.5em;"></i>'), '.', BR(),
                 T('Перейти в'), ' ', A(B(T('Балансы')), _href=URL('cab_bals','index#DATACHAINS'), _target='blank', _class='blue')),
            P(XML(T('Или <span class="orange_b">пополните</span> внутренний рублевый счёт через дистрибьюторов')), ':', BR(),
                 A(B(T('Дистрибьюторы')), _href=URL('distr','list'), _target='blank', _class='blue')),
            P(XML(T('Теперь в своих балансах найдите раздел %s и <span class="orange_b">выберите</span> валюту, которой хотите оплатить взнос, и нажмите кнопку "конвертировать"') % datachains_cash_system.name),
                 ' ', XML('<i class="fa fa-random"></i>'), '.', BR(),
                 T('Перейти в'), ' ', A(B(T('Балансы')), _href=URL('cab_bals','index#DATACHAINS'), _target='blank', _class='blue')),

            P(XML(T('Далее, на страничке обмена <span class="orange_b">задайте</span> величину перевода, <span class="orange_b">выберите</span> нужную программу, например "%s" или "%s", и совершите его.') % (B(datachains_cash_system.name + ': ' + cash_b.name),
                     B(datachains_cash_system.name + ': ' + cash_f.name))
                 ))
                ],
              _start=4),
            BR(),
            P(B(T('Подсказка')),': ', T('Если напрямую с внутреннего счёта для биткоинов нельзя конвертировать средства в нужную программу или деньги, попробуйте это сделать через рублевый счёт, предварительно сконвертировав биткоины с внутреннего счёта в рубли с помощью кнопки "Конвертирровать".')),
            P(B(T('Подсказка')),': ', T('Вы можете скооперироваться со своими друзьями, собрать совместно нужную сумму для получения уровня "Солнца" и потом сделать своих кооператоров своими подписчиками 1-го уровня. Они получат возможность тоже собирать под собой приглашенных до максимального уровня Вашей сети. Также Вы будете чеканить блоки на общий кооперативный котёл. Передать средства другому участнику можно по его номеру телефона, емайлу или коду клиента. На странице "Балансы" нажмите на кнопку "Передать"'), ':', XML('<i class="fa fa-play-circle"></i>'),
                 ),
        _id='list2',
        _class='container')

    
    return dict(h = h)

    return dict(message="hello from pay_cab.py")
