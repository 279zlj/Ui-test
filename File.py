from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time,unittest,re
class File(unittest.TestCase):
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
	def test_file(self):
		u"""登录"""
		browser = self.browser
		self.login()
		u"""切换到资源控制页"""
		browser.find_element_by_link_text("资源控制").click()
		time.sleep(8)
		u"""切换到文件存储"""
		browser.find_element_by_link_text("文件存储").click()
		time.sleep(8)
		u"""点击mds设置"""
		browser.find_element_by_id("mds").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='active']").send_keys("213")
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='spare']").send_keys("23")
		time.sleep(5)
		browser.find_element_by_xpath("//input[@value='yes']").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='mdsset']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='fstable']/tbody/tr[1]").click()
		time.sleep(5)
		u"""点击文件系统设置"""
		browser.find_element_by_id("set").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='size']").send_keys("123")
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='number']").send_keys("234")
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='quotasetting']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""点击新建文件系统"""
		browser.find_element_by_id("add").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='name']").send_keys("asdasd")
		time.sleep(5)
		browser.find_element_by_id("metapool").click()
		time.sleep(5)
		# Select(browser.find_element_by_id("metapool")).select_by_index(1)
		# time.sleep(5)
		browser.find_element_by_id("datapool").click()
		time.sleep(5)
		# Select(browser.find_element_by_id("datapool")).select_by_index(1)
		# time.sleep(5)
		browser.find_element_by_xpath("//div[@id='newfile']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""点击删除文件系统"""
		
		browser.find_element_by_id("delete").click()
		time.sleep(3)
		browser.find_element_by_id("delete").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='deletesure']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""关闭浏览器"""
		browser.close()
if __name__=='__main__':
	unittest.main()