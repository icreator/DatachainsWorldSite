# -*- coding: utf-8 -*-
# try something like


def index():
    
    session.forget(response)
    response.title=T('Первый раунд продажи акций ICO')
    response.not_show_function = True

    shareA_ID = 9

    cash_A = db.cash[shareA_ID]

    h = CAT()
    
    col1 = '3'
    col2 = '9'
    data1 = '2016-11-12'

    total = -cash_A.own_bal

    ERA = 10000000
    ICO_PERC = 30
    ERA_PERC = ICO_PERC * ERA / 100
    ERA_COST = total / ERA_PERC
    if (ERA_COST < 1 ):
        ERA_COST = 1
        
    h += DIV(
        DIV(
            H2(T('Программа начального предложения долей (ICO) блокчейн-среды для юридических и физических лиц "E-Share U"')),
            P(T('Эта программа предназначена для безналичной оплаты долей блокчейн-среды (покупка единиц ERA) путём оплаты паевых взносов в'), ' ',
              A(T('Инновационное потребительское общество "Польза"'),'.', _href='http://ipo-polza.ru', _target='blank', _class='white'),' ',
              T('Вы получите основные учётные единицы ERA, которые по сути являются акциями нашей блокчейн-среды, после старта блокчейн-среды. Также эта программа предоставляет пакет документов на основе законов РФ для юридического использования нашей блокчейн-среды в бизнесе и предпринимательстве - для выпуска векселей, заключения электронных договоров в блокчейне, пересылке в блокчейне заказных писем с уведомлением, для учета обмена имущества (бартер) с партнерами, для создания нового типа юридических лиц с электронным выпуском акций и голосованиями на блокчейн'), '. '),
            
            P(T('Платежи (в виде паевых взносов), поступившие на банковские счета ИПО "Польза" до старта среды будут иметь 15%-ю скидку при переводе их в целевую программу, которая будет учитывать владение этой долей единиц ERA. Надо понимать что цена единиц ERA будет со временем расти и паевые взносы например через год могут дать меньшее число ERA в собственность, чем при запуске среды. К тому же, участники данной целевой программы могут сами решать по какой цене впускать нового инвестора.')),
            P(T('С помощью единиц ERA можно самому форжить сдавать в их аренду форжерам, а также они дают право на удостоверение новых участников и голосовать по глобальным вопросам блокчейна'), '. '),
        _class='container'),
        _style='background-color:#ddd; color:#222; padding-bottom:30px;')
    h += DIV(
        DIV(
            CENTER(H2(T('Данные предложения и текущая цена'))),
            P(T('Всего будет выпущено единиц ERA'), ': ', B(ERA / 1000000), ' ', T('миллионов')),
            P(T('Доля выставленная на продажу в этой программе'), ': ', B(ICO_PERC), '%'),
            P(T('Доля выставленная на продажу в этой программе в единицах ERA'), ': ', B(ERA_PERC), ' ', T('штук')),
            #P(T('Всего собрано инвестиций в рублях'), ': ', B(total)),
            P(T('Текущая цена одной единицы ERA в рублях'), ': ', B(ERA_COST)),
            P(T('Капитализация'), ': ', B(round(float(ERA_COST * ERA * Decimal(0.000001)), 6)), ' ', T('миллионов рублей')),
        _class='container'),
        _style='background-color:#fff; color:#222; padding-bottom:30px;')
    h += DIV(
        DIV(
            H3(T('Вдобавок Вы получите')),
            P(B(T('Форжинг'),'.'), ' ', T('Вы будете получать прибыль от чеканки звеньев (форжинга блоков) с помощью своих ERA. Что такое форжинг описано в'), ' ', A(T('Программа старта'),'.', _href=URL('sun_a', 'index'), _class='white')),
            P(B(T('Вершина'),'.'), ' ', T('Вы получаете возможность создать реферальную сеть приглашая новых пользователей в общую блокчейн-среду. Вы будете получать награду с каждого приглашенного и от его приглашенных вглубь на 7-9 уровней. Таким образом Вы становитесь вершиной реферальной программы. Причем, абсолютно все транзакции в этой структуре будут автоматически приносить Вам прибыль, - для этого даже не нужно держать компьютер включенным и заниматься чеканкой. А так как блокчейн будет работать всегда, то это пассивный доход на всю жизнь! Что такое "вершина" и реферальная сеть в блокчейне описано в'), ' ', A(T('Программа старта'),'.', _href=URL('sun_a', 'index'), _class='white')),
            P(B(T('Гордость'),'.'), ' ', T('И наконец, Вы получите моральное удовлетворение и гордость за себя, так как наш блокчейн несёт великие улучшения для предпринимателей и обычных граждан. Это в первую очередь бесплатная личная усиленная электронная подпись и другие возможности использования, которые описаны тут:'), ' ',
                A(T('Блокчейн 3.0 для бизнеса'), _class='blue',
                    _href=URL('bc3biz','index')),' ', T('и'), ' ',
                A(T('Блокчейн 3.0 для граждан'), _class='blue',
                    _href=URL('bc3liv','index')),' ', T('и'), ' ',
                A(T('Блокчейн 3.0 для государства'), _class='blue',
                    _href=URL('bc3gov','index')),
                 ),

            P(T('Распределение акций можно увидеть в'),' ',
              A(T('блокчейн-эксплорере'), _target='blank', _class='white',
               _href='http://188.65.212.60:9057/index/blockexplorer.html?top=allnotzero&asset=32'), _class='orange'),

            P(T('Чтобы выкупить долю по этой программе - свяжитесь с нами (контакты вверху в меню справа)')),
            BR(),

            ###P(T('У нас уже %s+ участников!') % (50 + counter_rec), _class='orange'),
            DIV(CENTER(
                A(T('Стать Акционером!'), _href=URL('default','contacts', args=[shareA_ID]),
                  _class="btn btn-one btn-lg", _style="background-color:slategrey; font-size: 26px; margin-top: 30px; margin-left: 20px; padding: 10px 40px;"),
                  ),
            _style='',
            _class='row'),
            H2(T('Вопросы и Ответы')),
            DIV(B(T('Если я потеряю СИД (длинный секретный ключ для восстановления кошелька) и уничтожу файл кошелька wallet.dat или папку с ним /wallet, то можно ли его восстановить?'))),
            P(T('Нельзя, все средства на счетах этого кошелька будут утеряны навсегда.')),
            DIV(B(T('Когда планируется запуск боевой версии блокчейн среды?'))),
            P('17.01.2017'),
            DIV(B(T('Сколько будет выпущено основных учётных единиц ERA ("золотых монет")? И когда?'))),
            P(T('Всего будет выпущено 10 миллионов ERA разово в генесиз-блоке.')),
            DIV(B(T('Кому будут принадлежать выпущенные в генесиз-блоке единицы ERA?'))),
            P(T('Разработчикам и инвесторам.')),
            DIV(B(T('Будут ли еще выпускаться единицы ERA?'))),
            P(T('Нет')),
            DIV(B(T('Каким образом форжер получает “пакет форжинга” или единицы ERA?'))),
            P(T('В генесиз-блоке создаются специальные транзакции - передача в аренду форжеру единиц ERA, после чего он может форжить блоки до тех пор пока не кончится аренда.')),
            DIV(B(T('Сколько будет выпущено рабочих учётных единиц COMPU ("серебряных монет")? И когда?'))),
            P(T('Без ограничений, а разово в генесиз-блоке будет выпущено всего 10 COMPU.')),
            DIV(B(T('Кому будут принадлежать выпущенные в генесиз-блоке единицы COMPU?'))),
            P(T('Форжерам.')),
            DIV(B(T('Будут ли еще выпускаться единицы COMPU?'))),
            UL(T('Да, в блоке в котором мало транзакций, из расчёта величины равной 10-ти комиссиям от средней по размеру транзакции.'),
                T('И при появлении в блокчейне новой зарегистрированной персоны - как комиссия за примерно 70 транзакций.')),
            DIV(B(T('Какой уровень в глубину могут собрать под собой реферальную сеть участники, которые были приглашены в блокчейн после его запуска (то есть которые не были внесены в генесиз-блок)?'))),
            P(T('такой же как и те кто является вершиной. Просто им будет сложнее привлечь новых участников, которые еще не вошли в наш блокчейн.')),
            DIV(B(T('Какие требования к компьютеру для форжинга?'))),
            P(T('Должен быть установлен пакет Java, свободная память 1Гб, процессор 1 ядро.')),
            DIV(B(T('Обязательно ли брать виртуальную машину в облаке и чем она лучше?'))),
            P(T('ВМ лучше только тем, что она крутится независимо от интернета и электричества в Вашем доме - 24 часа каждый божий день, то есть это очень надежный компьютер. Если Вы не собираетесь заниматься профессионально форжингом, то хватит разового ключения комптютера днем на 3-5 часов.')),
            DIV(B(T('Чем отличается Ваша реферальная система учёта в блокчейне от МЛМ и сетевого маркетинга? Чем это отличается от пирамиды?'))),
            P(T('Рефералы - это приглашенные люди. По сути реферальная система - это сетевая структура. Но у нас не нужно от приглашенного что-то требовать купить или внести какие-то деньги в систему. Тут просто некуда вносить - нет центра. Тут есть множество равноправных “вершин”, которые к нам никак не относятся и полностью самостоятельные - это форжеры, которые войдут в генесиз-блок, - только они могут быть “вершиной”, которая больше никому не платит. Пирамида же имеет обязательный признак - нужно принести деньги и отдать их тому кто тебя пригласил, оплачивая ему его доход. У нас доход форжеров оплачивают инвесторы, а не рефералы. Мы для инвесторов расходное предприятие.')),
            DIV(B(T('Как и с чего участники получают доход со своих рефералов?'))),
            P(T('1/8-я от комиссий с транзакций идёт на реферальную сеть вверх по цепочке на 9 уровней. И если цепочка приглашений вышла на “вершину”, то весь остаток нераспределенных доходов достаётся вершине.')),
            DIV(B(T('Можно ли стать “вершиной” после запуска блокчейна, то есть по другой программе продажи пакетов форжинга?'))),
            P(T('Нет, это чисто технически невозможно. Вершина создаётся только у тех, кто внесён в генесиз-блок.')),
            DIV(B(T('Сколько участников может вместиться в генесиз-блок?'))),
            P(T('До 10 000 человек')),
            DIV(B(T('Инвесторы могут быть анонимными?'))),
            P(T('Да могут. Просто оплачиваете взнос биткоинами, конвертируете их во внутреннюю валюту "Рубли", а затем оплачиваете взнос в эту программу. При этом счет в блокчейне 3.0 тоже остается анонимным, до тех пор пока Вы его не удостоверите. Однако в этом случае Вы не сможете приглашать рефрералов. Зато можете продавать свою долю единиц ERA и использовать их для форжинга.')),
            DIV(B(T(''))),
            P(T('')),
        _class='container'),
        _style='background-color:#ddd; color:#222; padding-bottom:30px;')

    return dict( h = h )
