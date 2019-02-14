from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time,unittest,re
class pool(unittest.TestCase):
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
	def test_pool(self):
		browser = self.browser
		self.login()
		u"""切换到资源控制页"""
		browser.find_element_by_link_text("资源控制").click()
		time.sleep(8)
		u"""切换到存储池"""
		browser.find_element_by_link_text("存储池").click()
		time.sleep(10)
		u"""添加存储池"""
		browser.find_element_by_id("add").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='addname']").send_keys("abc")
		time.sleep(5)
		Select(browser.find_element_by_id("pooltype")).select_by_index(1)
		time.sleep(5)
		browser.find_element_by_id("poolrule").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='addnew']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='table_id']/tbody/tr[1]").click()
		time.sleep(5)
		u"""点击扩容"""
		browser.find_element_by_id("kr").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='poolsize']").send_keys("123")
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='dilatation']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""修改存储池名称"""
		browser.find_element_by_id("edit").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='name']").send_keys("asd")
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='editm']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""删除存储池"""
		browser.find_element_by_id("delete").click()
		time.sleep(5)
		browser.find_element_by_id("delete").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='deletesure']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""添加新客户端"""
		browser.find_element_by_id("addclient").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='clientname']").send_keys("dfshjhfdkjshfkjsdhfdkjs")
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='clientmodal']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='table']/tbody/tr[1]").click()
		time.sleep(5)
		u"""分配lun"""
		browser.find_element_by_id("addlun").click()
		time.sleep(5)
		Select(browser.find_element_by_id("lunselect")).select_by_index(1)
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='getlun']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""删除lun"""
		browser.find_element_by_id("deletelun").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='nolun']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""删除客户端"""
		browser.find_element_by_id("deletel").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='deletesure']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)

		u"""关闭浏览器"""
		browser.close()
if __name__=='__main__':
	unittest.main()