import sqlite3
from google.cloud import storage
import pandas as pd
import numpy as np
from datetime import datetime
import mysql.connector
import sys

cnx = mysql.connector.connect(user='root',password='ufm.12345',host='34.71.78.61',database='os-final')
cursor = cnx.cursor()
query1 = ('SELECT * FROM leads')
cursor.execute(query1)
frame = pd.DataFrame(cursor.fetchall())

frame.head()