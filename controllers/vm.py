# -*- coding: utf-8 -*-
# try something like

def amazon():
    response.not_show_function = True

    h = CAT(
        DIV(
            DIV(
                H2('AMAZON VM EC2', _class='center'),
                H4(T('Бесплатная виртуальная машина (ВМ) в облаке, на которой можно разместить несколько сайтов, магазинов и сервисов.')),
                P(T('Посмотрите инструкцию по запуску ВМ на'), ' ',
                      A('YouTube.com', TAG.i(_class='fa fa-youtube-play', _style='font-size:1.5em'),
                        _href='https://youtu.be/bBNTBn7zNL4', _class='white', _target='blank'),
                       ' ', T('или загрузить как файл в хорошем качестве'),' ',
                      A('tutor-vm.wmv', _href=URL('static', 'video/tutor-vm.wmv'), _class='white'),
                     '.'),

                P(T('Зарегистрируйтесь на хостинге'), ' ', A(B('Amazon'), _href='https://aws.amazon.com/ru/ec2/', _class='blue', _target='blank')),
                P(T('Вообще при входе в ВМ Вы окажетесь как на обычном компьютере - можете копировать файлы между ВМ и своим рабочим компьютером обычным образом через быстрые клавиши Ctrl-C и Crtl-V. Свернуть окно ВМ - нажать на иконку вверху ВМ, а переключаться на открытую ВМ - с помощью Alt-TAB.')),
                P(T('Внешний IP Вашей ВМ будет неизменным до тех пор, пока Вы не перезагрузите ее из личного кабинета Амазона. Перезагрузка ВМ обычным способом изнутри самой ВМ не меняет IP адрес её. Хотя Вы можете заплатить за постоянный IP.')),
                P(T('Чтобы ВМ работала, не выходите из нее, а просто закройте её окно.')),
                P(T('Для того чтобы подключиться к созданной ВМ - нажмите "Connet", скачайте файл .rdp и следуйте инструкциям.')),
                _class='container', _id='a'),
            _style='background-color:#ddd; color:#222;padding-bottom:30px;',
            _class=''),
        CENTER(IMG(_src=URL('static', 'images/tutor/amazon-01.png'))),
        DIV(
            DIV(
                CENTER(H3(T('Настройка полной ноды'))),
                P(T('Вам нужно разрешиь доступ извне по заданным портам, для этого откройте Группы секретности (Security groups) и выберите там Входящие правила (inbound). Затем нажмите Edit и введите новое правило на нужные порты как показано ниже.')),
                _class='container'),
            _style='background-color:#ddd; color:#222;padding-bottom:30px;',
            _class=''),
        CENTER(IMG(_src=URL('static', 'images/tutor/amazon-02.png'))),
        DIV(
            DIV(
                P(T('Задайте порты и правило для весх IP и т.д. как показано ниже.')),
                _class='container'),
            _style='background-color:#ddd; color:#222;padding-bottom:30px;',
            _class=''),
        CENTER(IMG(_src=URL('static', 'images/tutor/amazon-03.png'))),
        DIV(
            DIV(CENTER(H2(T('Настройка внутри ВМ'))),
                P(T('Теперь задайте входные правила внутри ВМ через Firewall')),
                _class='container'),
            _style='background-color:#ddd; color:#222;padding-bottom:30px;',
            _class=''),
        CENTER(IMG(_src=URL('static', 'images/tutor/amazon-04.png'))),
        DIV(
            DIV(
                P(T('Найти и открыть файревол.')),
                P(T('Создать входящее правило для нужных портов:')),
                _class='container'),
            _style='background-color:#ddd; color:#222;padding-bottom:30px;',
            _class=''),
        CENTER(IMG(_src=URL('static', 'images/tutor/amazon-05.png'))),
        CENTER(IMG(_src=URL('static', 'images/tutor/amazon-06.png'))),
        DIV(
            DIV(P(T('Теперь Ваша ВМ есть полная нода блокчейн-среды. Проверить можно в программе-клиентк блокчен-среды - при просмотре подключенных внешних узлов (пиров): Заходим в Меню, Отладка, Пиры. Если в списке пиров есть входящие подключения (remote), значит все работает как надо.')),
                _class='container'),
            _style='background-color:#ddd; color:#222;padding-bottom:30px;',
            _class=''),
    )
    return dict(h = h)

def index():
    response.title=T('Виртуальные машины в оюлаках')
    response.not_show_function = True

    h = CAT(
        H2(T('Как создать полную ноду в облаке')),
        H4(T('Такая нода будет работать круглосуточно зарабатывая для Вас комиссии с созданных блоков')),
        H3('Amazon'),
        P(T('Для того чтобы сделать полную ноду на Amazon: запускаем там Instanse free EC2 (это бесплатная на целый год виртуальная машина (ВМ), у неё настраиваем группу секретности, -там входное правило делаем на нужный порт TCP (9191 + для веб-експлорера) для всех IP. Затем внутри ВМ открываем Firewall и там добавляем входящее правило на те же локальные порты. Теперь Ваша ВМ есть полная нода блокчейн-среды. Проверить можно в просмотре пиров - если есть входящие подключения, значит все работает как надо.')),
        P(T('Вы можете взять виртуальную машину на Амазон бесплатно на целый год. Достаточно указать банковскую карту для проведения пробного платежа. Через год стоимость будет порядка 3-х долларов в месяц.'), ' ',
         A(B(T('Подробнее')), _href=URL('amazon'), _class='blue')),
        )
    
    return dict( h = DIV(h, _class='container'))
