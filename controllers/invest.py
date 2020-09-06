# -*- coding: utf-8 -*-


def index():
    session.forget(response)
    descr = T('Sell shares of blockchain startup - ICO')
    title = T('Краудинвестинг блокчейн стартапа - ICO')
    response.title= title
    response.not_show_function = True

    h = CAT(
    DIV(
        DIV(
            DIV(
                DIV(
            H1(title, _class='center'),
            P(T('ICO (initial coin offering) - сродни IPO - покупке акций компании перед её стартом. Но при ICO происходит покупка не акций, а основных учетных единиц среды -  токенов, монет и записи о покупке и распределении производятся в самом первом блоке блокчейна - в генесиз-блоке.')),
                        
            H2(T('Структура ICO')),
            P(T('5% для активистов и распространителей - по программе старта "Я Активист!"'), ' ',
              A(T('Подробнее.'), _href=URL('activ_a','index'), _class='white')),
            P(T('10% - ICO по свободной цене - по программе старта "E-Share A". Тут возможно анонимное участие через оплату биткоинами'), '. ',
              A(T('Подробнее.'), _href=URL('share_a','index'), _class='white')),
            P(T('10% - по фиксированной цене за 1 миллион рублей (1 ERA по цене 1 рубль). Первоочередное распределение между знакомыми и инвесторами, с которыми уже давно ведутся переговоры. Минимальная цена входа 10 тысяч рублей.'),
             A(T('Подробнее.'), _href=URL('share_f10','index'), _class='white')),
            P(T('30% - по свободной цене для юридических лиц и физических лиц в виде паевого участия в ИПО "Польза". Это распределение будет действовать и после запуска блокчейн среды, поэтому доли на это распределение будут постепенно передаваться из собственности команды по договорной цене'), '. ',
              A(T('Подробнее.'), _href=URL('share_u','index'), _class='white')
             ),
            P(T('Остаток, 45% остаётся пока у команды, но из них большая часть распределяется в генесиз-блоке между участниками программы старта "10 тысяч Звёзд" - это распределение повышает децентрализацию блокчейна с самого первого блока при его старте. Форжеры, участвующие в этой программе старта получают свои доли бесплатно, - но не в собственность, а в управление на время, пока не появятся новые инвесторы, желающие выкупить доли себе в собственность.')),
            P(T('Через полгода, начнётся мониториг форжеров и у тех, что недобросовестно исполняли свои обязонности, пакеты форжинга будут отозваны и выставлены на продажу для инвесторов или новых форжеров. Таким образом доля у команды будет снижаться'), '. '),
            P(T('10% резерв для стратегического партнера(ов).')),
            P(T('Итого у команды должно остаться 25%-я доля через год или два.')),
            H2(T('Цели ICO')),
            P(T('Собранные средства будут направлены на дальнейшее развитие блокчейн-среды 3-го поколения, внедрения решений на нём в жизнь в разных областях экономики, государства и жизни.')),
            
                    _class="col-sm-12"),
                _class="row"),
            _class="container", _style="padding:10px 10%;"),
            )
        )
    return dict(h =h)