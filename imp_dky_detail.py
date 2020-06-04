#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 15:28
# @Author  : wuuu__
# @File    : import_dky_tranw.py
# @Software: PyCharm
# 解析excle并写入mysql
import  xlrd
import  pymysql
file_path=r'C:\Users\wufan\Desktop\绕组明细.xlsx'
file = xlrd.open_workbook(file_path) #解析文件
sheet_1 = file.sheet_by_index(5)     #解析相应sheet页
row_count = sheet_1.nrows         #获取行数
def  excle_comtext(i):
    row_context=sheet_1.row_values(i)  #获取第i行数据
    cloud_id =row_context[1]         #获取第一列数据
    cloud_name=row_context[2]
    class_time_tag=row_context[3]

   # print(mrid,path_name)
    return cloud_id,cloud_name ,class_time_tag

def insert_database(data1,data2,data3):
    db = pymysql.connect(host='10.42.3.203',
                         port=3306,
                         user='root',
                         password='root.2011',
                         database='axe')
    cursor = db.cursor()
    db.autocommit(1)
    try:
        sql='''insert into  dky_relea_power_detail  (cloud_id , cloud_name , class_time_tag )  
                                            values ('%s','%s' , '%s')'''
        cursor.execute(sql%(data1,data2,data3))
    except pymysql.err.IntegrityError:
        print('出错了')

    # db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    for n in range(1,row_count):
        data=excle_comtext(n)
        # print(data[0],data[1])
        insert_database(data[0],data[1] , data[2])
        print('insert_database',(data[0],data[1] ,data[2]))
