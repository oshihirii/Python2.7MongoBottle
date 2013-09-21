from bottle import route, default_app, template, view, TEMPLATE_PATH
import pymongo
import os
 
@route('/')
def index():
    try:
        dbname = 'mydbname'
        connection = pymongo.MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])
        db = connection[dbname]
    except:
         return ("Couldn't connect to database")
    collection = db.myCollection
    query = {'blah':1}
    projection = {'content': 1, '_id': 0}
    cursor = collection.find_one(query,projection)
    try:
        return template('page1',{'dbresult':cursor['content']})
    except:
        return ("Problem passing data to template")

TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
    'app-root/repo/wsgi/views/')) 

application=default_app()
