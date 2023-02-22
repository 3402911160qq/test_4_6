# -*- coding: utf-8 -*-
# Time : 2022/12/23 14:41
# Author : daidai
# File : 自动化.py
# Desc :
#
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

e=Service(executable_path=r'C:\Users\Administrator.DESKTOP-GQ1FJUK\Downloads\edgedriver_win64\msedgedriver.exe')
driver=webdriver.Edge(service=e)
sleep(1)
driver.maximize_window()
sleep(1)
#登录禅道
driver.get('http://127.0.0.1/zentao/user-login.html')
sleep(2)
driver.find_element(By.ID,'account').send_keys('admin')
driver.find_element(By.NAME,'password').send_keys('123456qQ')
driver.find_element(By.ID,'submit').click()
sleep(3)

#添加用户
# driver.find_element(By.LINK_TEXT,'后台').click()
# driver.switch_to.frame('appIframe-admin')
# time.sleep(1)
# driver.find_element(By.LINK_TEXT,'人员').click()
# driver.find_element(By.LINK_TEXT,'添加用户').click()
# time.sleep(1)
# driver.find_element(By.ID,'account').send_keys('dai')
# driver.find_element(By.ID,'password1').send_keys('yu4824600thv')
# driver.find_element(By.ID,'password2').send_keys('yu4824600thv')
# driver.find_element(By.ID,'realname').send_keys('d')
# time.sleep(1)
# select_element=driver.find_element(By.ID,'role')
# time.sleep(1)
# Select(select_element).select_by_index(4)
# time.sleep(1)
# driver.find_element(By.ID,'verifyPassword').send_keys('123456qQ')
# driver.find_element(By.ID,'submit').click()
# time.sleep(1)

#删除用户
# driver.find_element(By.LINK_TEXT,'后台').click()
# driver.switch_to.frame('appIframe-admin')
# time.sleep(1)
# driver.find_element(By.LINK_TEXT,'人员').click()
# driver.find_element(By.LINK_TEXT,'用户').click()
# time.sleep(1)
# driver.find_element(By.LINK_TEXT,'搜索').click()
# time.sleep(1)
# driver.find_element(By.ID,'value1').send_keys('dd')
# driver.find_element(By.ID,'submit').click()
# time.sleep(1)
# driver.find_element(By.CLASS_NAME,'icon-trash').click()
# time.sleep(1)
# driver.switch_to.frame('iframe-triggerModal')
# driver.find_element(By.ID,'verifyPassword').send_keys('123456qQ')
# driver.find_element(By.ID,'submit').click()
# time.sleep(1)

#登出禅道
driver.switch_to.frame('appIframe-my')
from selenium.webdriver.common.action_chains import ActionChains  #导入鼠标移动的类方法
element1 = driver.find_element(By.ID,'main-avatar')
sleep(2)
ActionChains(driver).move_to_element(element1).perform()   #鼠标移动到指定元素位置
sleep(1)
driver.find_element(By.LINK_TEXT,'退出').click()

















#登出禅道
# driver.switch_to.frame('appIframe-my')
# element1=driver.find_element(By.ID,'main-avatar')
# time.sleep(1)
# ActionChains(driver).move_to_element(element1).perform()
# time.sleep(1)
# driver.find_element(By.LINK_TEXT,'退出').click()































