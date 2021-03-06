# -*- coding: utf-8 -*-
# try something like

if False: # for IDEA
    from gluon import *
    from db import *
    import auth
    from menu import *
    request = current.request
    response = current.response
    session = current.session
    cache = current.cache
    T = current.T
    pass


SUN7_ID = 18

FULL_PROJECT_NAME = 'DATACHAINS.World blockchain 3.0 project'

## CASH ID for list
E_SHARES_ID = 9
E_BIZ_ID = 12 # E-Biz
E_SOC_ID = 13

CLRS_btn = '-tre btn-lg pull-right'
CLRS_btn2 = '-tre btn-lg pull-right'

def u(h, url, cls='col-sm-4'):
    return DIV(DIV(P(h, _class='btn_mc2'), _class='btn_mc1', _onclick="location.href='%s'" % url), _class='btn_mc ' + cls)

def set_session(sess, man):
    sess.man_id = man.id
    sess.man_name = man.name or man.email

# confirm - подтверждение по почте получено
def connect_conf():
    if session.man_id:
        man = db.men[ session.man_id ]
        if man:
            db(db.man_keys.man_id == man.id).delete()
            redirect(URL('cabinet', 'index'))

    key = request.args(0)
    if not key:
        return dict(h = T('Пустой Ключ'))
    
    if key != session.mail_connect_key:
        rec = db(db.man_keys.temp_key == key).select().first()
        if rec:
            del db.man_keys[ rec.id ]
        return dict(h = T('неверная сессия'))
        
    rec = db(db.man_keys.temp_key == key).select().first()
    if not rec:
        return dict(h = T('Такой Ключ не найден'))
    
    man = db.men[ rec.man_id ]
    del db.man_keys[ rec.id ]
    if not man:
        return dict(h = T('Человек не найден'))
    
    set_session(session, man)
    redirect(URL('cabinet','index'))

def mmm(erm):
    import smtplib
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('ipo.polza@gmail.com','powered_sisi')
    smtpObj.sendmail("ipo.polza@gmail.com","icreator@mail.ru","go to bed!", "asdasdsad")
    smtpObj.quit()
    return

    
def mail_connect(man, req):
    #from gluon.tools import Mail
    import random
    import string
    key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(40))
    # запомним ключ посланный - только его принимаем
    db(db.man_keys.man_id == man.id ).delete()
    db.man_keys.insert( man_id = man.id, temp_key = key )
    session.mail_connect_key = key
    
    url = URL('cabinet', 'connect_conf', args=[key], scheme=True, host=True)
    #context = dict( key = key, man = man.name, url = url )
    #mess = response.render('man/mail_connect.html', context)
    mess = CAT(
            H2(T('Привет'), ', ', man.name or man.email, '!'),
            BR(),
            P(T('Вы или кто-то запросил подключение к Персональному Кабинету на %s') % req.env.http_host),
            P(T('Для подключения к сайтк нажмите на')),
            CENTER(H2(A(B(T('Эту Ссылку')), _href=url))),
            BR(),
            P(T('Если это не Вы запрашивали подключения, то просто игнорируйте данное письмо.')),
            BR(),
            P(T('Администрация проекта'), ' ', B(FULL_PROJECT_NAME),'.'),
        
        )
    #to_addrs = ['kentrt@yandex.ru','icreator@mail.ru']
    h = CAT(P(B(T('Письмо послано для [%s]. На всякий случай проверьте так же ящик для спама.') % man.email)))
    if req.is_local:
        h += DIV(mess)
    else:
        mail_sets = myconf.take('email')

        from gluon.tools import Mail
        mail = Mail()
        mail.settings.server = mail_sets['server']
        mail.settings.sender = mail_sets['sender']
        mail.settings.login = mail_sets['login']
        mail.send(
              #to = [man.email, 'icreator@mail.ru'],
              to = [man.email],
              subject = T('Подключение к %s') % APP_NAME,
              message = '<html>%s</html>' % mess )
    
    return h

def connect_form(res=''):
    if session.man_id:
        ##redirect(URL('cabinet','index'))
        return
    
    form_to_view = True
    form = FORM(
        DIV(
            DIV(LABEL(T('Введите Ваш Е-майл'),': '), _class='col-sm-4'),
            DIV(INPUT(_name='em', requires=IS_EMAIL()), _class='col-sm-8'),
        _class = 'row'),
             INPUT(_type='submit', _class='btn btn-' + CLRS_btn))
    if form.accepts(request, session, keepvalues=True):
        man = db(db.men.email == form.vars.em).select().first()
        form_to_view = False
        if not man:
            import time
            time.sleep(2)
            import random
            import string
            while True:
                ref_key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(10))
                if not db(db.men.ref_key == ref_key).select().first():
                    break
            man_id = db.men.insert(email = form.vars.em, ref_key = ref_key, ref_man = GIFT_CODE) ## , name = form.vars.mm, 
            db.commit()
            man = db.men[ man_id ]


        #response.flash = CENTER(B(T('Email with access key send to Your. Check email and spam folder')))
        response.flash = CENTER(B(T('Письмо выслано на Ваш Емэйл. На всякий случай проверьте папку для спама.')))
        res = mail_connect(man, request)
    elif form.errors:
        response.flash = CENTER(T('Проверьте данные, обнаружена ошибка!'))
    else:
        ##response.flash = CENTER('please fill the form')
        pass
    
    h = DIV(H2(T('Подключение к Персональному Кабинету')),
            P(T('Для подключения введите Ваш емэйл и мы вышлем Вам ключ доступа'),'.'),
            BR(), form if form_to_view else '',
            P(T('Пожалуйста используйте броузер Google Chrome для корректной посылки письма. При этом сессия будет создана именно для этого броузера.')),
            res,
            BR(),
            _class='inv')
    
    return h

def disconnect():
    
    #return dict( h = (T('Sorry, email is busy')))
    session.man_id = session.man_name = None
    redirect(URL('cabinet', 'index'))
    
def form_accs_validate(f):
    if db((db.man_accs.bal_id == f.vars.bal_id)
          & (db.man_accs.acc == f.vars.acc)).select().first():
        f.errors.cash_id = T('Уже существует')
        response.flash = T('Данные внесены с ошибками')

def download():
    response.not_show_function = True
    man_id = session.man_id
    h = CAT()
    if not man_id:
        h += DIV(
            BR(),
            P(XML(T('Для получения новостей от проекта, сообщений об обновления просьба пройдите %s')
                    % A(B(T('Регистрацию')), _href=URL('cabinet', 'index'), _class='blue' ))),
            BR(),
            _class='container')

    h += DIV(
        H1('DATACHAINS ПРОДУКТЫ', _class='center'),
        P('Распределённая среда учета на технологии блокчейн 3.0 - денежных средств, активов, акций, голосований, товаров и услуг готовится к запуску! Вы можете стать её членом и получить начальные управляющие и рабочие единицы. Для этого скачайте клинет-кошелек и создайте свои счета.', BR()),
        P('*', T('Посмотрите инструкцию по установке'), ' ',
          A('YouTube.com', TAG.i(_class='fa fa-youtube-play', _style='font-size:1.5em'),
            _href='https://youtu.be/8WP4ysbCgiI', _class='white', _target='blank'),
           ' ', T('или загрузить как файл в хорошем качестве'),' ',
          A('tutor-bals.wmv', _href=URL('static', 'video/tutor-dload.wmv'), _class='white'),
         '.'),
        P(T('Внимание! Для работы нужен пакет'), ' ', A(B('Java 8'), _class='blue', _href='http://www.java.com/ru/', _target='blank')),
        P(A(B('ERM4 v.3.01.09'), _href=URL('static','files/ERM4.zip'),
            _class='blue'), ' - ', T('это БОЕВАЯ блокчейн среда 3-го поколения.')),
        P(A(B('ERM5 v.2.16.08'), _href=URL('static','files/ERM5.zip'), _class='blue'), ' - ', T('это пробная среда для обучения.')),
        P('Для получения учётных единиц, необходимых для внесения записей в среду, сообщите нам свой счёт в этой среде.'),
        P('Если синхронизация не происходит, загрузите последнюю версию с сайта и удалите базу блоков (папки /data и /dataBak).'),
        P('Просмотреть деятельнось в боевой среде ERM4 можно через веб-интерфейс',': ',
          A(B('Block Explorer ERM4 #1'), _class='blue', _href='http://54.194.119.240:9047/index/blockexplorer.html', _target='blank'),', ',
          A(B('Block Explorer ERM4 #2'), _class='blue', _href='http://185.146.168.226:9047/index/blockexplorer.html', _target='blank'),'.'),
        P('Просмотреть деятельнось в пробной среде ERM5 можно через веб-интерфейс',': ',
          A(B('Block Explorer ERM5 #1'), _class='blue', _href='http://54.194.119.240:9057/index/blockexplorer.html', _target='blank'),'.',
          A(B('Block Explorer ERM5 #2'), _class='blue', _href='http://185.146.168.226:9057/index/blockexplorer.html', _target='blank'),'.'),
        _class='container', _id='product')

    h += CAT(
        DIV(
            DIV(
                    H2('Установка для Windows', _class='center'),
                    P(T('Распакуйте скачанный архив в рабочую папку.')),
                    P(T('Запустите run.bat или ERM4.jar (или ERM5.jar для игровой версии). Если система выдаст предупреждение откройте расширенные настройки и разрешите запуск.')),
                    P(IMG(_src=URL('static', 'images/tutor/erm-start-1.png'))),
            BR(),
                    H2('Установка для Unix', _class='center'),
                    P(T('Распакуйте скачанный архив в рабочую папку.')),
                    P(T('Запустите run.sh или ERM4.jar (или ERM5.jar для игровой версии).')),
                    #P(IMG(_src=URL('static', 'images/tutor/erm-start-1.png'))),
            BR(),
                    H2('Установка для Mac', _class='center'),
                    P(T('Распакуйте скачанный архив в рабочую папку.')),
                    P(T('Запустите ERM4.jar (или ERM5.jar для игровой версии). Если система выдаст предупреждение что это незарегистрированная программа, то откройте контекстное меню (двойной клик на файле) и в нем выберие "Открыть".')),
                    P(IMG(_src=URL('static', 'images/tutor/mac-start-1.png'))),
                    P(T('Дальше жмём "Открыть"')),
                    P(IMG(_src=URL('static', 'images/tutor/mac-start-2.png'))),
            BR(),
                    H2(T('Описание')),
                    P(A(T('Дальнейшее описание'), _href=URL('bc3base', 'index'), _class='white')),
                    P(T('')),
                    _class='container', _id='product'),
            _style='background-color:#ddd; color:#222;padding-bottom:30px;',
            _class='row'),
            )
    return dict(h = h)

# class="fa fa-heart"
def fa_icons(fa_icon, val):
    h = CAT()
    for i in range(val or 0):
        h += TAG.i(_class='fa ' + fa_icon)
    return h


# заменить все не цифры и проверить длинну
import re
regular_phone = re.compile("\D")
def valid_phone(ph):
    str = regular_phone.sub("","%s" % ph)
    return str

def show_man(req, man):
    col1 = '3'
    col2 = '9'
    h = CAT(H1(T('Личный Кабинет'), _id='pers'))

    h += P('*', T('Посмотрите инструкцию по работе с балансами на'), ' ',
                      A('YouTube.com', TAG.i(_class='fa fa-youtube-play', _style='font-size:1.5em'),
                        _href='https://youtu.be/Qkt7eC8SDxI', _class='white', _target='blank'),
                       ' ', T('или загрузить как файл в хорошем качестве'),' ',
                      A('tutor-bals.wmv', _href=URL('static', 'video/tutor-bals.wmv'), _class='white'),
                     '.')

    h += DIV(
        DIV(T('Имя'), ': ', _class='col-sm-' + col1),
        DIV(man.name, _class='col-sm-' + col2),
        _class='row', _id='name')
    h += DIV(
        DIV(T('Уровень Инвестиций'), ': ', _class='col-sm-' + col1),
        DIV(B(man.investor_level or 0, _class='inv'), _class='col-sm-' + col2),
        _class='row')

    man_id = man.id
    if not IS_LOCAL and not DEVELOP and session.man_id != man_id:
        return

    ##
    session.man_name = man.name or man.email
    session.man_id = man_id
    
    h += H4(T('Личные данные'))
    h += DIV(
        DIV(T('Емэйл'), ': ', _class='col-sm-' + col1),
        DIV(B(man.email, _class='inv'), _class='col-sm-' + col2),
        _class='row')
    h += DIV(
        DIV(T('Сотовый телефон'), ': ', _class='col-sm-' + col1),
        DIV(B(man.phone, _class='inv'), _class='col-sm-' + col2),
        _class='row')
    h += H4(T('Реферальная система'))
    h += P(T('Каждый раз, когда реферал (пришедший по реферальной ссылке), оплачивает программы старта или делает другие платежи, наши инвесторы дарят Вам до 10% от суммы его платежа'),'. ',
          T('Размер награды можно увидеть на странице балансов под описанием локальной денежной единицы или внутренней программы'))
    h += DIV(
        DIV(T('Ваш реферальный код'), ':', BR(),
            '(', T('он же указатель для внутренних платежей'), ')', _class='col-sm-' + col1),
        DIV(B(man.ref_key, _class='inv'),
            _class='col-sm-' + col2),
        _class='row')
    h += DIV(
        DIV(T('Реферальная ссылка 1'), ': ', _class='col-sm-' + col1),
        DIV(B('%s' % URL('start', 'index', vars={'gc': man.ref_key}, scheme=True, host=True)),
            _class='col-sm-' + col2),
        _class='row')
    h += DIV(
        DIV(T('Реферальная ссылка 2'), ': ', _class='col-sm-' + col1),
        DIV(B('%s' % URL('star_a', 'index', vars={'gc': man.ref_key}, scheme=True, host=True)),
            _class='col-sm-' + col2),
        _class='row')
    h += DIV(
        DIV(T('Реферальная ссылка 3'), ': ', _class='col-sm-' + col1),
        DIV(B('%s' % URL('sun_a', 'index', vars={'gc': man.ref_key}, scheme=True, host=True)),
            _class='col-sm-' + col2),
        _class='row')
    h += DIV(
        DIV(P('*', T('Вообще любая ссылка с добавкой параметра "%s" является реферальной') % ('gc=' + man.ref_key), '. ',
             T('Надо помнить что первый параметр добавляется к URL через "?", а все остальные через "&"'),'.'), _class='col-sm-8'),
        _class='row')
    if man.ref_man and len(man.ref_man) > 5:
        h += DIV(
            DIV(T('Ваc пригласил наставник'), ': ', _class='col-sm-' + col1),
            DIV(B('%s' % man.ref_man),
                _class='col-sm-' + col2),
            _class='row')
    
    ##local_import(bonus_lib, reload=True)
    import bonus_lib
    referals, active_referals = bonus_lib.calc_referals(db, man)
    ref_bonus = bonus_lib.calc_referals_bonus(active_referals)

    h += DIV(
        DIV(T('Количество Ваших рефералов'), ':', _class='col-sm-' + col1),
        DIV(B(referals, _class='inv'),
            _class='col-sm-' + col2),
        _class='row')
    h += DIV(
        DIV(T('Количество активных рефералов'), ':', _class='col-sm-' + col1),
        DIV(B(active_referals, _class='inv'),
            _class='col-sm-' + col2),
        _class='row')
    h += DIV(
        DIV(T('"Звёздные баллы" за рефералов'), ':', _class='col-sm-' + col1),
        DIV(B(ref_bonus, _class='inv'),
            _class='col-sm-' + col2),
        _class='row')

        
    h += H3(T('Бонус для программы "10 тысяч Звёзд"'))
    h += CAT(P(T('Чтобы бесплатно попасть в программу старта "10 тысяч Звёзд" и начать форжинг с самого старта блокчейн-среды, заработайте "Звёздные баллы". Для этого запостите в социальной сети новость про старт нашего блокчейн проекта. В своем посте Вы можете указать свою реферальную ссылку на программу старта "10 тысяч Звёзд"'), ' ', B(URL('star_a', 'index', vars={'gc': man.ref_key}, scheme=True, host=True))),
           P(T('Размезмещайте новость в разных соц.сетях, и ссылки на посты введите в поля ниже. Через некоторое время Вам будут начислены "Звёздные баллы" в зависимости от числа лайков на Ваши посты. Количество "Звёздных баллов" может увеличить размер Вашего пакета форжинга. Баллы затем трансформируются в доли программы старта "10 тысяч Звёзд", что будет отражено в Ваших балансах личного кабинета. Так же чем больше по Вашим ссылккам прийдет рефералов, тем больше вы получите еще "Звёздных баллов".')),
           P('*', T('Примечание. Чтобы получить ссылку на Ваш пост нужно, в Фейсбуке например, выбрать пункт меню "Встроить", далее "Расширенные настройки" и там взять ссылку.')),
           P('*', T('Примечание. Не забудьте еще указать ниже счет для вывода к этой программе старта чтобы мы смогли его внести в генесиз-блок.')),
        )

    form_soc1 = FORM(
                        LABEL(T('Ссылка на пост 1'),':'),' ',
                        INPUT(_name='social1', _value = man.social1 or '', requires=IS_NOT_EMPTY(), _class='account',
                              _placeholder='https://www.facebook.com/dmitry.ermolaev.1/posts/938248279640175'), ' ',
                 INPUT(_type='submit', _class='btn btn-' + CLRS_btn))
    if form_soc1.accepts(request, session, keepvalues=True, formname='form_tre'):
        man.update_record(social1 = form_soc1.vars.social1)
        redirect(URL())
    elif form_soc1.errors:
        response.flash = T('Ошибки ввода')
    
    if False and man.social1:
        h += P(T('Ваш первый пост'), ': ', A(man.social1, _href=man.social1, _target='blank', _class='white'))
    else:
        h += form_soc1

    h += BR()
    # https://www.facebook.com/dmitry.ermolaev.1/posts/938248279640175
    form_soc2 = FORM(
                        LABEL(T('Ссылка на пост 2'),':'),' ',
                        INPUT(_name='social2', _value = man.social2 or '', requires=IS_NOT_EMPTY(), _class='account',
                              _placeholder='https://www.facebook.com/dmitry.ermolaev.1/posts/938248279640175'), ' ',
                 INPUT(_type='submit', _class='btn btn-' + CLRS_btn))
    if form_soc2.accepts(request, session, keepvalues=True, formname='form_ащк'):
        man.update_record(social2 = form_soc2.vars.social2)
        redirect(URL())
    elif form_soc2.errors:
        response.flash = T('Ошибки ввода')
    
    if False and man.social2:
        h += P(T('Ваш второй пост'), ': ', A(man.social2, _href=man.social2, _target='blank', _class='white'))
    else:
        h += form_soc2
    
    h += H4(T('"Звёздные баллы" за активность в социальных сетях'), ': ', man.bonus)
    h += H4(T('"Звёздные баллы" за рефералов'), ': ', ref_bonus)
    h += BR()
    
    currs_select = []
    for item in db((db.cash_system.used == True)
                   & (db.cash_system.id == db.cash.system_id)
                   & (db.cash.used==True)).select(db.cash.id, db.cash_system.name, db.cash.name, orderby = db.cash.full_name):
        ##print item
        currs_select.append(OPTION(item.cash_system.name + ':' + item.cash.name, _value = item.cash.id))
        
    form_add_acc = FORM(H3(T('Добавить Счёт для вывода средств')),
                        P(T('Эти счета нужно взять из блокчейн-кошелька'), ' ', 
                          A(T('вот так'), _href=URL('bc3base', 'index#accounts'), _target='blank', _class='white')),
                        LABEL(T('Система средств'),':'),' ', SELECT(currs_select, _name='cash_id'), BR(),
                        LABEL(T('Счёт/Адрес/Кошелёк'),':'),' ',
                        INPUT(_name='account', requires=IS_NOT_EMPTY(),
                                  _placeholder='78JFPWVVAVP3WW7S8...', _class='account'),
                 INPUT(_type='submit', _class='btn btn-' + CLRS_btn))

    if form_add_acc.accepts(request, session, keepvalues=True, formname='form_one'):
        cash_id = form_add_acc.vars.cash_id
        acc = form_add_acc.vars.account.strip()

        # man_bal exist?
        man_bal = db((db.man_bals.man_id == man_id)
                    & (db.man_bals.cash_id == cash_id)).select().first()
        
        # man_bal_acc exist?
        acc_rec_exist = man_bal and db((db.man_accs.acc == acc)
                    & (db.man_accs.bal_id == man_bal.id)).select().first()
        if acc_rec_exist:
            response.flash = CENTER(T('Этот счёт уже введён'))
            ##return  DIV(h, _class='container')
        else:
            cash = db.cash[ cash_id ]
            if cash:
                if man_bal:
                    man_bal_id = man_bal.id
                else:
                    man_bal_id = db.man_bals.insert(man_id = man_id, cash_id = cash_id)

                db.man_accs.insert(bal_id = man_bal_id, acc = acc)
                redirect(URL('cab_bals', 'index'))
            else:
                response.flash = CENTER(T('Такой денежной системы нет'))
                ##return  DIV(h, _class='container')
    elif form_add_acc.errors:
        response.flash = CENTER(T('Ошибки при введении счёта'))
    else:
        ##response.flash = CENTER('please fill the form')
        pass

    h += form_add_acc
        
    h += BR()
    #h += HR()
    form_name = FORM(H3(T('Изменить Имя')),
                        LABEL(T('Новое Имя'),':'),' ', INPUT(_name='name', _value = man.name or '', requires=IS_NOT_EMPTY()), ' ',
                 INPUT(_type='submit', _class='btn btn-' + CLRS_btn))
    if form_name.accepts(request, session, keepvalues=True, formname='form_two'):
        man.update_record(name = form_name.vars.name)
        redirect(URL())
    elif form_name.errors:
        response.flash = T('Ошибки ввода')
    
    h += form_name

    if man.phone == None:
        h += HR()
        form_phone = FORM(H3(T('Изменить сотовый телефон')),
                            LABEL(T('Номер сотовго телефона'),':'),' ', INPUT(_name='phone', _value = man.phone or '', requires=IS_NOT_EMPTY()), ' ',
                     INPUT(_type='submit', _class='btn btn-' + CLRS_btn))
        if form_phone.accepts(request, session, keepvalues=True, formname='form_three'):
            phone = form_phone.vars.phone
            phone = valid_phone(phone)
            rec_exist = db(db.men.phone == phone).select().first()
            if rec_exist:
                response.flash = T('Этот телефон уже введён')
            else:
                man.update_record(phone = phone)
                redirect(URL())
        elif form_phone.errors:
            response.flash = T('Ошибки ввода')
    
        h += form_phone
        
    h += BR()
    h += CENTER(H3(A(B(T('Скачать Блокчейн ПО')), _href=URL('cabinet','download'), _class='white')))

    
    return DIV(h, _class='container')

def get_bal_lvl(man_id, cash_id, max_bal):
    if max_bal == 0:
        return 0
    man_bal = db((db.man_bals.man_id == man_id)
               & (db.man_bals.cash_id == cash_id)).select().first()
    if man_bal and man_bal.bal:
        return int(5 * man_bal.bal / max_bal)
    
    return 0

def list():
    response.title=T('Список Участников')
    response.not_show_function = True

    h = CAT()
    cl1 = 'col-sm-3'
    cl2 = 'col-sm-4'
    cl3 = 'col-sm-5'
    h += DIV(
        DIV(P(T('Имя'), _class='header'), _class=cl1),
        DIV(P(T('Уровень инвестиций'), BR(),
                SPAN(XML('<i class="fa fa-star"></i> '),
                  _style='color:#ff9100'), ' - 7 SUN', BR(),
                SPAN(fa_icons('fa-heart', 1),' ',
                  _style='color:#fd6cad'), ' - SHARE'),
            _class=cl2),
        DIV(P(T('Ник Ссылка +Вклад_В_Биткоинах'), _class='header'), _class=cl3),
         _class='row')
    
    max_field = db.man_bals.bal.max()
    max_shares = db(db.man_bals.cash_id == E_SHARES_ID).select(max_field).first()['MAX(man_bals.bal)']
    max_biz = db(db.man_bals.cash_id == E_BIZ_ID).select(max_field).first()['MAX(man_bals.bal)']
    max_soc = db(db.man_bals.cash_id == E_SOC_ID).select(max_field).first()['MAX(man_bals.bal)']
    #print max_shares, max_biz, max_soc
    
    odd = False
    bitcoin_id = myconf.take('cash.bitcoin_id', cast=int)
    datachain_id = myconf.take('cash.datachain_id', cast=int)
    
    for m in db(db.men).select(orderby = db.men.email):
        man_id = m.id
        odd = not odd
        email_id = m.email.find('@')
        
        investor_pay_shares = get_bal_lvl(man_id, E_SHARES_ID, max_shares)
        #investor_pay_biz = get_bal_lvl(man_id, E_BIZ_ID, max_biz)
        #investor_pay_soc = get_bal_lvl(man_id, E_SOC_ID, max_soc)
        
        man_bal_sun_volume = 0
        man_bal_sun = db((db.man_bals.man_id == man_id)
               & (db.man_bals.cash_id == SUN7_ID)).select().first()
        if man_bal_sun:
            man_bal_sun_volume = man_bal_sun.bal
                

        man_bal_result_btc = db((db.man_bals.man_id == m.id)
                     & (db.man_bals.cash_id == db.cash.id)
                     & (db.cash.system_id == bitcoin_id)).select().first()
        if man_bal_result_btc:
            investor_pay_btc = man_bal_result_btc.man_bals.dep_incomed
            investor_pay_btc = investor_pay_btc > 0 and SPAN(' +', investor_pay_btc) or ''
        else:
            investor_pay_btc = 0
            investor_pay = ''
            
        man_bal_erm = db((db.man_bals.man_id == m.id)
                     & (db.man_bals.cash_id == db.cash.id)
                     & (db.cash.system_id == datachain_id)
                     & (db.man_bals.id == db.man_accs.bal_id)).select().first()
        
        sun_view = ''
        if False and man_bal_erm:
            datachain_addr = man_bal_erm.man_accs.acc[:15]
            #print m.id, m.name, man_bal_erm.man_accs.id, datachain_addr
            sun = db((man_bal_erm.man_accs.id == db.man_acc_goods.man_acc_id)
                     & (db.goods.id == 1)
                     & (db.goods.id == db.man_acc_goods.good_id)).select().first()
            if sun:
                sun_view = XML('<i class="fa fa-star"></i>')
        else:
            datachain_addr = None

        h += DIV(
                DIV(A(m.name or '-', _href=URL(args=[man_id])), _class=cl1),
                DIV(H5(
                          man_bal_sun_volume and SPAN(XML('<i class="fa fa-star" style="font-size-:20px; color:#ff9100"></i>'),
                          SPAN(int(man_bal_sun_volume))) or '', ' ',
                          fa_icons('fa-heart', investor_pay_shares),' ',
                          #fa_icons('fa-heart', investor_pay_biz),'+',
                          #fa_icons('fa-heart', investor_pay_soc),
                      _class='-header'), _class=cl2, _style='color:#fd6cad'),
                DIV(P(datachain_addr or ('@' + m.email[:email_id]), ' ',
                      investor_pay_btc or '',
                      _class='header'), _class=cl3),
                
             _class='inv row' + (odd and ' odd' or ''))
    
    return dict(h = DIV(h, _class='container'))

def index():
    response.title=T('Личный Кабинет')
    response.not_show_function = True

    man_id = request.args(0) or session.man_id
    if man_id:
        man = db.men[ man_id ]
        if man:
            return dict(h = show_man(request, man))
        
        response.flash = T('Такого ID пользователя нет')
        ##redirect(URL('cabinet', 'list'))
        return dict()
    
    return dict( h = DIV(connect_form(), _class='container') )
