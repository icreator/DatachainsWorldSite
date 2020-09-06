# -*- coding: utf-8 -*-
# try something like


def index():
    
    session.forget(response)
    response.title=T('Зажги Солнце блокчейна')
    response.not_show_function = True

    sun7F_ID = 18
    sun7B_ID = 19
    
    cash_f = db.cash[sun7F_ID]
    cash_b = db.cash[sun7B_ID]

    h = CAT()
    
    h += DIV(
        DIV(
            DIV(
                DIV(
                    H3(T('Эта программа будет стартовать позже, ждите новостей!')),
                    H3(P(XML(T('Присоединайтесь к программе %s')
                               % A(T('777 Солнц'), _href=URL('sun_a', 'index'), _class="btn btn-for btn-lg")))),
                    H3(P(' ', P(T('Золотая ERA грядёт!')))),
                _class='col-sm-12'),
                _class='row'),
                _class='container orange',
               _style='color:white; text-shadow:0.15em 0.15em 0.3em black; max-height:500px; min-height: 500px;'),
        _style='max-height:500px; min-height: 500px;',
        _id='box_bg') # for backstretch JS
    

    return dict( h = h )
