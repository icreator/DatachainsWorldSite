# -*- coding: utf-8 -*-
# try something like

def index():
    
    session.forget(response)
    response.title=T('Зажги Солнце блокчейна')
    response.not_show_function = True

    
    h = DIV(
        DIV(
            DIV(
                DIV(
                    CENTER(H1(T('День "Д" настал'))),
                    H3(P(T('Настал день "Д", настал час "Ч"! И наконец мы можем увековечить себя в истории и заработать на этом, УРА - запускаем блокчейн 3-го поколения! И приглашаем Вас стать привилегированным пользователем нашего блокчейна, с записью в генесиз-блок!'))),
                    DIV(
                        DIV(
                            _class='col-sm-2'),
                        DIV(
                            H4(P('+ ', XML(T('Вы получаете <span style="color:cyan;">пакет для форжинга</span>, с помощью которого Ваш компьютер сможет зарабатывать деньги c самого первого блока!')))),
                            H4(P('+ ', XML(T('Вы становитесь <span style="color:cyan;">отцом-основателем</span> блокчейн-среды 3-го поколения, с правом решать вопросы и голосовать об её изменениях!')))),
                            H4(P('+ ', XML(T('Вы <span style="color:cyan;">становитесь вершиной</span> своей собственной и одновременно первой в мире реферальной сети на блокчейне, глубина которой достигает 9-ти уровней!')))),
                            H4(P('+ ', XML(T('Вы становитесь не просто участником самого яркого события в мире блокчейн-технологий, а творите его вместе с нами: <span style="color:cyan;">именно Вы запускаете</span> первый блокчейн 3-го поколения, о котором все говорят, но никто живьём еще не видел!')))),
                            DIV(SPAN(T('7 ноября 2016, Дмитрий Ермолаев'), BR(), T('и команда стартапа DATACHAINS.World'), _class='pull-right')),
                            #DIV(T('и команда стартара DATACHAINS.World'), _class='row pull-right'),
                            _class='col-sm-10'),
                        _class='row'),
                        BR(),
                        #url("http://media.rusbase.vc/upload_tmp/shutterstock_179360048.jpg")
                        CENTER(
                            IMG(_SRC='http://media.rusbase.vc/upload_tmp/shutterstock_179360048.jpg', _height=300),
                            H1(A(B(T('Поехали!')), _class='btn-lg btn-for', _href=URL('sun_a', 'index')))),
                    
                    _class='col-sm-12'),
                    _class='row'),
                _class='container orange',
               _style='color:white; text-shadow:0.15em 0.15em 0.3em black; max-height-:500px; min-height: 500px; padding:20px 60px;'),
        _style='max-height:500px; min-height: 500px;',
        _id='box_bg') # for backstretch JS


    return dict( h = h )
