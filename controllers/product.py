# -*- coding: utf-8 -*-

def index():
    h = CAT(
    DIV(
        DIV(
                H1('DATACHAINS-ПРОДУКТЫ', _class='center'),
                P('Распределённая среда учета денежных средств, активов, акций, голосований, товаров и услуг готовится к запуску! Вы можете стать её членом и получить начальные управляющие и рабочие единицы. Для этого скачайте клинет-кошелек и создайте свои счета.', BR(),
                    ),
                P(A(B('ERM7 v.2.14.01'), _href=URL('static','files/ERM7.zip'), _target='blank'), ' - ', T('Эта версия пока только для генерации счетов в среде, цепочка боков не стабильна.')),
                P(T('Внимание! Для работы нужен пакет'), ' ', A(B('Java'), _href='http://www.java.com/ru/', _target='blank')),
                P('Для получения учётных единиц, необходимых для внесения записей в среду, сообщите нам свой счёт в этой среде.'),
                P('Если синхронизация не происходит, загрузите последнюю версию с сайта и удалите базу блоков (папки /data и /dataBak).'),
                P('Просмотреть деятельнось в среде можно через веб-интерфейс',': ',
                  A(B('Explorer'), _href='http://54.194.119.240:9180/index/blockexplorer.html', _target='blank'),'.'),
                P(
                    XML(T('Определите %s места своего рождения') % A(T('Геокоординаты'), _href='http://u-karty.ru/opredelenie-koordinat-na-karte-yandex', _target='blank')),
                T(''),
                ),
               DIV(
                    TAG.center(
                        H2(A(T('Обсуждение запуска'), _href='https://bitcointalk.org/index.php?topic=1289411.0', _target='blank',
                           _class='button blue-bgc')), # lightblue-bgc
                        _style='padding: 30px;',
                        _class='col-sm-12'),
                    _class='row m-0'),
                _class='container', _id='product'),
        _style='background-color:#ddd; color:#222;padding-bottom:30px;',
        _class='row m-0'),

        )
    return dict(h=h)
