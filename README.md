Python2.7MongoBottle
======================================

Work In Progress.  

Bare bones example of setting up a Python 2.7 app on OpenShift with:

- MongoDB
- RockMongo
- PyMongo
- Bottle

**Set Up OpenShift Online Account and Install Client Tools (on Fedora)**

- Create an account on http://openshift.com
- Download and install the Clients Tools via the terminal with:

        [me@my ~] su
        Password:
        [root@ymy username]  yum install rubygem-rhc
        [root@ymy username]  exit # exit from super user
        [me@my username]  mkdir my_openshift_apps # create a folder for your openshift apps
        [me@my username]  cd my_openshift_apps # navigate into that folder
        [me@my my_openshift_apps] rhc setup
        #  the login prompt refers to your username at openshift.com
        #  follow prompts to generate:
        #  token
        #  ssh keys
        #  a name for your namespace
        
- Update client tools with:

        [me@my my_openshift_apps] su
        Password:
        [root@my my_openshift_apps] gem update rhc
        [root@my username] exit # exit from super user

**Steps To Create Application**

In your terminal, from within the folder where you would like your application folder created eg `my_openshift_apps`:  


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
