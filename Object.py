from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time,unittest,re
class Object(unittest.TestCase):
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
	def test_object(self):
		u"""登录"""
		self.login()	
		browser = self.browser	
		u"""切换到资源控制页"""
		browser.find_element_by_link_text("资源控制").click()
		time.sleep(8)
		u"""切换到对象存储"""
		browser.find_element_by_link_text("对象存储").click()
		time.sleep(8)
		u"""添加用户"""
		browser.find_element_by_id("add").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='addid']").send_keys("3ads4324")
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='addname']").send_keys("asddasf")
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='addnew']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""修改用户"""
		browser.find_element_by_id("editlist").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='name']").send_keys("asddasf")
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='edit']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""添加权限"""
		browser.find_element_by_id("addauth").click()
		time.sleep(5)
		Select(browser.find_element_by_id("authtype")).select_by_index(1)
		time.sleep(5)
		Select(browser.find_element_by_id("whatauth")).select_by_index(1)
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='auth']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""删除权限"""
		browser.find_element_by_id("deleteauth").click()
		time.sleep(5)
		Select(browser.find_element_by_id("authtype")).select_by_index(1)
		time.sleep(5)
		Select(browser.find_element_by_id("whatauth")).select_by_index(1)
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='auth']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""配额设置"""
		browser.find_element_by_id("quota").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='max-object']").send_keys("213")
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='max-size']").send_keys("123")
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='quotaset']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""查看用户信息"""
		browser.find_element_by_id("view").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='all']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""删除用户"""
		browser.find_element_by_id("delete").click()
		time.sleep(5)
		browser.find_element_by_id("delete").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='deletesure']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""添加子用户"""
		browser.find_element_by_id("subadd").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='subname']").send_keys("asd")
		time.sleep(5)
		Select(browser.find_element_by_id("tank")).select_by_index(1)
		Select(browser.find_element_by_id("authtype")).select_by_index(1)
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='addsub']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""修改子用户"""
		browser.find_element_by_id("sedit").click()
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='subn']").send_keys("342423")
		time.sleep(5)
		Select(browser.find_element_by_id("modifyrank")).select_by_index(1)
		time.sleep(5)
		browser.find_element_by_xpath("//*[@id='subedit']/div/div/div[@class='modal-footer']/button[1]").click()
		time.sleep(5)
		u"""删除子用户"""
		browser.find_element_by_id("subdelete").click()
		time.sleep(5)
		browser.find_element_by_xpath("//div[@id='tips']/div[@id='deletesure']/div/div/div[@class='modal-footer']/button[1]").click()
		u"""关闭浏览器"""
		browser.close()
if __name__=='__main__':
	unittest.main()