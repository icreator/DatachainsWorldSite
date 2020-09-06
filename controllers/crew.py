# -*- coding: utf-8 -*-
#
session.forget(response)
response.title=T('Команда')
response.not_show_function = True


def index():
    session.forget(response)
    response.title=T('Команда')
    response.not_show_func = True
    h = CAT(
        DIV(DIV(DIV(
        #H1(''),
                P(T('Ищем программиста Java и C++')),
        
                P(XML(T('Хочешь стать востребованным и знаменитым? Смело %s с нами!') % A(B('связывайся'), _href=URL('default','contacts')))),
                _class="col-sm-12"),
            _class="container", _style="padding:10px 10%;"),
        _class='row', _id='invite', _style="padding-bottom:10px;")
        )
    
    crew = CAT()
    for r in db(db.crew).select():
        crew += CAT(
            DIV(
            DIV(
                IMG(_src=URL('default','dowload/uploads',args=[r.pic]), _class='img-circle', _width=200) if r.pic else ' ',
                IMG(_src=URL('static','images/uploads',args=[r.pic_url]), _class='img-circle', _width=200) if r.pic_url else ' ',
                _class='col-sm-4', _style='width:230px;',
                ),
            DIV(
                B(r.fio), ' ', 
                r.linkedin and A('LinkedIN', _href='https://www.linkedin.com/profile/view?id='+r.linkedin, _target='_blank') or '',BR(),
                r.skills,
                r.contacts and CAT(BR(),XML(r.contacts)) or '',
                _class='col-sm-8',
                ),
            _class='row'),
            DIV(P(XML('&laquo;'), TAG.i(r.say), XML('&raquo;')),
            _class='row'),
            HR(),
            )
        
    
    h += DIV(DIV(
            H1(P(T('Команда'))),
            DIV(crew,
                A(B(T('см. презентацию')), _class='blue', _href='https://docs.google.com/presentation/d/1OpfTvrsQ_R0TXt8RHfRBjrqAt9TYgGZuXwSgM5LXudc/edit#slide=id.gcae1e2fa1_0_10', _target='blank'),
                _class="col-sm-12"),
            _class="container", _style="padding:10px 10%;"),
        _class='row', _id='list', _style="padding-bottom:10px;")

    return dict(h = DIV(h, _class='container'))

def invite():
    form = SQLFORM(db.crew,
        # fields = ['email'],
        submit_button = T('Присоединиться'),
        #labels = {'email': T('Ваш емэйл')  },
        formstyle='divs',
        )
    if form.accepts(request.vars, session):
        response.flash = T('Вы внесены')
    elif form.errors:
        response.flash = T('ОШИБКА!')
    else:
        print request.ajax, request.vars
        response.flash = T('MISSed')

    return locals()
