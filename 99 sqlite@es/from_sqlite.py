#导入数据库驱动 python内建sqlite3驱动 无需加载外部文件

import sqlite3

class sqlite3data(object):

    def __init__(self,sqlite_add):
        self._add =sqlite_add
 
#获得数据
    def getData(self):

        try:
            #连接数据库
            conn = sqlite3.connect(self._add)

            #创建游标
            cursor = conn.cursor()

            #查询数据
            sql = "select * from table1"
            cursor.execute(sql)

            values = cursor.fetchall()

            print("table date is:",values)
            return values


        except Exception :
            raise
        finally:
            cursor.close()
            #提交事务
            conn.commit()
            #关闭连接
            conn.close() 




