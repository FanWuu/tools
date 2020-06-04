import  my_conn

def ddl_table(cloum_num):
    i=0
    ddl_sql=''
    while i <=cloum_num:

        cloun=' '.join('cloud'+str(i) , ' varchar(2)  default null' ,',' ,  '\n')
        ddl_sql=  ', '.join(ddl_sql, cloun)
        ddl='create table  test_1445 (' + ddl_sql +')  engine = innodb '
        i = i + 1

    return  ddl

if __name__ == '__main__':
    # a=my_conn.db_conn()
    create_table_sql =ddl_table(9999)
    print(create_table_sql)
    # a.execute(create_table_sql)
