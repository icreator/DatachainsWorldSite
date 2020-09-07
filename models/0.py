# -*- coding: utf-8 -*-

if False: # for IDEA
    from gluon import *
    request = current.request
    response = current.response
    session = current.session
    cache = current.cache
    T = current.T
    pass


### session is not defibed still here

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)

DEVELOP = myconf.take('app.develop', cast=bool)
APP_NAME = myconf.take('app.name')

#response.alert = CENTER(A(B(T('Внимание! Новая Боевая среда ERM4 v.3.01.01 запущена! Скачиваем, устанавливаем и запускаем. Необходимо пересоздавать кошелек из SEED')), _href='http://datachainsworld.ru/index.php?topic=39.0', _target='blank', _style='color: red;'))
response.alert = CENTER(A(B(T('Внимание! ERM4 v.3.01.07 обновление! Скачиваем, устанавливаем и запускаем.')), _href=URL('cabinet', 'download'), _target='blank', _style='color: red;'))

if request.ajax:
    ##session.forget(response)
    pass
else:
    from gluon import current
    current.IS_LOCAL = IS_LOCAL = request.is_local
    current.IS_MOBILE = IS_MOBILE = request.user_agent().is_mobile
    current.IS_TABLET = IS_TABLET = request.user_agent().is_tablet
    current.ADMIN = ADMIN = request.controller == 'appadmin'
    
    SKIN = myconf['skin']

    LANGS = {
        'ru': ['Русский', 'ru.png'],
        'en': ['English', 'gb.png'],
        'de': ['Deutsche ', 'de.png'],
        'tr': ['Türkçe', 'tr.png'],
    }

if DEVELOP:
    print 'in 0', request.ajax and 'AJAX' or '', request.url, request.env.REMOTE_ADDR, request.now
