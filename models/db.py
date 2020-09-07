# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

##### for IDE
if False:
    pass


if not request.env.web2py_runtime_gae:
    migrate = 0
    fake_migrate = myconf.take('db.fake_migrate') and True or False
    migrate = (myconf.take('db.migrate') or migrate) and True or False
    ## if NOT running on Google App Engine use SQLite or other DB
    ## folder="../databases"
    if DEVELOP:
        db = DAL(myconf.take('db.uri_dvp'), check_reserved = ['all'],
                fake_migrate = fake_migrate,
                migrate = migrate
                )
    else:
        db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'],
                fake_migrate =fake_migrate,
                migrate = migrate
                )
    ## define session here
    session.connect(request,response, cookie_key = myconf.take('cookie.key'),compression_level=None)
    ###session.connect(request, response, db=db)
    ###session.connect(request, response, db = MEMDB(Client()))
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')
