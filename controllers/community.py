# -*- coding: utf-8 -*-

response.generic_patterns = ['*.html']

session.forget()

def vacant():
    response.title=T('Вакансии')
    response.not_show_function = True
    h = CAT(
        DIV(
            DIV(
        CENTER(H2(T('Вакансии'))),
        P(T('вакансии размещены в разделе на форуме проекта'), ': ', A('DataChainsWorld.ru', _href='http://datachainsworld.ru/index.php?board=16.0', _target='blank', _class='white')),
                
                BR(),
        _class='row'),
        _class='container'),
        )
    return dict(h =h)

##@cache.action(time_expire=cache_expire, cache_model=cache.ram, quick='P')
def index():
    response.title=T('Сообщество')
    response.not_show_function = True
    h = CAT(
        DIV(
            DIV(
        CENTER(H2(T('Сообщество'))),
        H3(T('Форумы')),
        P(T('Форум проекта'), ': ', A('DataChainsWorld.ru', _href='http://datachainsworld.ru/', _target='blank', _class='white')),
        P(T('Slack'), ': ', A('datachains.slack.com/messages/@slackbot/', _href='https://datachains.slack.com/messages/@slackbot/', _target='blank', _class='white')),
                
        H3(T('Социальные сети')),
        P(T('Facebook'), ': ', A('DATACHAINS group', _href='https://www.facebook.com/groups/datachains/', _target='blank', _class='white'),
          ', ', A('DATACHAINS page', _href='https://www.facebook.com/datachains/', _target='blank', _class='white')),
        P(T('VK'), ': ', A('DATACHAINS group', _href='https://vk.com/datachains', _target='blank', _class='white')),
        H3(T('Месенжеры')),
        P(T('Telegram bot'),': @Datachainsbot'),
                
                BR(),
        _class='row'),
        _class='container'),
        )
    return dict(h =h)
