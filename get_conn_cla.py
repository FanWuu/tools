import  pymysql

class dbpool():
    def __init__(self,host='192.168.152.132',port=6033,user='root',password='root.2019',database='axe'):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.database=database


    def get_conn(self):
        self.db=pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database)
        self.cur=self.db.cursor()

    def exec(self,sql):
        # self.get_conn()
        self.cur.execute(sql)
        self.db.commit()
        # self.close()

    def close(self):
        self.cur.close()
        self.db.close()

    def fetchdata(self):
        # self.exec(sql)
        # self.cur.fetchall()
        ss=self.cur.fetchall()
        # print(self.cur.fetchall())
        return   ss



if __name__ == '__main__':

    sql='''select  *  from  axe.cc;'''
    a=dbpool()
    a.get_conn()
    a.exec(sql)
    res=a.fetchdata()
    for i in res:
        print(i)
    a.close()
