import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': 'ufm.12345',
    'host': '34.71.78.61',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem'
}

# now we establish our connection
cnxn = mysql.connector.connect(**config)

config['database'] = 'final_os'  # add new database to config dict
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()

cursor = cnxn.cursor()  # initialize connection cursor
cursor.execute('INSERT INTO leads () VALUES ()')  # create a new 'testdb' database
cnxn.close()  # close connection because we will be reconnecting to testdb