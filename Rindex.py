from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import unittest,time,re
class Rindex(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(30)
		self.base_url = "http://192.168.2.67:8088"
		self.verificationErrors = []
		self.accept_next_alert = True
	def test_resourse(self):
		u"""切换到资源控制页"""
		browser = self.browser
		browser.get(self.base_url)
		browser.find_element_by_id("user").send_keys("admin")
		browser.find_element_by_id("pwd").send_keys("admin00")
		browser.find_element_by_id("loginbtn").click()
		browser.find_element_by_link_text("资源控制").click()
		time.sleep(8)
		u"""测试查看按钮"""
		self.allview()
		u"""测试节点界面"""
		self.osdview()
	def allview(self):
		# self.resourse()
		browser = self.browser
		u"""查看cpu使用率"""
		browser.find_element_by_id("cpuview").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='cput']/div/div/div[@class='modal-footer']/button[2]").click()
		time.sleep(5)
		u"""查看iops使用率"""
		browser.find_element_by_id("iopsview").click()
		time.sleep(5)
		browser.find_element_by_id("iopsview").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='iopsmbps']/div/div/div[@class='modal-footer']/button[2]").click()
		time.sleep(5)
		u"""查看mbps使用率"""
		browser.find_element_by_id("mbpsview").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='iopsmbps']/div/div/div[@class='modal-footer']/button[2]").click()
		time.sleep(5)
	def osdview(self):
		u"""切换到节点"""
		# self.resourse()
		browser = self.browser
		browser.find_element_by_link_text("节点").click()
		time.sleep(8)
		# much = 1
		# while (much < 4):
		# 	browser.find_element_by_xpath("div[@class='content']/div[@id='sample']/div["+str(much)+"]").click()
		# 	time.sleep(3)
		# 	much=much+1
		u"""点击修改iSCSI"""
		browser.find_element_by_id("edit").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='editm']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		# print("关闭浏览器")
		browser.close()
if __name__=='__main__':
	unittest.main()