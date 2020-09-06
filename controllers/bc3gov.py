# -*- coding: utf-8 -*-

response.generic_patterns = ['*.html']

session.forget()
#response.not_show_function = True


# переходник для показа ссыфлкок и картинок в листингах
def download():
    return response.download(request,db)

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

    h += CENTER(H1(T('Наши решения к которым Вы можете присоедиться уже сейчас')))
    h += CENTER(H1(T('или заказать решение под себя')))
    h += BR()
    
    odd = True
    cl1 = '5'
    cl2 = '7'
    for r in [[T('Учёт социальных статусов'),T('Студент, пенсионер, безработный, военнослужащий, ...')],
              [T('Учёт инвалидностей'),T('Для социального фонда РФ')],
              [T('Учёт судимотей'),T('')],
              [T('Учёт гражданства'),T('')],
              [T('Учёт патентов и лицензий для ИП'),T('Учёт лицензий - на что когда и кем выдана - невозможно подделать и данные о выданных лицензиях видны публично - не нужно делать долие запросы и проверки - повышается эффективность надзорной деятельности РосНадзор')],
              [T('Учёт дипломов и аттестатов'),T('Для МинТруда и МинОбразования')],
              [T('Учёт специальностей и квалификаций'),T('Для МинТруда и МинОбразования')],
              [T('Учёт трудовой занятости'),T('Для МинТруда и МинОбразования')],
              [T('Предложите Вашу задачу!'),T('Мы с радостью сделаем решение её на нашей блокчейн-среде')],

             ]:
        h += DIV(
            DIV(DIV(
                DIV(H3(r[0]), _class='col-sm-' + cl1 ),
                DIV(r[1], _class='col-sm-' + cl2 ),
            _class = 'row'), _class = 'container'),
            _class = 'row' + ' odd' if odd else '')
        odd = not odd
    h += HR()
    h += CENTER(H2(A(B(T('Закажите свой блокчейн')), _href=URL('bc3order','index'), _class='white')))

    
    return dict(h=h)
