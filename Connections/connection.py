
import pymysql.cursors

# Connect to the database
import pymysql
connection = pymysql.connect(unix_socket='/cloudsql/durable-cursor-307206:us-central1:os-final',
        user='root',
        password='ufm.12345',
        db='os-final',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO leads (nombre,telefono,fecha, ciudad, id_productor,fecha_inicio) VALUES ('Alex','12348765',timestamp,'Guatemala',1,timestamp)"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM leads"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
