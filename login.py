#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import unittest,time,re

class Login(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
		# browser.time.sleep(2)     强制性等待
		self.browser.implicitly_wait(30)
		self.base_url = "http://192.168.2.67:8088"
		self.verificationErrors = []
		self.accept_next_alert = True
	def login(self):
		browser = self.browser
		browser.get(self.base_url)
		browser.find_element_by_id("user").send_keys("admin")
		browser.find_element_by_id("pwd").send_keys("admin00")
		browser.find_element_by_id("loginbtn").click()
		time.sleep(5)
	def test_login(self):
		u"""登录"""
		browser = self.browser
		self.login()
		# print("关闭浏览器")
		browser.close()
	def test_bar(self):
		u"""测试导航栏"""
		browser = self.browser
		self.login()
		browser.find_element_by_id("useropt").click()
		time.sleep(3)
		browser.find_element_by_id("usermanager").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='usert']/tbody/tr[1]").click()
		time.sleep(5)
		# print("点击修改")
		u"""点击修改"""
		browser.find_element_by_id("edit").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='name']").send_keys('123456')
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='content']").send_keys('0')
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='editm']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		# print("点击删除")
		u"""点击删除"""
		browser.find_element_by_id("delete").click()
		time.sleep(5)
		browser.find_element_by_id("delete").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='deletesure']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		# print("点击管理")
		u"""点击管理"""
		browser.find_element_by_id("manager").click()
		time.sleep(3)
		# print("点击版本")
		u"""点击版本"""
		browser.find_element_by_id("version").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='bb']/div/div/div[@class='modal-footer']/button[2]").click()
		time.sleep(5)
		browser.find_element_by_id("manager").click()
		time.sleep(3)
		# print("点击lisense")
		u"""点击lisense"""
		browser.find_element_by_id("lisenseopt").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='lisense']/div/div/div[@class='modal-footer']/button[2]").click()
		time.sleep(5)
		browser.find_element_by_id("manager").click()
		time.sleep(3)
		# print("点击日志管理")
		u"""点击日志管理"""
		browser.find_element_by_id("logmanager").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='logt']/tbody/tr[1]").click()
		time.sleep(5)
		browser.find_element_by_id("collect").click()
		time.sleep(5)
		Select(browser.find_element_by_id("type")).select_by_index(1)
		time.sleep(5)
		Select(browser.find_element_by_id("time")).select_by_index(1)
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='addnew']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		browser.find_element_by_id("deletelist").click()
		time.sleep(5)
		browser.find_element_by_id("manager").click()
		time.sleep(3)
		# print("点击添加警告")
		u"""点击添加警告"""
		browser.find_element_by_id("addwarn").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='notice']/div/div/div[@class='modal-footer']/button[2]").click()
		time.sleep(5)
		# print("点击语言")
		u"""点击语言"""
		browser.find_element_by_id("langue").click()
		time.sleep(5)
		browser.find_element_by_id("english").click()
		time.sleep(5)
		# print("点击语言")
		u"""点击语言"""
		browser.find_element_by_id("langue").click()
		time.sleep(5)
		browser.find_element_by_id("chinese").click()
		time.sleep(5)
		browser.find_element_by_id("useropt").click()
		time.sleep(3)
		# print("点击退出登录")
		u"""点击退出登录"""
		browser.find_element_by_id("outlogin").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='logout']/div/div/div[@class='modal-footer']/button").click()
		time.sleep(5)
		# print("关闭浏览器")
		browser.close()
	def tearDown(self):
		self.browser.quit()
		self.assertEqual([],self.verificationErrors)
if __name__=='__main__':
	unittest.main()