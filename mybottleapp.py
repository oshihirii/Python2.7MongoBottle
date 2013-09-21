from bottle import route, default_app, template, view
import pymongo
 
@route('/')
@view('page1.tpl')
def index():
    try:
        dbhost = 'admin:password@127.x.xx.xxx:27017/'
        dbname = 'mydbname'
        connection = pymongo.MongoClient("mongodb://" + dbhost)
        db = connection.dbname
    except:
         return ("Couldn't connect to database")
    collection = db.myCollection
    result = collection.find_one()
    return template('page1',{'dbresult':result['content']})

import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
    'runtime/repo/wsgi/views/')) 

application=default_app()
