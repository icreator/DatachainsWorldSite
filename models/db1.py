# coding: utf8

UNIQ = True

LOCAL_CASH_NAME = 'DATACHAINS'

from decimal import Decimal

db.define_table('crew_kind',
    Field('name', length=30),
    format='%(name)s',
    )

# подписка для клиентов
db.define_table('crew',
    Field('kind', db.crew_kind),
    Field('btc', length=40, label=T('Биткоин адрес')),
    Field('fio', length=100),
    Field('pic', 'upload'),
    Field('pic_url'),
    Field('email', length=60, unique=True,
        requires = [IS_EMAIL(error_message=T('Неправильный емайл!')),
                    IS_NOT_IN_DB(db, 'crew.email')]),
    Field('linkedin', length=100),
    Field('vk', length=100),
    Field('skills', 'text'),
    Field('contacts','text'),
    Field('say','text'),
    format='%(email)s',
    )

# дистрибьюторы
db.define_table('distrib',
    Field('name', length=100),
    Field('url'),
    Field('pic_url'),
    Field('used','boolean', default=True), # ON - OFF
    Field('info','text'),
    format='%(name)s',
    )

db.define_table('its',
    Field('ref_', 'integer'),
    Field('name', length=100),
    Field('inpay_addr', length=60, comment='coin address'),
    Field('descr', 'text'), ## widget=ckeditor.widget),
    Field('on_created', 'date'),
    format='%(name)s',
    )
db.its.ref_.requires = IS_EMPTY_OR(IS_IN_DB(db, 'its.id', '%(name)s'))

####
db.define_table('cash_system',
    Field('used','boolean', default=True), # ON - OFF
    Field('inside','boolean', default=True, comment='Inside system - local service cash'),
    Field('name','string', length=60, default = LOCAL_CASH_NAME, comment='PayPal, Yandex, ...'),
    Field('img','string', length=20, comment='for image static/images/cash'),
    Field('descr','text'),
    Field('url','string', length=40),
    format = '%(name)s',
    )

db.define_table('cash',
    Field('system_id', db.cash_system, default = 1),
    Field('used','boolean', default=True), # ON - OFF
    Field('name','string', length=20, comment='USD, BTC'),
    Field('unlimited','boolean', default=False, comment='own_bal may be < 0'), # ON - OFF
    Field('as_goods','boolean', default=False, comment='True - can\'t convert back to money - it is goods'), # ON - OFF
    Field('unsend','boolean', default=False, comment='True - can\'t send to other user'), # ON - OFF
    Field('accuracy','integer', default=8),
    Field('full_name', 'string', length=30, unique=UNIQ, compute=lambda r: '%s %s' % (r['system_id'], r['name'])),
    Field('img','string', length=20, comment='for image static/images/cash/*.png'),
    Field('descr','text'),
    Field('ref_gift', 'decimal(8,3)', default = Decimal(0), comment='Gift for referal man. if < 1 = as koeff'),
    Field('def_amo', 'decimal(8,3)', default = Decimal(1), comment='default amount'),
    Field('bal', 'decimal(16,8)', default = Decimal(0), comment='total balance of users'),
    Field('own_bal', 'decimal(16,8)', default = Decimal(0), comment='total balance owned by service'),
    format = '%(full_name)s',
    )

db.define_table('men',
    Field('email', 'string', length=60, unique=UNIQ,
          requires=[IS_EMAIL(), IS_NOT_IN_DB(db, 'men.email')],
          #requires=IS_EMPTY_OR(IS_EMAIL(),
          ),
    Field('phone', 'string', length=20, unique=UNIQ,
          requires=IS_NOT_IN_DB(db, 'men.phone'),
          #requires=IS_EMPTY_OR(IS_EMAIL(),
          ),
    Field('name','string', length=30, comment='Name'),
    Field('social1', 'string', comment='url to cosial post 1'),
    Field('social2', 'string', comment='url to cosial post 2'),
    Field('bonus', 'integer', default=0, comment='bonus for socisl piar'),
    Field('investor_level', 'integer', default=0),
    Field('ref_man','string', length=10, readable=True, writable=False, comment='referal man'),
    Field('ref_key','string', length=10, unique=UNIQ, readable=True, writable=False, comment='referal key'),
    format = '%(email)s',
    )
#db.executesql('CREATE INDEX IF NOT EXISTS men_ref_idx ON men (ref_key);')

# ключи доступа сюда запминаем - только надо их удалять периодически
db.define_table('man_keys',
    Field('man_id', db.men),
    Field('created_on', 'datetime', default=request.now ),
    Field('temp_key','string', length=100, unique = UNIQ),
    )
db.define_table('man_bals',
    Field('man_id', db.men, readable=False, writable=False),
    Field('cash_id', db.cash),
    Field('bal', 'decimal(16,8)', readable=False, writable=False, default = Decimal(0), comment='balance for this money'),
    Field('dep_bill', 'string', length=40, readable=False, writable=False, comment='bill_id in that money system for deposit'),
    Field('dep_incomed', 'decimal(16,8)', default = Decimal(0), comment='total incomed amount from this BILL'),
    format = '%(man_id)s %(cash_id)s',
    )

db.define_table('man_accs',
    Field('bal_id', db.man_bals),
    Field('acc','string', length=60, requires=IS_NOT_EMPTY(), comment=T('wallet address')),
    Field('amo_outcomed', 'decimal(16,8)', default = Decimal(0), comment='outcomed amount'),
    format = '%(id)s %(acc)s',
    )
#db.executesql('CREATE INDEX IF NOT EXISTS man_accs_idx ON man_accs (acc);')


db.define_table('goods',
    Field('name','string', length=60, requires=IS_NOT_EMPTY()),
    Field('cnt', 'integer', default=0),
    format = '%(id)s %(name)s',
    )
db.define_table('man_acc_goods',
    Field('man_acc_id', db.man_accs),
    Field('good_id', db.goods),
    Field('cnt', 'integer', default=0),
    format = '%(id)s',
    )

###
### bal -> nal or bal -> external acc
db.define_table('man_bal_txs',
    Field('in_id', # db.man_bals), # if empty - as withdraw to ACC_ID
        requires = IS_EMPTY_OR(IS_IN_DB(db, 'man_bals.id', '%(man_id)s %(cash_id)s'))
        ),
    Field('out_id', # db.man_bals), # if empty - as incomed payment
        requires = IS_EMPTY_OR(IS_IN_DB(db, 'man_bals.id', '%(man_id)s %(cash_id)s'))
        ),
    Field('acc_id', # db.man_accs),
        requires = IS_EMPTY_OR(IS_IN_DB(db, 'man_accs.id', '%(bal_id)s')),
        comment='if not None - it is the external operation'
        ),
    Field('op_id', 'string', length=70, ## requires=IS_NOT_EMPTY(),
          comment=T('transaction id if it is external')),
    Field('amo_in', 'decimal(16,8)', default = Decimal(0), comment=T('transaction amount')),
    Field('amo_out', 'decimal(16,8)', default = Decimal(0), comment=T('transaction amount')),
    Field('created_on', 'datetime', default=request.now ),
    Field('mess', 'string'),
    )

# тут сделаем уникальный сложную проверку
db.man_bals.cash_id.requires=IS_IN_DB(db, 'cash.id', '%(name)s',
      _and = IS_NOT_IN_DB(db(db.man_bals.man_id==request.vars.man_id), 'man_bals.cash_id'))

db.define_table('rates',
    Field('cash1_id', db.cash),
    Field('cash2_id', db.cash),
    Field('val', 'decimal(16,8)', default=1),
    Field('created_on', 'datetime', default=request.now ),
    format = '%(cash1_id)s->%(cash1_id)s',
    )

db.define_table('pubkeys',
    Field('pubkey', 'string', length=50, requires=IS_NOT_EMPTY()),
    Field('fio', 'string'),
    format = '%(id)s %(pubkey)s',
    )

############################
############################
## TRUNCATE
try:
    if db(db.man_bal_txs).isempty():
        db.man_bal_txs.truncate()
    if db(db.man_accs).isempty():
        db.man_accs.truncate()
    if db(db.man_bals).isempty():
        db.man_bals.truncate()
    if db(db.cash).isempty():
        db.cash.truncate()
    if db(db.cash_system).isempty():
        db.cash_system.truncate()
except:
    pass

#####################################################
## sets
if db(db.cash_system).isempty():
    for r in [
            dict(name='DATACHAINS', url='http://datachains.world', inside = True,
                 descr='Стартап на инновации блокчейн 3.0'),
            dict(name='Bitcoin', url='http://bitcoin.org', inside = False,
                 descr='Международная общественная криптовалюта'),
            dict(name='PayPal', url='http://paypal.com', inside = False,
                 descr='Электронные деньги'),
            dict(name='Yandex', url='http://money.yandex.ru', inside = False,
                 descr='Электронные деньги'),
            dict(name='BANK A', inside = False,
                 descr='Банковский безналичный перевод. Учет оплааты ручной - для справки обратитесь к администрации проекта',
                 ),
        ]:
        db.cash_system.insert( **r )

if db(db.cash).isempty():
    for r in [
            dict(system_id = 1, name='RUB', unlimited = True, accuracy = 2, def_amo = 5000,
                 descr='Внутренняя учётная единица для рублей, внесенных участником на свой локальный счёт. Вы можете обмениваться ею внутри сервиса между другими участниками или оплачивать ею другие программы проекта.'),
            dict(system_id = 1, name='E-Share A', unlimited = True, as_goods = True, unsend = True,
                 descr='Акция раннего инвестора в блокчейн-стартапе (все проекты)'),
            dict(system_id = 1, name='E-Share B', unlimited = True, as_goods = True, unsend = True,
                 descr='Акция инвестора в блокчейн-стартапе (все проекты)'),
            dict(system_id = 1, name='E-Share C', unlimited = True, as_goods = True, unsend = True,
                 descr='Акция позднего инвестора в блокчейн-стартапе (все проекты)'),
            dict(system_id = 1, name='E-Векселя', unlimited = True, as_goods = True, unsend = True,
                 descr='Акция раннего инвестора в блокчейн-среде по учету векселей и других обязательств - 30%',
                 ),
            dict(system_id = 1, name='E-Партии', unlimited = True, as_goods = True, unsend = True,
                 descr='Акция раннего инвестора в блокчейн-среде по учету членов партий и их голосований - 30%',
                 ),
            dict(system_id = myconf.take('cash.bitcoin_id', cast=int), name='BTC',
                 descr='Биткоины, учет оплаты автоматический',
                 def_amo=0.1),
            dict(system_id = myconf.take('cash.yandex_id', cast=int), name='РУБ.Я', accuracy=2, img='RUB',
                 descr='Электронные деньги',
                 def_amo=10000 ),
            dict(system_id = myconf.take('cash.paypal_id', cast=int), name='USD.P', accuracy=2,
                 descr='Электронные деньги',
                 def_amo=100 ),
            #dict(system_id = myconf.take('cash.bank_a_id', cast=int), name='USD', accuracy=2,
            #     descr='Банковский безналичный перевод. Учет оплааты ручной - для справки обратитесь к администрации проекта',
            #     def_amo=100 ),
            #dict(system_id = myconf.take('cash.bank_a_id', cast=int), name='РУБ', accuracy=2,
            #     descr='Банковский безналичный перевод. Учет оплааты ручной - для справки обратитесь к администрации проекта',
            #     def_amo = 10000 ),
        ]:
        #print r
        db.cash.insert( **r )
