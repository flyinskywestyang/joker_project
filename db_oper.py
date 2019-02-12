#db_oper.py
#数据库的访问类
import pymysql
import db_config 
#示例
class DBOPER:
    def __init__(self):
        self.host = db_config.host
        self.user = db_config.user
        self.password = db_config.password
        self.dbname = db_config.dbname
        self.db_conn = None
        
    def open_conn(self):
        try:
            self.db_conn = pymysql.connect(self.host,self.user,self.password,self.dbname)
        except Exception as e:
            print("数据库链接错误")
            print(e)
        else:
            print("数据库链接成功")

    def close_conn(self):
        try:
            self.db_conn.close()
        except Exception as e:
            print("数据库关闭错误")
            print(e)
        else:
            print("数据库关闭成功")

    def do_queue(self,sql):
        if not sql:#参数合法性判断
            print("SQL语句不合法")
            return None
        if sql == "":#参数合法性判断
            print("SQL语句不合法")
            return None
        try:
            cursor = self.db_conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()#只取出数据不进行处理
            cursor.close()
            return result
        except Exception as e:
            print("查询出错")
            print(e)
            return None

    def do_update(self,sql):
        if not sql:#参数合法性判断
            print("SQL语句不合法")
            return None
        if sql == "":#参数合法性判断
            print("SQL语句不合法")
            return None
        try:
            cursor = self.db_conn.cursor()
            result = cursor.execute(sql)
            self.db_conn.commit()
            cursor.close()
            return result#返回受影响笔数
        except Exception as e:
            print("SQL语句出错")
            print(e)
            return None

if __name__ == "__main__":
    dboper = DBOPER()
    dboper.open_conn()
    result = dboper.do_queue("select * from acct")
    for x in result:
        print(x)
    ret = dboper.do_update("insert into acct values('622345124310','yu','c010',1,date(now()),1,45325.45)") 
    if not ret:
        print("修改错误")
    else:
        print("影响笔数:%d"%ret)
    dboper.close_conn()     

#自己的思路
# class DBOPER:
#     def __init__(self):
#         pass
 
#     def open_conn(self):
#         conn = pymysql.connect(host,user,password,dbname)
#         return conn

#     def close_conn(self):
#         connect = self.open_conn()
#         connect.close()

#     # 执行查询返回结果
#     def do_queue(self,sql):
#         connect = self.open_conn()
#         cursor = connect.cursor()#获取游标
#         sqlist = sql 
#         tmp = cursor.execute(sqlist)#执行sql
#         connect.commit()
#         cursor.close()
#         self.close_conn()
#         return tmp

#     # 执行增删改等变更操作
#     def do_update(self,sql):
#         try:
#             connect = self.open_conn()
#             cursor = connect.cursor()#获取游标
#             sqlist = sql
#             tmp = cursor.execute(sqlist)#执行sql
#             connect.commit()
#             cursor.close()
#             print("插入成功！") 
#             except Exception as e:
#             connect.rollback()#出现异常回滚
#             print("数据库操作失败")
#             print(e)
#         finally:
#             self.close_conn()
#         return tmp

# if __name__ == "__main__":
#     dboper = DBOPER()
#     dboper.do_queue("select * from acct")
#     dboper.do_update("insert into acct values('622345124309','queue','c009',1,date(now()),1,24325.45)")
    


















