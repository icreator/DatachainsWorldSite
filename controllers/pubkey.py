# -*- coding: utf-8 -*-

#response.generic_patterns = ['*.html']

session.forget()

# переходник для показа ссыфлкок и картинок в листингах

def get():
    pk = request.vars.get('acc')
    ##print len(pk), pk
    if pk and len(pk) > 40 and len(pk) < 50:
        rec = db(db.pubkeys.pubkey == pk).select().first()
        if rec:
            result = H3(T('ФИО'), ': ', B(rec.fio))
        else:
            import time
            time.sleep(3)
            result = H3("Ничего не найдено")
    else:
        import time
        time.sleep(3)
        result = H3("Ничего не найдено")
        
    response.js = "$('.go-btn').removeClass('disabled');$('#go').children('i').removeClass('fa-refresh fa-spin').addClass('fa-search');"
    return result

##@cache.action(time_expire=cache_expire, cache_model=cache.ram, quick='P')
def index():

    acc = request.args(0)
    
    return dict(acc=acc)
