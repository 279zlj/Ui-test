from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time,unittest,re
class block(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
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
	def test_block(self):
		"""登录"""
		self.login()
		browser = self.browser	
		u"""切换到资源控制页"""
		browser.find_element_by_link_text("资源控制").click()
		time.sleep(8)
		u"""切换到块设备"""
		browser.find_element_by_link_text("块设备").click()
		time.sleep(8)
		u"""添加块设备"""
		browser.find_element_by_id("add").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='addname']").send_keys("asd")
		time.sleep(3)
		browser.find_element_by_xpath("//*[@id='addsize']").send_keys("123")
		time.sleep(3)
		Select(browser.find_element_by_id("sizeunit")).select_by_index(1)
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='selectpool']").click()
		time.sleep(5)
		Select(browser.find_element_by_id("selectpool")).select_by_index(1)
		time.sleep(2)
		Select(browser.find_element_by_id("selectpool")).select_by_index(1)
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='addnew']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='table_id']/tbody/tr[1]").click()
		time.sleep(5)
		u"""扩容"""
		browser.find_element_by_id("kr").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='poolsize']").send_keys("234")
		time.sleep(3)
		browser.find_element_by_xpath("//div[@id='dilatation']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""创建快照"""
		browser.find_element_by_id("snap").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='snapname']").send_keys("asd")
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='snapcontent']").send_keys("jkhfkudhsakfhds")
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='addsnap']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""快照独立"""
		browser.find_element_by_id("depend").click()
		time.sleep(5)
		u"""删除块设备"""
		browser.find_element_by_id("delete").click()
		time.sleep(5)
		browser.find_element_by_id("delete").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='deletesure']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='table']/tbody/tr[1]").click()
		time.sleep(5)
		u"""修改快照"""
		browser.find_element_by_id("edit").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='tipsmodel']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""快照回滚"""
		browser.find_element_by_id("black").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='tipsmodel']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""克隆"""
		browser.find_element_by_id("clone").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='tipsmodel']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""删除快照"""
		browser.find_element_by_id("deletel").click()
		time.sleep(5)
		u"""关闭浏览器"""
		browser.close()
if __name__=='__main__':
	unittest.main()