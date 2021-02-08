# _*_ coding:utf-8 _*_
from selenium import webdriver                                  #导入浏览器模块
from Page.loginPage import Login_page                           #导入登录对象类
from Public import log,readConfig,readExcel                     #导入封装的Log方法、GetPath方法
import unittest,time,paramunittest

excel= readExcel.readExcel('UI_TestCase.xlsx')                  #获取excel文件
names=excel.get_sheetnames()                                    #获取sheel
testcase=excel.get_xlsx(names[0])                               #获取指定shell的case
baseurl = readConfig.Read_Config().get_info('HTTP','baseurl')   #获取配置文件的baseurl
log_info =log.logger                                            #log方法

@paramunittest.parametrized(*testcase)
class TestLogin(unittest.TestCase):
    """
    网易企业邮箱登录测试
    """
    def setParameters(self,NO,case_name,path,username,password,result):
        """
        从 excel 中获取用例
        :param NO: 用例编号
        :param case_name: 用例名称
        :param username: 账号
        :param password: 密码
        :param result: 预期结果
        """
        self.no =NO
        self.case_name = str(case_name)
        self.path = baseurl+str(path)
        self.username = username
        self.password = password
        self.result=result

    @classmethod
    def setUpClass(self):
        """执行类之前运行一次"""
        self.driver = webdriver.Chrome()              #启动浏览器
        self.login_page = Login_page(self.driver)     #初始化loginPage对象

    @classmethod
    def tearDownClass(self):
        """执行完类后执行一次"""
        time.sleep(3)                                 #等待时间
        self.driver.close()                           #关闭浏览器窗口

    def setUp(self):
        """执行每个测试用例前执行一次"""
        self.login_page.open(self.path, '网易企业邮箱 - 登录入口')            #打开首页，并断言title是否正确
        log_info.info('---%s %s测试用例 测试开始---' % (names[0], self.case_name))

    def tearDown(self):
        """执行完每个测试用例后执行一次"""
        log_info.info('---%s %s测试用例 测试结束---' % (names[0], self.case_name))

    #@unittest.skip("无条件跳过该测试")
    def test_login(self):
        """登录成功测试"""
        #self._testMethodName = self.case_name                   #当前函数方法+测试用例测试函数名称
        self._testMethodDoc = self.case_name                     # 测试函数文档
        self.login_page.click_loginway()
        self.login_page.input_username(self.username)             #输入用户名
        self.login_page.input_password(self.password)               #输入密码
        self.login_page.click_login()                               #点击登录按钮

        if self.case_name in ['登录成功']:
            try:
                self.assertEqual(self.result, self.login_page.show_userid(), msg='断言失败')  # 断言
                self.login_page.click_exit()                                # 点击退出按钮
                log_info.info('***断言成功***')
            except Exception as e:
                log_info.info('***断言失败***')
                self.login_page.get_windows_img()
                raise e

        elif self.case_name in ['登录失败-账号为空']:
            try:
                self.assertEqual(self.result, self.login_page.username_air(), msg='断言失败')  # 断言
                log_info.info('***断言成功***')
            except Exception as e:
                log_info.info('***断言失败***')
                self.login_page.get_windows_img()
                raise e

        elif self.case_name in ['登录失败-密码为空']:
            try:
                self.assertEqual(self.result, self.login_page.password_air(), msg='断言失败')  # 断言
                log_info.info('***断言成功***')
            except Exception as e:
                log_info.info('***断言失败***')
                self.login_page.get_windows_img()
                raise e
        else:
            try:
                self.assertEqual(self.result, self.login_page.Mismatch(), msg='断言失败')  # 断言
                log_info.info('***断言成功***')
            except Exception as e:
                log_info.info('***断言失败***')
                self.login_page.get_windows_img()
                raise e

if __name__ == '__main__':
    unittest.main()