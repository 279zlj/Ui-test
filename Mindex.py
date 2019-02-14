from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time,unittest,time,re
class mindex(unittest.TestCase):
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
	def test_risk(self):
		u"""登录"""
		browser = self.browser
		self.login()
		u"""切换到风险控制页"""
		# browser.find_element_by_link_text("风险控制").click()
		browser.find_element_by_id("management").click()
		time.sleep(5)
		browser.find_element_by_link_text("解决方案").click()
		time.sleep(5)
		browser.find_element_by_link_text("导入解决包").click()
		time.sleep(5)
		u"""关闭浏览器"""
		browser.close()
if __name__=='__main__':
	unittest.main()