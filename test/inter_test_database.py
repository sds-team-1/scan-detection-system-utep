import sys

sys.path.insert(0, '../')

from Database import DatabaseHelper

database = DatabaseHelper.SDSDatabaseHelper('mongodb://localhost:27017')

print('database variable ready')