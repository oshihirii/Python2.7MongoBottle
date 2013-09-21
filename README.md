Python2.7MongoBottle
======================================

This is a bare bones example of setting up a Python 2.7 app on OpenShift with:

- MongoDB
- RockMongo
- PyMongo
- Bottle

At the end of this tutorial, your browser should output:

    Your result is:
    
    Here is some content.
    
The value `Here is some content.` will be pulled from a MongoDB database.  
    
Your application directory structure will look like this:

    app.py.disabled
    - data
    -- .gitkeep
    - libs
    -- .gitkeep
    README.md
    setup.py *
    setup.pyc
    setup.pyo
    - wsgi
    -- application *
    -- mybottleapp.py *
    -- static
    --- README
    -- views *
    --- page1.tpl *
    .git
    -- git stuff in here
    .openshift
    -- openshift stuff in here
    
The files and folders highlighted with asterixes above are the only ones you will need to modify when following this tutorial.  

**Set Up OpenShift Online Account and Install Client Tools (on Fedora)**

**01** -- Create an account on http://openshift.com

**02** -- Download and install the Clients Tools via the terminal with:

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
        
**03** -- Update Client Tools with:

        [me@my my_openshift_apps] su
        Password:
        [root@my my_openshift_apps] gem update rhc
        [root@my username] exit # exit from super user

**Steps To Create Application**

In your terminal, from within the folder where you would like your application folder created eg `my_openshift_apps`:  


**04** -- `rhc app create YourAppName python-2.7`   // Create the Python application.

**05** -- `rhc cartridge add mongodb-2.2 -a YourAppName`   // Add the MongoDB cartridge (keep details somewhere safe).

**06** -- `rhc cartridge add rockmongo-1.1 -a YourAppName`   // Add the RockMongo cartridge (keep details somewhere safe).

**07** -- Go to `YourAppName-YourNameSpace.rhcloud.com/rockmongo`

**08** -- Create a collection in the database named after your app called `myCollection`.

**09** -- Insert a document with this data:


    {
    "content":"Here is some content."
    "blah":1
    }


**10** -- In your local application folder, replace the contents of the `setup.py` file with those from the same file in this repo.

**11** -- In your local application folder, in the `wsgi` folder, replace the contents of the `application` file with those from the same file in this repo. 

**12** -- In your local application folder, in the `wsgi` folder, create a file called `mybottleapp.py` and add contents from the same file in this repo.

**13** -- In your local application folder, in the `wsgi` folder, create a folder called `views` and add the file from this repo called `page1.tpl`.  

**14** -- Add, commit and push as usual:  

        git add --all :/
        git commit -m "add your message here"
        git push
