# -*- coding: utf-8 -*-

response.generic_patterns = ['*.html']

session.forget()

# переходник для показа ссыфлкок и картинок в листингах
def download():
    return response.download(request,db)

##@cache.action(time_expire=cache_expire, cache_model=cache.ram, quick='P')
def index():
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

    #return response.render(h)
    return dict(h=h)

def contacts():
    session.forget(response)
    response.title=T('Контакты')
    response.not_show_function = True
    h = CAT(
        DIV(
            CENTER(H2('Адрес')),
        H4(P('г.Москва, Покровский бульвар д.8 стр.2А. 4-й этаж оф.6. Вход в арку, далее во внутреннем дворе вход правее по ходу.')),
        DIV(
        DIV(
         CENTER(IMG( _src=URL('static','images/in_place1.jpg'), _style="width:240px"),
         _class="col-sm-6")),
        DIV(
         CENTER(IMG( _src=URL('static','images/in_place2.jpg'), _style="width:240px"),
         _class="col-sm-6")),
        _class="row"),
        DIV(
        
        #H3(T('Отзывы, Обсуждение, Жалобы, Благодарности')),
        #T('Можно найти в ветке на'),' ',
        #A(T('международном форуме о криптовалютах'),
        #  _href='https://bitcointalk.org/index.php?topic=307648.0', _target='_blank'),'. ',
        #H2(T('Обратная связь')),

            DIV(
            CENTER(H2('КОМАНДА')),
        CENTER(H3(T('Директор по развитию и внешним коммуникациям'))),
                DIV(
        P(IMG( _src=URL('static','images/nikishkin_nik.jpg'), _style="width:320px")),
                    _class="col-sm-5"),
                DIV(
        H4(T('Никишкин Николай Анатольевич')),
        T('тел'),': ', '+7 916 711 18 91 ', BR(),
        A('facebook: Николай Никишкин', _href='https://www.facebook.com/notoff86', _target='_blank', _class='blue'), BR(),
        #T('Skype'),': ', 'i-creator',BR(),
            
                    _class="col-sm-7"),
                    _class="row"),
        HR(),
            DIV(
        CENTER(H3(T('Коммерческий директор'))),
                DIV(
        P(IMG( _src=URL('static','images/borisov.jpeg'), _style="width:320px")),
                    _class="col-sm-5"),
                DIV(
        H4(T('Борисов Евгений Борисович')),
        T('тел'),': ', '+7 915 333 17 97 ', BR(),
        A('facebook: Евгений Борисов', _href='https://www.facebook.com/profile.php?id=100001625036579', _target='_blank', _class='blue'), BR(),
        BR(),
        T('Почтовый ящик'),': ', 'Borisov_Evgen7@mail.ru',BR(), # Borisov_evgen7@mail.ru
                BR(),
            
                    _class="col-sm-7"),
                    _class="row"),
            DIV(
        CENTER(H3(T('Директор по разработке и внедрению блокчейн-технологий'))),
                DIV(
        P(IMG( _src=URL('static','images/ermolaev-1-2.jpg'), _style="width:320px")),
                    _class="col-sm-5"),
                DIV(
        H4(T('Ермолаев Дмитрий Сергеевич')),
        T('тел'),': ', '+7 916 917 20 19 ', BR(),
        'Facebook', ': ', A('Дмитрий Ермолаев', _href='https://www.facebook.com/dmitry.ermolaev.1', _target='_blank', _class='blue'), BR(),
        BR(),
        T('Почтовый ящик 1'),': ', 'icreator@mail.ru',BR(),
        T('Почтовый ящик 2'),': ', 'adm@ipo-polza.ru',BR(),
                BR(),
        T('Skype'),': ', 'i-creator',BR(),
                        BR(),
        H3(T('Для частных инвесторов')),
        H4(T('Для внесения рублей на счет как физическое лицо используйте'),':'),
        T('Карта Сбербанка'),' ', '4276880136232943', BR(),
        T('кошелек Яндекс'), ' ', '41001555269641', BR(),
        T('кошелек КИВИ, по сотовому телефону'), ' ', '+79169172019', BR(),
        H4(T('Для внесения рублей на счет как юридическое лицо используйте'),':'),
        A(T('Инновационное потребительское общество "Польза"'), _href='http://ipo-polza.ru', _target='blank', _class='white'),
                BR(),
                    _class="col-sm-7"),
                    _class="row"),
        HR(),
        _class='row'),
        _class='container'),
        )
    return dict(h =h)

def law():
    session.forget(response)
    response.title=T('ЗАКОНЫ и Блокчейн')
    response.not_show_function = True
    h = CAT(
        DIV(
            BR(),
            CENTER(H1(T('Все наши решения на блокчейн-средах находятся в правовом поле России'))),
            BR(),

        DIV(
        H2(T('А так же мы подготовли пакет поправок для внедрения Блокчейн-технологий для других применений и направили его в Думу РФ')),
        H4(T('Подробнее в открытом доступе тут'),':'),
            DIV(
                TAG.center(
                    H2(A(T('DUMA 2016-06-02 - blockchain'), _href='https://github.com/icreator/DUMA-2016-06-02', _target='_blank',
                   _class='button lightblue-bgc col-sm-12')), # lightblue-bgc
                _style='padding: 5px;',
                _class='co-l-sm-12'),
            _class='row'),
                BR(),
                BR(),
        _class='row'),
        _class='container'),
        )
    return dict(h =h)
