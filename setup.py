from setuptools import setup

setup(name='YourAppName', version='1.0',
      description='Enter a description here',
      author='Your Name', author_email='youremail@example.org',
      url='http://www.your-url.com',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['WebOb',
                          'bottle',
                        #  'mysql-connector-python',
                          'pymongo',
                        #  'psycopg2',
      ],
     )
