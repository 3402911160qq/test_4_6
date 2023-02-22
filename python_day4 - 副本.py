# -*- coding: utf-8 -*-
# Time : 2022/11/18 17:09
# Author : daidai
# File : lianxi.py
# Desc :

# 1.在方框里打印字符串，屏幕长度为80，方框长度比字符串长6
# 左边距为（屏幕长度-方框长度）/2，字符串在方框的中央
# 显示结果如下：
# Sentence:this is a first sentence
# screen=80
# str=input('请输入字符串： ')
# str_a=len(str)
# box=str_a+6
# left=(screen-box)//2
# print(' '*left+'+'+'_'*(box-2)+'+')
# print(' '*left+'|'+' '*(box-2)+'|')
# print(' '*left+' '*2+str+' '*2+'|')
# print(' '*left+'|'+' '*(box-2)+'|')
# print(' '*left+'+'+'_'*(box-2)+'+')

#
# 1、以字典典型结构存储一下数据：
# Alice(phone:9432,Address:Foo drive 23),
# Beth(phone:9102,Adderess:Bar street 42),
# Cecil(phone:3158,Adderss:Baz avenue 90),
# 编写代码实现：输入用户名，将显示相应的用户详细信息
#
# user={'Alice':{'phone':'9432','Address':'Foo drive 23'},
#       'Beth':{'phone':'9102','Adderess':'Bar street 42'},
#       'Cecil':{'phone':'3158','Adderss':'Baz avenue 90'}
#
# }
# name=input('请输入用户名： ')
# user_info = user[name]
# user_phone= user_info['phone']
# user_Address= user_info['Address']
# print(name,user_phone,user_Address)


#2、存储班里同学名字为set类型，同学名有Alice,Bob,Candy,David,Elland,并且显示成一列。
set1={'Alice','Bob','Candy','David','Elland'}
print(set1.pop())
print(set1.pop())
print(set1.pop())
print(set1)
