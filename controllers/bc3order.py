# -*- coding: utf-8 -*-

if False: # for IDEA
    from gluon import *
    request = current.request
    response = current.response
    session = current.session
    cache = current.cache
    T = current.T
    pass

response.generic_patterns = ['*.html']

session.forget()

# переходник для показа ссыфлкок и картинок в листингах

##@cache.action(time_expire=cache_expire, cache_model=cache.ram, quick='P')
def index():
    response.not_show_function = True

    h = CAT(
        DIV(
            DIV(
                    H2(T('Основы блокчейн 3.0')),
                    P(T('Вообще блокчейн - это технология правдивого учёта, при котором все записи защищены от подлога и изменения, а создание каждой записи сопровождено электронной подписью создателя. При этом нет центрального посредника, который бы мог всё контролировать и вмешиваться, а взаимодействие сторон идёт напрямую между собой.')),
            BR(),
                    P(T('Все решения на нашем блокчейне приведены в  соответствие с законодательствами РФ и в доказательсво будут проведены показательные суды для признания действий учтённых в блокчейне как юридически-значимые.')),
            BR(),
                    P(T('Наш блокчейн 3-го поколения позволяет вести достоверный учёт юридических-значимых действий: подписание договоров, актов приёма-передачи, выпуск обязательств и их обращение, например векселей, голосования на собраниях акционеров и совета директоров и т.д.')),
                    P(T('Также наш блокчейн позволяет вести учёт должностей и статусов, назначений и например заявлений о приёме на работу.')),
                    P(T('Вдобавок Вы можете вести складской учёт, кто за что отвечает или сквозной трекинг вашего товара в транспортной сети своих подрядчиков.')),
            BR(),
                    P(T('Ещё Вы можете пользоваться встроенной товарно-сырьевой биржей, совершая юридически-значимые сделки напрямую со своими партнерами.')),
            BR(),
                    P(T('Причём учёт ведётся автоматически - при создании записи что товар принят, пример, на склад таким-то кладовщиком - ведь он подписывается своей электронной подписью в акте приёма товара или накладной. И вообще бумажных документов в этой среде не будет, а бухгалтерия (кроме зарплаты) будет считать автоматически без бухгалтеров (задумка на будущее).')),
            BR(),
                    P(T('Таким образом Вы можете выстроить безденежную экономику в своем регионе - на обмене напрямую товарами,  услугами и обязательствами их предоставить. Например нормо-час грузоперевозки 100 тонн груза  на 1 тонну зерна 3-й категории.')),
            BR(),
                    P(T('Для торговых сетей есть возможность выпускать подарочные электронные высоко защищенные от подделки подарочные сертификаты и единые бонусные карты, на  которых могут храниться все бонусные программы всех торговых сетей разом. Что даёт Вашим клиентам удобство для их накопления и обмена. И вообще торговые сети и потребительские общества могут перейти в будущем на выпуск “частных денег” в виде подарочных сертификатов или товарных талонов в блокчейне.')),
            BR(),
                    P(T('Для учебных заведений есть возможность вести учёт выданных сертификатов, дипломов, удостоверений и оценок учащимся - в результат чего работодателям не нужно получать от Вас справки - все данные об учёбе видны публично в блокчейне.')),
            BR(),
                    P(T('Для государственных служб и местного самоуправления есть возможность вести учёт разного рода статусов - воинских званий, инвалидностей, социальных статусов, гражданства, социальных льгот и выплат и т.д. Что резко сокращает расходы на обслуживание учёта и снижает время затрачиваемое гражданами на обращения в гос.органы, так как они самостоятельно могут вносить изменения в учёт с помощью своих заявлений, подписанных их личной удостоверенной электронной подписью.')),
                    H2(P(T('Создать свою собственную'), ' ',
                     A(T('блокчейн-среду 3-го поколения'), _href='https://docs.google.com/document/d/1PrEZBnlmavhQkuGVSMkgOXiLrfx3SFEXJhcDt47igdw/edit?usp=sharing',
                       _target='blabk', _class='white'))),
                    P(T('')),
                    _class='container', _id='product'),
            _style='background-color:#ddd; color:#222;padding-bottom:30px;',
            _class='row'),
            )
    return dict(h = h)
