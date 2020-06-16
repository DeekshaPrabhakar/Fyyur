import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
dialect = "postgres"
username = "postgres"
host = "localhost"
port = "5432"
databasename = "fyyur"
#'postgres://postgres@localhost:5432/fyyur'
SQLALCHEMY_DATABASE_URI = "{}://{}@{}:{}/{}".format(dialect, username, host, port, databasename) 
SQLALCHEMY_TRACK_MODIFICATIONS = False