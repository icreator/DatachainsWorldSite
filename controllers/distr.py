# -*- coding: utf-8 -*-
# try something like

def list():
    response.title=T('Список Дистрибьюторов')
    response.not_show_function = True

    h = CAT(
        CENTER(H2(T('Список Партнёров и Дистрибьюторов'))),
        P(XML(T('Описание для желающих как %s') % A(B(T('стать Партнёром или Дистрибьютором')),
                                             _href=URL('distr', 'index'), _class='white'))))
    cl1 = 'col-sm-4'
    cl2 = 'col-sm-2'
    cl3 = 'col-sm-6'
    h += DIV(
        DIV(P(T('Дистрибьютор'), _class='header'), _class=cl1),
        DIV(P(T('Уровень'), _class='header'), _class=cl2),
        DIV(P(T('Описание'), _class='header'), _class=cl3),
         _class='row')
    
    
    odd = False
    
    for m in db(db.distrib).select(orderby = db.distrib.name):

        h += DIV(
                DIV(A(IMG(_src=m.pic_url), ' ', B(m.name), _href=m.url, _target='blank'),
                    _class=cl1),
                DIV('',
                    _class=cl2),
                DIV(XML(m.info),
                    _class=cl3),
                
             _class='inv row' + (odd and ' odd' or ''))
    
    return dict(h = DIV(h, _class='container'))


def index():
    
    session.forget(response)
    response.title=T('Дистрибьюция блокчейн-среды')
    response.not_show_function = True

    h = CAT()
    
    h += DIV(
            DIV(
                DIV(
                DIV(
                BR(),
                H1(T('Дистрибьюция - заработок на старте блокчейн-сред')),
                H2(T('Вы получаете скидку до 30%')),
                H2(T('Это выгодный заработок на Вашей клиентской базе')),
                #BR(), BR(), BR(), BR(),
                _class='col-sm-8'),
                DIV(
                    #A(T('Зажечь!'), _href=URL('api','index'),
                    #  _class="btn btn-one btn-lg", _style="background-color:slategrey; font-size: 26px; margin-top: 50px; padding: 10px 40px;"),
                    _style='-bottom:10px;-right:10px;',
                _class='col-sm-4'),
                _class='row'),
                _class='container',
               _style='color:white; text-shadow:0.15em 0.15em 0.3em black; max-height:500px; min-height: 500px;'),
        _style='max-height:500px; min-height: 500px;',
        _id='box_bg') # for backstretch JS
    
    col1 = '2'
    col2 = '3'
    data1 = '2016-10-26'
    h += DIV(
        DIV(
            DIV(
                DIV(H3(T('Несите свет знаний')),
                _class='col-sm-4'),
                DIV(
                    P(T('Станьте проводником новых знаний о технологии блокчейн!')),
                _class='col-sm-8'),
            _style='padding-top: 20px;',
            _class='row'),
            DIV(
                DIV(H3(T('Получайте доход')),
                _class='col-sm-4'),
                DIV(
                    P(T('За каждую продажу нашей услуги Вы оставляете у себя до 30% с цены!')),
                _class='col-sm-8'),
            _style='padding-top: 20px;',
            _class='row'),
            H2(T('Виды дистрибьюции')),
            UL([
                    SPAN(B(T('Реферальный партнёр')), '. ', T('Самый простой способ заработка - просто даёте свою реферальную ссылку и все кто по ней заходят становятся вашими рефералами. И их платежи на данном сайте дают Вам подарок в зависимости от реферального процента по данному виду платежа. Обычно это 10% от суммы платежа Вашего реферала. Реферальную ссылку Вы можете получить в своём'), ' ', 
                    A(B(T('Личном Кабинете')), _href=URL('cabinet', 'index'), _class='blue'), '.'),
                    SPAN(B(T('Простой дистрибьютор')), '. ', T('Вы можете разместить на своём сайте наши программы старта со своими ценами и своим описанием. При этом оплату со своих клиентов Вы будете собирать напрямую - на Ваши банковские карты или безналичные счета. Накопив некоторую сумму, оптом, оплачиваете к нам рублевую или биткоиновую сумму, получаете средства на свой внутренний счет, затем переводите эти средства в нужную программу старта и далее в пределах этой программы переводите нужные суммы своим клиентам по их емайлу. Далее либо подаёте нам оптовый список счетов клиентов (емай - блокчейн-счёт для программы старта), либо присылаете на емайл своему клиенту ссылку на наш сервис, для того чтобы он сам задал номер счета для вывода средств. Таким образом, ваши клиенты становятся внесенными в нашу систему учета'), '.'),
                    SPAN(B(T('Дистрибьютор')), '. ', T('Отличие от простого дистрибьютора в том, что цены программы Вы не меняете, а оптовый список клиентов еще содержит суммы платежей клиентов. И по каждому клиенту в отдельности нами проводится расчёт Вашей дистрибьюторской награды. К тому же Вам не нужно самостоятельно переводить средства на внутренние счета клиентов - это будет сделано автоматически'), '.'),
                    ]),
            H2(T('Программа дистрибьюции старта блокчейн-среды'), SPAN(XML('<i class="fa fa-star"></i> '),
                  _style='color:#ff9133')),
            
            H3(T('Выгоды которые Вы получите как Дистрибьютор')),
            P(B('1. '), T('Ваша клиентская база даст Вам заработок около 1000-5000 с физ.лица и около 10000-50000 с юр.лица согласно рекомендуемым ценам программ старта'), ' ',
                 ),
            P(B('2. '), T('Ваши клиенты впоследствии после запуска блокчейн-среды начнут быстрее вести бизнес, уменьшат свои затраты и повысят свой доход. А значит смогут больше заказывать и покупать Ваших услуг и товаров.')),
            P(B('3. '), T('Вы можете воочию убедиться в возможностях нашей блокчейн-среды, составить мнение о её перспективах и обдуманно стать нашим ранними инвестором по выгодной цене.')),
            H3(T('Уровни скидок')),
            P(T('Примечание. Чем выше уровень Вы продали тем больше скидка.')),
            DIV(
                DIV(B(T('Размер уровня в рублях для физ.лиц')),
                    _class='col-sm-' + col1),
                DIV(B(T('Скидка')),
                    _class='col-sm-' + col2),
                DIV(B(T('Размер уровня в рублях для юр.лиц')),
                    _class='col-sm-' + col1),
                DIV(B(T('Скидка')),
                    _class='col-sm-' + col2),
            _class='row'),
            DIV(
                DIV(CENTER('< 15 000'),
                    _class='col-sm-' + col1),
                DIV(CENTER('30%', ' ', T('но не более'), ' ', 3000),
                    _class='col-sm-' + col2),
                DIV(CENTER('< 50 000'),
                    _class='col-sm-' + col1),
                DIV(CENTER('20%', ' ', T('но не более'), ' ', 6000),
                    _class='col-sm-' + col2),
            _class='row'),
            DIV(
                DIV(CENTER('15 000 - 100 000'),
                    _class='col-sm-' + col1),
                DIV(CENTER('20%', ' ', T('но не более'), ' ', 7000),
                    _class='col-sm-' + col2),
                DIV(CENTER('50 000 - 350 000'),
                    _class='col-sm-' + col1),
                DIV(CENTER('15%', ' ', T('но не более'), ' ', 14000),
                    _class='col-sm-' + col2),
            _class='row odd'),
            DIV(
                DIV(CENTER('> 100 000'),
                    _class='col-sm-' + col1),
                DIV(CENTER('10%', ' ', T('но не более'), ' ', 15000),
                    _class='col-sm-' + col2),
                DIV(CENTER('> 350 000'),
                    _class='col-sm-' + col1),
                DIV(CENTER('10%', ' ', T('но не более'), ' ', 50000),
                    _class='col-sm-' + col2),
            _class='row'),
            H3(T('Что нужно:')),
            P(T('Заключить дистрибьюторское соглашение с ИПО Польза или войти в Целевую Программу "Старт 7 Солнц"')),
            P(T('Получить от клиента его счет в блокчейн-среде, который он должен создать самостоятельно, загрузив и установив нашу программу-клиент блокчейн-среды. Вы можете архив этой программы поставлять на своём сайте, чтобы Ваши клиенты не переходили на сторонние сайты.')),
            P(T('Оплатить оптом лицензии для своих клиентов на заданные уровни и предоставить список счетов и уровень (в рублевом выражении) для этого счета.')),

            H3(A(T('Дистрибуторы'), _href=URL('distr','list'), _class='white')),

            H3(T('Описание программ старта')),
            P(T('Вы можете их немного изменить под своё видение.')),
            DIV(CENTER(
                A(T('"777 Солнц" для граждан'), _href=URL('sun_a','index'),
                  _class="btn btn-one btn-lg", _style="background-color:slategrey; font-size: 26px; margin-top: 30px; margin-left: 20px; padding: 10px 40px;"),
                A(T('"77 Солнц" для бизнеса'), _href=URL('sun_b','index'),
                  _class="btn btn-one btn-lg", _style="background-color:slategrey; font-size: 26px; margin-top: 30px; margin-left: 20px; padding: 10px 40px;"),
                  ),
            _style='',
            _class='row'),
        _class='container'),
        _style='background-color:#ddd; color:#222; padding-bottom:30px;')


    import random
    links = [
        '8349611_6690c42b-.jpg',
        #'514107_devushka_reka_priroda-.jpg',
        #'1327938348_girls-1.jpg',
        '8349611_6690c42b-.jpg',
        #'main_dominican.jpg',
        #'yahta_na_gorizonte_1280x1024-.jpg',
        #'aguri-015.jpg',
        'avstralia-19.jpg',
        #'100.news.111.jpg.medium.jpg',
        'trd_hq2.jpg',
        '83166786_PARASHUT.jpg',
        #'1388389935_zhemchuzhina_chernogo_morya_2013_goda_2.jpg',
        'hq-wallpapers_ru_nature_42726_1920x1080.jpg',
        #'1502_5065.jpg',
        '193351511.jpg',
        #'svadba_v_usadbe.jpg',
        'img1338631927.jpg',
        '2569_villa-1.jpg',
        '03cheers.jpg',
        ]
    random.shuffle(links)
    ll = []
    for l in links:
        ll.append(URL('static','images/b/%s' % l))
    response.files.append(URL('static','js/backstretch.js'))
    h += SCRIPT('''
        //jQuery(document).ready(function() {
            //$('.span_left').backstretch([
            $('#box_bg').backstretch(%s, {duration: 7000, fade: 3330});
        //    });
            ''' % XML(ll))

    return dict( h = h )
