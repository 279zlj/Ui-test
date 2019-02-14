from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest,time,re
class Aindex(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(30)
		self.base_url = "http://192.168.2.67:8088"
		self.verificationError = []
		self.accept_next_alert = True
	def test_control(self):
		u"""切换到资源调配页"""
		browser = self.browser
		browser.get(self.base_url)
		browser.find_element_by_id("user").send_keys("admin")
		browser.find_element_by_id("pwd").send_keys("admin00")
		browser.find_element_by_id("loginbtn").click()
		time.sleep(5)
		u"""资源调配页导航栏测试"""
		self.control_left()
		u"""点击新建规则"""
		self.control_rule()
	def control_left(self):
		browser = self.browser
		u"""资源调配页导航栏测试"""
		browser.find_element_by_link_text("资源调配").click()
		time.sleep(5)
		browser.find_element_by_link_text("对象参数设置").click()
		time.sleep(5)
		browser.find_element_by_link_text("FS客户端").click()
		time.sleep(5)
		browser.find_element_by_link_text("参数修改").click()
		time.sleep(5)
		browser.find_element_by_link_text("运维设置").click()
		time.sleep(5)
	def control_rule(self):
		browser = self.browser
		u"""点击新建规则"""
		browser.find_element_by_id("addrule").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='rulename']").send_keys("qwe")
		time.sleep(3)
		browser.find_element_by_xpath("//div[@id='newrule']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='table_id']/tbody/tr[1]").click()
		time.sleep(5)
		# u"""点击编辑"""
		# browser.find_element_by_id("editlist").click()
		# time.sleep(5)
		# browser.find_element_by_xpath("//div[@id='editem']/div/div/div[@class='modal-footer']/button[1]").click()
		# time.sleep(5)
		# u"""点击删除"""
		# browser.find_element_by_id("deletelist").click()
		# time.sleep(5)
		# browser.find_element_by_xpath("//div[@id='tips']/div[@id='deletesure']/div/div/div[@class='modal-footer']/button[1]").click()
		# time.sleep(5)
		# print("关闭浏览器")
		u"""关闭浏览器"""
		browser.close()
if __name__=='__main__':
	unittest.main()