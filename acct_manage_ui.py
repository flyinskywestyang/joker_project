#acct_manage_ui.py
from db_oper import *
from acct_manage import * 

if __name__ == "__main__":
    db_oper = DBOPER()#实例化数据访问对象
    db_oper.open_conn()#打开链接
    am = Acct_Manage(db_oper)
    
    menu = '''
    ----------------请选择要执行的操作-----------------
        1 - 查询所有
        2 - 根据账户查询 
    '''
    print(menu)

    oper = input("请选择要执行的操作:")
    if oper == '1':
        accts = am.query_all_acct()
        for acct in accts:
            print(acct) 
    elif oper == '2':
        acct_no = input("请输入要查询帐号")
        acct = am.query_by_id(acct_no)
        print(acct)
    else:
        print("暂不支持")

