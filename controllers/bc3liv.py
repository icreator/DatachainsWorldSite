# -*- coding: utf-8 -*-

response.generic_patterns = ['*.html']

session.forget()

# переходник для показа ссыфлкок и картинок в листингах
def download():
    return response.download(request,db)

def poll():
    response.not_show_function = True

    h = CAT(
        DIV(
            CENTER(H2(T('Голосования в блокчейне 3.0'))),
            CENTER(H3(T('Если Вам нужны открытые честные голосвания без возможности подмены'))),
            P(T('Онлайн голосования - просто и эффективно')),
           _class = 'container'),
        DIV(CENTER(IMG(_src=URL('static', 'images/tutor/voting-01.png')))
            ),
        DIV(
            CENTER(H3(T('Значимость голосований'))),
            P(T('Результаты голосования видны открыто и кто за что голосовал явно, то есть голос учитывается юридически значимо и удостоверен усиленной электронной подписью.')),
           _class = 'container'),
        DIV(CENTER(IMG(_src=URL('static', 'images/tutor/voting-02.png')))
            ),
        DIV(
            BR(),
            H3(A(T('Еще решения для граждан'), _href=URL('bc3liv','index'), _class='blue')),
            P(T('')),
            BR(),
           _class = 'container'),
        )

    return dict(h=h)

##@cache.action(time_expire=cache_expire, cache_model=cache.ram, quick='P')
def index():
    response.not_show_function = True

    '''
    h = DIV(
            TAG.center(
                H1(B(SPAN('DATA', _style='color:chartreuse;'), SPAN('CHAINS', _style='color:gold;'),
                     SPAN('.WORLD', _style='color:powderblue;'),
                  ), _style='font-size:60px;text-shadow:1px 1px 2px black, 0em 0em 0em #00F1FF'),
                #H1('The Gobal Financial Revolution', _style='color:deepskyblue;text-shadow: 3px 3px 5px black, 0em 0em 0em #000;'),
                H4('проект внедрения технологии блокчейн в повсеместную жизнь - "в цепочки данных мы верим!"'),
                #2('But all its is DATACHAINS!'),
            ),
            _class='container-fluid bgi_h1', _style='background:#FFF; color: #666',
            _id="top_line")

    h += BR()
    '''
    h = CAT()

    h += CENTER(H1(T('Наши решения к которым Вы можете присоединиться уже сейчас')))
    h += CENTER(H1(T('или заказать решение под себя')))
    h += BR()
    
    odd = True
    cl1 = '4'
    cl2 = '8'
    for r in [
            [B(T('Основы')),
               P(T('Базовые возможности нашего блокчейна 3-го поколения'), '. ', A(B(T('Подробнее')), _href=URL('bc3all','index'), _class='white')),
               ],
            [A(TAG.i(_class='fa fa-link'), ' ', SPAN(T('Голосования ТСЖ')),
             _href = URL('bc3liv', 'poll')),
               P(T('Вам нужны удаленные голосования без возможности подтасовки и полностью законные и юридически-значимые, то наш блокчейн 3.0 для Вас.'), ' ', A(B(T('Подробнее')), _href=URL('bc3liv','poll'), _class='white')),
               ],
            [A(TAG.i(_class='fa fa-link'), ' ', SPAN(T('Голосования в партиях')),
             _href = URL('bc3liv', 'poll')),
               P(T('Хотите честных выборов своих лидеров, проводимых на любом удалении дешево и эффективно? Наш блокчейн для Вас!'), ' ', A(B(T('Подробнее')), _href=URL('bc3liv','poll'), _class='white')),
               ],
            [A(TAG.i(_class='fa fa-link'), ' ', SPAN(T('Завещания честно и эффективно')),
             _href = URL('bc3liv', 'zav')),
               P(T('в разработке'), ' ', A(B(T('Подробнее')), _href=URL('bc3liv','zav'), _class='white')),
               ]
             ]:
        h += DIV(
            DIV(DIV(
                DIV(H4(r[0]), _class='col-sm-' + cl1 ),
                DIV(r[1], _class='col-sm-' + cl2 ),
            _class = 'row'), _class = 'container'),
            _class = 'row' + ' odd' if odd else '')
        odd = not odd
    h += HR()
    h += CENTER(H2(A(B(T('Закажите свой блокчейн')), _href=URL('bc3order','index'), _class='white')))

    
    return dict(h=h)
