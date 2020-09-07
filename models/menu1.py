# -*- coding: utf-8 -*-

if False:
    from gluon import *
    request = current.request
    response = current.response
    session = current.session
    cache = current.cache
    T = current.T
    pass

if request.ajax:
    pass
else:

    ALERT = None
    #ALERT='ATTENTION!!! servise on recharge'
    MNU_ICONS = True

    NO_IMG=True # for local develop

    TITLE = 'DATACHAINS.World'
    KEYWORDS = T('blockchain 3.0 datachain')
    DESCRIPTION = T('design blockchain 3.0')

    if IS_MOBILE:
        LOGO = None
        pass
    else:
        LOGO = DIV(A(SPAN('DATA', IMG(_src=URL('static','images/logo_dcw.png'), _width=30), 'CHAINS'),
                              _href=URL('default','index'), _class='button brand'),
                    _id='start', _class='brand_wrapper')
        pass


    LANG_CURR = session.lang or T.accepted_language
    def lang_sel():
        langs = []
        for (n,l) in LANGS.iteritems():
            if LANG_CURR == n: continue
            vars = request.vars.copy()
            vars['lang'] = n
            langs.append((
                    CAT(IMG(_src=URL('static', 'images/flags/' + l[1]), _width=30, _alt=''),
                        ' ', not IS_MOBILE and l[0] or ''), False, URL(args=request.args, vars=vars))
                  )
        return langs


    # 
    lang = LANGS.get(LANG_CURR, LANGS.get('en', LANGS.get('ru', LANGS.values()[0])))
    MENU_RIGHT = [
        (CAT(IMG(_src=URL('static', 'images/flags/' + lang[1]), _width=30, _alt=''), not IS_MOBILE and CAT( ' ', lang[0]) or ''),
            False, None, lang_sel())
        ]

    MAN_NAME = session.man_name

    if False:
        pass
    else:
        response.menu = MENU_1 = [
            (SPAN(MNU_ICONS and TAG.i(_class='fa fa-link big3', _style='color:red;') or '', ' ', T('БЛОКЧЕЙН 3-го поколения'), _title=T('Общее описание')),
                 False, URL('default','index')),
            (SPAN(MNU_ICONS and TAG.i(_class='fa fa-user-circle-o big3', _style='color:red;') or '', ' ', T('КАБИНЕТ %s' % MAN_NAME) if MAN_NAME else T('Личный Кабинет'), _title=T('Балансы, личные данные')),
                 False, URL('cabinet','index')),
            (SPAN(MNU_ICONS and TAG.i(_class='fa fa-btc big3', _style='color:red;') or '', ' ', T('ЗАРАБОТАТЬ'), _title=T('Тут можно заработать')),
                 False, URL('earn','index')),
            (SPAN(MNU_ICONS and TAG.i(_class='fa fa-line-chart big3', _style='color:red;') or '', ' ', T('ИНВЕСТИРОВАТЬ'), _title=T('Для инвесторов в блокчейн')),
                 False, URL('invest','index')),
            (SPAN(MNU_ICONS and TAG.i(_class='fa fa-file-text big3', _style='color:red;') or '', ' ',T('ОПИСАНИЕ')),
                 False, URL('bc3base','index')),
            (SPAN(MNU_ICONS and TAG.i(_class='fa fa-comments-o big3', _style='color:red;') or '', ' ', T('СООБЩЕСТВО'), _title=T('Нам нужны специалисты')),
                 False, URL('community', 'index')),
            (SPAN(MNU_ICONS and TAG.i(_class='fa fa-plus-circle big3', _style='color:red;') or '', ' ', T('ВАКАНСИИ'), _title=T('Нам нужны специалисты')),
                 False, URL('community', 'vacant')),
            (SPAN(MNU_ICONS and TAG.i(_class='fa fa-rocket big3', _style='color:red;') or '', ' ', T('НОВОСТИ'), _title=T('')),
                 False, URL('news','index')),
            (SPAN(True and TAG.i(_class='fa fa-phone big3', _style='color:red;') or '', _title=T('Наши Контакты')),
                 False, URL('default','contacts')),
        ]
    
    MENU_2 = None
    cnt = request.controller
    if cnt in ['default', 'bc3biz', 'bc3gov', 'bc3liv', 'bc3all','bc3base',]:
        MENU_2 = [
            (T('Основы'), False, URL('bc3base','index')),
            (T('Блокчейн для бизнеса'), False, URL('bc3biz','index')),
            (T('Блокчейн для граждан'), False, URL('bc3liv','index')),
            (T('Блокчейн для гос.органов'), False, URL('bc3gov','index')),
            (T('ЗАКОНЫ и Блокчейн'), False, URL('default','law')),
            (T('Whitepaper'), 0, URL('default', 'index#whitepaper')),
            (T('Загрузить'), 0, URL('cabinet','download')),
            ]

    elif cnt in ['cabinet', 'cab_bals']:
        MENU_2 = [
                    (T('Балансы'), 0, URL('cab_bals','index')),
                    (SPAN(T('Загрузить')), 0, URL('cabinet','download')),
                    (T('ОТКЛючиться'), 0, URL('cabinet','disconnect'))
            ]
        if IS_LOCAL:
            MENU_2.append((SPAN(T('Участники')), 0, URL('cabinet','list')))

    elif cnt in ['earn', 'star_a', 'distr', 'sun_a', 'sun_b', 'activ_a']:
        MENU_2 = [
                    #(T('Новогодний подарок "Я Активист!"'), 0, URL('activ_a','index')),
                    (T('Флагман'), 0, URL('earn', 'partner_dc')),
                    (T('Партнер'), 0, URL('earn', 'partner')),
                    (T('Дистрибьютор'), 0, URL('distr','index')),
                    #(T('Форжер "Звезда"'), 0, URL('star_a','index')),
            ]
    elif cnt in ['pubkey']:
        MENU_2 = [
                    #(T('Новогодний подарок "Я Активист!"'), 0, URL('activ_a','index')),
                    (T('Флагман'), 0, URL('earn', 'partner_dc')),
                    (T('Загрузить'), 0, URL('cabinet','download'))
            ]
    elif cnt in ['invest', 'share_a', 'share_f10', 'share_u']:
        MENU_2 = [
                    (T('ICO рыночное'), 0, URL('share_a','index')),
                    (T('ICO фиксированное'), 0, URL('share_f10','index')),
                    (T('ICO для юр.лиц'), 0, URL('share_u','index')),
            ]
    else:
        MENU_2 = [
                     (T('Загрузить'), 0, URL('cabinet','download'))
            ]
