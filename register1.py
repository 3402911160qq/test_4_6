# -*- coding: utf-8 -*-
# Time : 2022/12/9 17:47
# Author : daidai
# File : register.py
# Desc :

from encapsulation1 import ReadWrite

class Reg:
    # def __init__(self):
    #     self.file=r'C:\Users\Administrator.DESKTOP-GQ1FJUK\Desktop\data.txt'

    def Reg_v(self):
        username=input('请输入用户名： ')
        password=input('请输入密码： ')
        ReadWrite().txtWrite(username,password)
        # f=open(self.file,'a',encoding='utf-8')
        # value=f"{username},{password}\n"
        # f.writelines(value)
        # f.close()
        return True

if __name__=='__main__':
    user1=Reg()
    user1.Reg_v()
