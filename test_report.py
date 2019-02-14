#coding=utf-8
import unittest
import login
import Rindex
import Aindex
import Object
import block
import File
import pool
import Mindex
import HTMLTestRunner

testunit=unittest.TestSuite()
testunit.addTest(unittest.makeSuite(login.Login))
testunit.addTest(unittest.makeSuite(Rindex.Rindex))
testunit.addTest(unittest.makeSuite(Aindex.Aindex))
testunit.addTest(unittest.makeSuite(Object.Object))
testunit.addTest(unittest.makeSuite(block.block))
testunit.addTest(unittest.makeSuite(pool.pool))
testunit.addTest(unittest.makeSuite(File.File))
testunit.addTest(unittest.makeSuite(Mindex.mindex))

filename='C:\\Users\\zlj\\Desktop\\UI-test\\'+u"测试报告"+"report.html"
fp=open(filename,"wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况')
runner.run(testunit)