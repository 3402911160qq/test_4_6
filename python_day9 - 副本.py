# -*- coding: utf-8 -*-
# Time : 2022/12/9 11:22
# Author : daidai
# File : python_day9.py
# Desc :继承、封装、多态
##继承：
#1·
# class Goat:
#     def __init__(self):
#         self.name='乔丹'
#         print(f"{self.name}将篮球推向了全世界")
#
#     def play(self):
#         print(f"{self.name}是历史上最伟大的篮球运动员，篮球之神")
#
# #2·
# class Mamba:
#     def __init__(self):
#         self.name='科比'
#         print(f"{self.name}最具职业精神的伟大篮球运动员")
#
#     def god_mamber(self):
#         print(f"{self.name}是我最喜欢的篮球运动员")
#
# #3·
# class KingJames(Mamba,Goat):
#     def __init__(self):
#         super().__init__()    #超级父类
#         #self.name = '詹姆斯'
#         print(f"{self.name}最全能的篮球运动员")
#
#     def god(self):
#         print(f"{self.name}是历史上唯一给三个城市带来总冠军的篮球远动员")
#
# K1=KingJames()
# #K1.god_mamber()
# #K1.play()
# super(KingJames,K1).god_mamber()
#

##封装：
# class student:
#     def __init__(self,sno,sname):
#         self.sno = sno
#         self.sname = sname
#
#     @property
#     def name(self):     #可读
#         return self.__sname
#
#     @name.setter       #可写
#     def name(self,newvalue):
#         self.__sname=newvalue
#
#     def study(self):
#         print(f"{self.__sname}正在学习.....")
#
# s1=student(1,'tester01')
# s1.name='tester02'
# print(s1.name)


##多态：
# class Duck:
#     def fly(self):
#         print('鸭子沿着地面起飞')
#
# class Swan:
#     def fly(self):
#         print('天鹅在空中飞翔')
#
# class Plane:
#     def fly(self):
#         print('飞机起飞了')
#
# def fly(obj):
#     obj.fly()
#
# duck=Duck()
# swan=Swan()
# plane=Plane()
#
# fly(duck)
# fly(swan)
# fly(plane)




















