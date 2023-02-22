# -*- coding: utf-8 -*-
# Time : 2022/11/30 9:47
# Author : daidai
# File : python_day7.py
# Desc :

# # 1.定义两数之和的函数（位置参数传值）-sum()
def sun(num1,num2):
    nums=num1+num2
    return nums
print('第一题:',sun(2,5))


# # 2.定义两数之差的函数（关键字参数传值）-sub()
def sub(num1,num2):
    nums=num2-num1
    return nums
print('第二题：',sub(3,5))

# # 3.定义多个数之积的函数（可变位置参数值）-multiply()
def multiply(*num):
    nums=1
    for i in range(len(num)):
        nums*=num[i]
    return nums
print('第三题：',multiply(1,4,6))

# #4.定义多个数之和函数（可变关键字传值）-m_sum()
def m_sum(**num):
    value_list=list(num.values())
    nums=0
    for i in range(len(value_list)):
        nums+=value_list[i]
    return nums
print('第四题：',m_sum(a=2,b=4,c=5))

# 5.定义两数取余的函数（默认值函数）-left_num()
def left_num(num1,num2=5):
    value_num=num1%num2
    return value_num
print('第五题：',left_num(7))

# 6.编写一个名为odd_even()的函数，它有一个名为number的参数，判断一个数字是否为奇数或偶数
def odd_even(number):
    if number%2==0:
        return('偶数')
    else:
        return('奇数')
print('第六题',odd_even(10))

# 7.编写出绝对值函数ads1()
def ads1(num):
    if num>0:
        return num
    else:
        return -num
print('第七题：',ads1(-6))

# 8.请定义一个 square_of_sum 函数，它接受一个list,返回list中每个元素平方的和
def square_of_sum(list):
    sum=1
    for i in range(len(list)):
        sum+=list[i]**2
    return sum
print('第八题：',square_of_sum([1,4,6,8]))


# 9.用二分法搜索一组数据中某一特定元素的位置










