#acct_manage.py
#账户管理类
#实现账户新增修改查询删除等逻辑处理
from db_oper import * 

class Acct:#账户类，仅用于数据传输
    def __init__(self,acct_no,acct_name,acct_type,balance):
        self.acct_no = acct_no
        self.acct_name = acct_name
        self.acct_type = acct_type
        self.balance = balance
    
    def __str__(self):
        ret = "帐号:%s,户名:%s,类型:%d,余额:%.2f"%(self.acct_no,self.acct_name,self.acct_type,self.balance)
        return ret

class Acct_Manage:#账户管理类
    def __init__(self,db_oper):
        self.db_oper = db_oper
    #查询所有账户信息
    def query_all_acct(self):
        accts = []
        #拼装所需SQL
        #执行查询 
        #返回结果
        sql = "select * from acct"
        result = self.db_oper.do_queue(sql)
        if not result:
            print("查询结果为空")
            return None
        for r in result:
            acct_no = r[0]
            acct_name = r[1]
            acct_type = int(r[3])
            balance = r[6]
            accts.append(Acct(acct_no,acct_name,acct_type,balance))
        return accts
    #根据账户查询
    def query_by_id(self,acct_no):
        sql = '''select * from acct where acct_no = %s''' % acct_no
        result = self.db_oper.do_queue(sql)
        if not result:
            print("查询返回空对象")
            return None
        #提取查询结果，实例化Acct对象返回
        r = result[0]#取得第一行数据
        acct_no = r[0]
        acct_name = r[1]
        acct_type = int(r[3])
        balance = r[6]
        return Acct(acct_no,acct_name,acct_type,balance)




