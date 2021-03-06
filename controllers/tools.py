# -*- coding: utf-8 -*-

if request.ajax:
    if not request.is_local:
        raise HTTP(501, 'error')
else:
    if not IS_LOCAL:
        raise HTTP(501, 'error')

def getInvestorList():
    CASH_INV_A = 9
    
    res = {}
    
    for rec in  db((db.man_bals.bal > 0)
             & (db.man_bals.cash_id == CASH_INV_A)).select():
        acc = db(db.man_accs.bal_id == rec.id).select().first()
        if acc and acc.acc and len(acc.acc) > 25:
            res[acc.acc] = int(rec.bal)

    return '%s' % res

def invList():
    
    inv = {'7J1S62H1YrVhPcLibcUtA2vFACMtiLakMA': 5000, '73igNXcJbLZxoM989B2yj4214oztMHoLGc': 170, '74MxuwvW8EhtJKZqF7McbcAMzu5V5bnQap': 1000,
           '7Cp622VhpUwpzWnzDV3XyPepVM5AF682UF': 5000, '7PnyFvPSVxczqueXfmjtwZNXN54vU9Zxsw': 360000, '7ANHQck4rANJ5K2RsF1aAGYYTyshpFP4cM': 4388,
           'CmmGpEbumf3FspKEC9zTzpFTk86ibLRwEbqxZ3GuAykL': 600, '7JU8UTuREAJG2yht5ASn7o1Ur34P1nvTk5': 470000, '7DedW8f87pSDiRnDArq381DNn1FsTBa68Y': 550000,
           '7K4XaDVf98J1fKDdCS8oYofYgFgoezFEAA': 5000, '7EMFYDJW2mxBAPDgWsVbAULMSx5BzhC9tq': 7250,
           '7JMtB4zjEyig1sfBqFTHdvuPqvbtmaQcvL': 3333, '7LPhKZXmd6miLE9XxWZciabydoC8vf4f64': 13000,
           '7Gdt8ZdiFuHrwe9zdLcsE1cKtoFVLDqyho': 8910, '7Pw2u4k2QBxrrUYsoaaBTCkdsYDK7wvS1X': 27500,
           '79VxiuxRgFTp8cUTRDBAoZPGXEdqY7hD8h': 1000, '7NeUmKbZadHLwS9FfLdhFL4ymVYSieF9Uc': 500,
           '7ARdsYAd4c92mHUofN7fLS8C3VeMwbTJAr': 550, '7LcwdEBZWVyFyaFhFoGC3SUxyqH5Uo9Zrq': 5555,
           '79qUjyTW4VoSgMKpF2dLW9eCwGVTSSnP2H': 1950, '7QqeSR442vstwcf5Hzm3t2pWgqupQNxRTv': 1000, '76UjGyQ4TG9buoK8yQ1PmW2GE6PoPAEDZw': 5000,
           '78HfjphyuwWkLw7jMymcTM3UsRdXCE5auq': 1000, '7CbRHH27V9xsaqKfTzSqNwNFhxKLhbf4g5': 160, '7GWr8njMyjkDs1gdRAgQ6MaEp2DMkK26h7': 100000,
           '7A9FFw3mQfDrP9y8WCifrZ3pvsKwerkMLr': 5000, '77fdZVgXhnebykEmhuEkkxYxs7nFoTEWdP': 10000, '788AwMejUTX3tEcD5Leym8TTzKgbxVSgzr': 816,
           '7AfGz1FJ6tUnxxKSAHfcjroFEm8jSyVm7r': 4000, '7PrZEW6ZdkZDj5GMCCp918n7EbyHVf3mRa': 500, '79MXwfzHPDGWoQUgyPXRf2fxKuzY1osNsg': 60000,
           '77HyuCsr8u7f6znj2Lq8gXjK6DCG7osehs': 6925, '77QMFKSdY4ZsG8bFHynYdFNCmis9fNw5yP': 900000, '7LETj4cW4rLWBCN52CaXmzQDnhwkEcrv9G': 1300000,
           '7EM7P1neMZkw2EXr2kn15XMixfYVVTwvWF': 5500}
    sum1 = 0
    res = {}
    sss = ''
    for k, v in inv.iteritems():
        sum1 += v
        pp = v / Decimal(3.8768827156)
        res [ k ] = pp
        sss += 'Arrays.asList("%s", "%s"),<br />' % (k, round(pp,8))
    
    return sss

def activList():
    
    inv = {'73dXJb1orwqk1ADW364KEAzPVQNGa1vX9S': 50, '73igNXcJbLZxoM989B2yj4214oztMHoLGc': 1,
           '73yfeCDiSciBF1vc3PG8uyJMty4jRDxxL9': 1, '74MxuwvW8EhtJKZqF7McbcAMzu5V5bnQap': 105,
           '74Rcp979npxf6Q5zV6ZnpEnsxrsCHdXeNU': 1, '74rRXsxoKtVKJqN8z6t1zHfufBXsELF94y': 2,
           '75qZ6ncf5T4Gkz1vrwkqjCPJ1A5gr2Cyah': 1, '75rEoNUknMU3qYGjS3wriY53n1aRUznFus': 1,
           '75rVEuvpzhLJznkXZaYyxJq8L9pVCeqFbk': 1, '77GYw61CPhDhdHsHg8oYCaKhenq2izAps8': 1,
           '78Eo2dL898wzqXBn6zbGanEnwXtdDF2BWV': 1, '78HfjphyuwWkLw7jMymcTM3UsRdXCE5auq': 2,
           '78JFPWVVAVP3WW7S8HPgSkt24QF2vsGiS5': 100, '78KCkgNeSvxwtnVJTyzLFGGzmP8SUUuN1J': 1,
           '78cK2QS34j8cPLWwHDqCBy36ZmikiCzLcg': 1, '79gQ4iB4Cs8EkhrUanEiDQtKArt6k6NAdu': 1,
           '79qUjyTW4VoSgMKpF2dLW9eCwGVTSSnP2H': 1, '7A9FFw3mQfDrP9y8WCifrZ3pvsKwerkMLr': 1,
           '7AJNCwQvbEbGn7Mt3mzPHbK1Zxvy9t6xtA': 1, '7AXey16ivPRCQoFWzkMU4Q7V8FZugqjYUX': 15,
           '7CPGk25mTFGhANaBCiV4LqrowcUfrfLcRe': 1, '7Cy2J5ST6ukHSJVWtQd7eH4wbhbSBbMbZD': 1,
           '7D7S5veDCiAwvBCkoK4G2YqdXC4dZ3SH1Q': 1, '7DRH1MjEo3GgtySGsXjzfdqeQYagutXqeP': 1,
           '7DedW8f87pSDiRnDArq381DNn1FsTBa68Y': 1, '7FPm2tet9HTVmBMe5xvRzp4sWoS6d8PgWZ': 1,
           '7Fgkw8cuPiTc4LVRvkYBuXEEfGYxrg6XiX': 1, '7GWr8njMyjkDs1gdRAgQ6MaEp2DMkK26h7': 3,
           '7HWxbcgVRxzdxDiVj9oc5ZG39a93imLUWz': 1, '7J3M8xwJeG5gyBC5kLPb5c2kVHoTsMT5MK': 1,
           '7JNUfHeuCRLApKX9MievkAoGdFgVfBf7DE': 1, '7K4XaDVf98J1fKDdCS8oYofYgFgoezFEAA': 1,
           '7KcBS1bmK1NiYwJD1mgwhz1ZFWESviQthG': 1, '7Kh5KvHCuWAq8XHioKyUBZxRmbwCJZV5b2': 100,
           '7MPmVWSobucE6TdJvnEeohFAZnCej7fr2F': 1, '7NeUmKbZadHLwS9FfLdhFL4ymVYSieF9Uc': 1,
           '7PnyFvPSVxczqueXfmjtwZNXN54vU9Zxsw': 1}
    sum1 = 0
    for k, v in inv.iteritems():
        sum1 += v

    res = {}
    sss = ''
    for k, v in inv.iteritems():

        pp =  500000.0 * v / sum1
        res [ k ] = pp
        sss += 'Arrays.asList("%s", "%s"),<br />' % (k, round(pp,8))
    
    return sss


# шлем рассылку в скрытых копиях
#mess = response.render('add_shop_mail.html', context)
def send_email_to_descr(to_addrs, subj, mess=None, rec=None, templ=None):
    mail_sets = myconf.take('email')

    from gluon.tools import Mail
    mail = Mail()
    mail.settings.server = mail_sets['server']
    mail.settings.sender = mail_sets['sender']
    mail.settings.login = mail_sets['login']
    
    mess = mess or ''
    if rec and templ:
        context = dict( rec = rec )
        mess = response.render(templ, context)

    print 'sensed to:', to_addrs
    mail.send(
          to = to_addrs[0],
          #cc=len(to_addrs)>1 and to_addrs[1:] or None, - как спам коипии делает (
          bcc=len(to_addrs)>1 and to_addrs[1:] or None,
          subject = subj,
          message = '<html>%s</html>' % mess )


def mail_to_clients():
    subj = 'ERM4 v.3.01.07 СРОЧНО! DATACHAINS.World #14'
    h = CAT(
        H1('Срочно обновляемся до ERM4 v.3.01.07'),
        H3('Новости от блокчейн-проекта DATACHAINS.World #14'),
        P('Исправлена ошибка с форжерами, теперь Вы будете собирать больше блоков'),
        #CENTER(A(B(T('DataChainsWorld')), _href='http://datachainsworld.ru/', _target='blank', _style='color: red;')),
        CENTER(A(B(T('Загрузить')), _href='http://datachains.world/cabinet/download', _target='blank', _style='color: red;')),
        #P(A(B(T('Инструкция как и что делать')), _href='https://www.facebook.com/groups/datachains/', _target='blank', _style='color: red;'))
    )
    mess = '%s' % h
    ####send_email_to_descr('icreator@mail.ru',subj,mess)
    return mess
    to_addrs = []
    for r in db(db.men).select():
        to_addrs.append(r.email)
        if len( to_addrs ) > 5:
            send_email_to_descr(to_addrs, subj, mess)
            to_addrs = []
    if len(to_addrs)>0:
        send_email_to_descr(to_addrs, subj, mess)

##############
def index():
    return dict(message="hello from tools.py")
