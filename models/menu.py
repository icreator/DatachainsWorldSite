# -*- coding: utf-8 -*-

if request.ajax:
    pass
else:
    desc = '...'
    url = URL(scheme=True, host=True) + '/'
    img_src=URL('static','images/block-to-data.png') #,scheme=True, host=True)
    title = 'Data Chains World'
    ## read more at http://dev.w3.org/html5/markup/meta.name.html
    response.meta = dict(
        author = 'iCreator <icreator@mail.ru>',
        description = desc,
        keywords = 'datachain, blockchain, sidechain, multichain',
        generator = 'iCreator by Web2py',
        url = url,
        d1 = { 'content':title, 'property':"og:title" },
        d2 = { 'content': desc, 'property':"og:description" },
        d3 = { 'content': url, 'property':"og:url" },
        sn = { 'content': 'DataChains World', 'property':"og:site_name" },
        image = { 'content': img_src, 'property':"og:image" },
        image_w = { 'content': '955', 'property':"og:image:width" },
        image_h = { 'content': '756', 'property':"og:image:height" },
        )

    ## your http://google.com/analytics id
    response.google_analytics_id = None

    if IS_MOBILE:
        response.top_line = None
    elif request.controller == 'cards':
        response.top_line = DIV(
            TAG.center(
                H1(B(SPAN('DATA', _style='color:chartreuse;'), SPAN('CHAINS', _style='color:gold;'),
                     SPAN('.WORLD', _style='color:powderblue;'),
                  ), _style='font-size:60px;text-shadow:1px 1px 2px black, 0em 0em 0em #00F1FF'),
                #H1('The Gobal Financial Revolution', _style='color:deepskyblue;text-shadow: 3px 3px 5px black, 0em 0em 0em #000;'),
                H2(T('BLOCKCHAIN для банков и платёжных систем')),
                #H3('Bitcoin rise the blockchain. Blockchain rise the sidechains. Sidechains rise the privatechains.'),
                #2('But all its is DATACHAINS!'),
            ),
            _class='container-fluid bgi_h1', _style='background:#FFF; color: #666',
            _id="top_line")
    else:
        response.top_line = DIV(
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
