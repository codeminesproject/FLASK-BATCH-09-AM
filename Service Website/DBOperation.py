import config
import pymysql

def dbConnect():
    connection = pymysql.connect(host=config.DB_HOST,
                                 database=config.DB_NAME,
                                 user=config.DB_USERNAME,
                                 password=config.DB_PASSWORD,
                                 port=config.DB_PORT)
    if connection.open:
        return connection
    else:
        return None

def insert(query):
    connection = dbConnect()
    if connection!=None:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            return True
    else:
        return False

def getSingleData(query):
    connection = dbConnect()
    if connection!=None:
        with connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchone()
            return data
    else:
        return None
