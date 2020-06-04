import   pymysql


def get_tables():
    db=pymysql.connect(host='192.168.106.134',
                       port=3306,
                       user='axe',
                       password='root.2018' )
    cursor=db.cursor()
    sql='''select  table_name from  information_schema.tables  where table_schema='axe' ; '''
    cursor.execute(sql)
    data =cursor.fetchall()
    print(data)
    cursor.close()
    db.close()
