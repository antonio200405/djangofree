from peewee import *

user = 'djangofree'
password = '@djangofree12'
db_name = 'free'

conn = MySQLDatabase(
    db_name, user=user,
    password=password,
    host='localhost'
)