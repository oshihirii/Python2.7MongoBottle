Python2.7MongoBottle
======================================

Bare bones example of setting up a Python 2.7 app on OpenShift with:

- MongoDB
- RockMongo
- PyMongo
- Bottle

**Steps**

In your terminal, from within the folder where you would like your application folder created:  


**01** -- `rhc app create YourAppName python-2.7`   // Create the Python application.

**02** -- `rhc cartridge add mongodb-2.2 -a YourAppName`   // Add the MongoDB cartridge (keep details somewhere safe).

**03** -- `rhc cartridge add rockmongo-1.1 -a YourAppName`   // Add the RockMongo cartridge (keep details somewhere safe).

**04** -- Go to `YourAppName-YourNameSpace.rhcloud.com/rockmongo`

**05** -- Create a collection in the database named after your app called `myCollection`.

**06** -- Insert a document with this data:


    {
    "content":"Here is some content."
    }


**07** -- In your local application folder, replace the contents of the `setup.py` file with those from the same file in this repo.

Notes:

- The `setup.py` file was originally from https://github.com/openshift-quickstart/Bottle-Python3-quickstart/blob/master/setup.py
- This step will install PyMongo and Bottle.

**08** -- SSH in to your app with `rhc ssh YourAppName`, type `env` and press `Enter`.

**09** -- Locate, copy and keep the the values from the following environment variables somewhere safe:

        $OPENSHIFT_MONGODB_DB_HOST
        $OPENSHIFT_PYTHON_IP
        $OPENSHIFT_PYTHON_PORT

**10** -- In your local application folder, in the `wsgi` folder, replace the contents of the `application` file with those from the same file in this repo.  

**11** -- In your local application folder, in the `wsgi` folder, create a folder called `views` and add the file from this repo called `page1.tpl`.  

**12** -- Add, commit and push as usual:  

        git add --all :/
        git commit -m "add your message here"
        git push
