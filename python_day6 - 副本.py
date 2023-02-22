# -*- coding: utf-8 -*-
# Time : 2022/11/24 20:45
# Author : daidai
# File : python_day6.py
# Desc :练习

'''
#题一：
设置程序实现用户登录（用for循环或while循环实现）
1）输入用户名和密码
2）判定是否正确（name="admin",password="root")
3)登录仅有三次机会，超过三次则提示“失败超过三次，请24小时候再登录！”
4）登录失败次数小于三次，给出提示信息“登录失败，还剩{次数}次几回！”
# '''
# for time in range(1,4):
#     name=input('请输入用户名： ')
#     password=input('请输入密码： ')
#     if name=='admin' and password=='root':
#         print('登录成功')
#         break
#     else:
#         if time==3:
#             print('失败超过三次，请24小时候再登录！')
#         else:
#             print(f'登录失败，还剩{3-time}次机会！')
#


#题三
#30个人在一条船上，超载，需要15人下船。于是人们排成一队，排队的位置即为他们的编号。
#报数，从1开始，数到9的人下船。如此循环，直到船上仅剩15人为之，问都有哪些编号的人下船了呢？
test1=[]
for i in range(1,31):
    test1.append(i)
print(test1)

drop_ship=0
while drop_ship<15:
    for i in range(9):
        if i==8:
            name=test1.pop(0)
            print(f'第{name}下船')
            drop_ship+=1
        else:
            test1.append(test1.pop(0))




