# -*- coding: utf-8 -*-
# Time : 2022/12/7 11:26
# Author : daidai
# File : python_day8.py
# Desc :

#类
class parent:
    national='中国'       #类属性
    @classmethod
    def study(cls):    #类方法
        print('正在学习')

    def __init__(self,name,age):
        self.name=name   #实例属性
        self.age=age
        print('构造方法')

    def work(self):  #实例方法
        print(f'{self.name}都在工作')

    @staticmethod
    def run():
        print(f"静态方法可以使用类属性{parent.national},不可以使用实例属性！")


p1=parent('张三',30)
p2=parent('李四',40)
#属性
##类属性：在类中，为全局变量（类和实例都可以访问）
# print(parent.national)
# print(p1.national)
##实例属性:定义在实例方法里的，局部变量（只有实例可以访问，类不可以）
# print(p1.name)
# print(p2.name)
##添加属性（添加类的属性为私有属性）
##添加类属性
# parent.address='北京'
# print(parent.address)
#添加实例属性
# p1.addrs='上海'
# print(p1.addrs)
#修改类属性值（对类和实例都有影响）
# parent.national='USA'
# print(parent.national)
# print(p1.national)
# print(p1.national)
#修改实例属性值（只对被修改的实例有影响，对其他实例没有影响）
# p1.age=32
# print(p1.age)
# print(p2.age)
# #删除类属性（对类和所有实例都有影响）
# del parent.national
#print(parent.national)
#print(p1.national)
#print(p2.national)
#删除实例属性（只对被删除的实例有影响，对其他实例没有影响）
#del p1.name
#print(p1.name)
#print(p2.name)

#方法
##类方法：在方法的上面添加@classmethod装饰器，方法的参数(cls)，这里的cls就是代表类；类和实例都可以访问类方法
# print(parent.study())
# print(p1.study())
# print(p1.study())
#构造方法：初始化方法，__init__(),该方法是在实例化对象时调用，一般用来定义实例属性或者需要提前准备的操作
#实例方法：普通方法，必须有self参数（类不可以访问实例方法，所有的实例都可以访问实例方法
#parent.work()
p1.work()
p2.work()
#静态方法：在普通方法上面添加@staticmethod.没有参数
parent.run()
p1.run()
p2.run()















