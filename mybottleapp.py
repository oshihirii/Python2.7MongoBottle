from bottle import route, default_app, template, view
import pymongo
 
@route('/')
def index():
    try:
        dbhost = 'admin:password@127.x.xx.xxx:27017/'
        dbname = 'mydbname'
        connection = pymongo.MongoClient("mongodb://" + dbhost)
        db = connection[dbname]
    except:
         return ("Couldn't connect to database")
    collection = db.myCollection
    query = {'blah':1}
    projection = {'content': 1, '_id': 0}
    cursor = collection.find_one(query,projection)
    try:
        return template('page1',{'dbresult':cursor})
    except:
        return ("Problem passing data to template")

import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
    'app-root/repo/wsgi/views/')) 

application=default_app()
