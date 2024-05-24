import pymysql

def get_db_connnection():
    connection = pymysql.connect(host='',
                                 user='admin',
                                 password='password',
                                 db='utez',
                                 charset='utf8mb4',
                                 cursosclass=pymysql.cursors.DicCurso)
    return connection