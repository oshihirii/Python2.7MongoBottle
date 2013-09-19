Python2.7MongoBottle
======================================

Bare bones example of setting up a Python 2.7 app on OpenShift with:

- MongoDB
- RockMongo
- PyMongo
- Bottle

**Steps**


**01** -- `rhc app create YourAppName python-2.7`   // create the python application

**02** -- `rhc cartridge add mongodb-2.2 -a YourAppName`   // add mongodb cartridge (keep details somewhere safe)

**03** -- `rhc cartridge add rockmongo-1.1 -a YourAppName`   // add rockmongo cartridge (keep details somewhere safe)

**04** -- go to app-namespace.rhcloud.com/rockmongo

**05** -- create a collection in the database named after your app called 'myCollection'

**06** -- insert a document with this data:


    {
    "content":"Here is some content."
    }


**07** -- in your local application folder, replace the contents of the setup.py file with those in the same file in this repo (originally from https://github.com/openshift-quickstart/Bottle-Python3-quickstart/blob/master/setup.py)
