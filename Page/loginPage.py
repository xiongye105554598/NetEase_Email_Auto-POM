# _*_ coding:utf-8 _*_
from selenium.webdriver.common.by import By
from Page.basePage import BasePage                          #导入基本类
from Public import log

log_info =log.logger                                        #log方法

class Login_page(BasePage):
    """
    登录页面操作步骤
    """
    #元素定位器
    login_way =(By.ID,"switchNormalCtrl")
    username = (By.ID, "accname")
    password = (By.ID, "accpwd")
    login_btn = (By.XPATH, "//*[@id='loginBlock']/div[2]/form[1]/div[5]/button")
    logout = (By.XPATH, "//*[@id='top']/div/div[2]/div[3]/div/a[5]")
    login_msg = (By.ID, 'msgpid')
    user_air=(By.XPATH,"//*[@id='loginBlock']/div[2]/form[1]/div[1]/div")
    pw_air=(By.XPATH,"//*[@id='loginBlock']/div[2]/form[1]/div[2]/div")

    #打开页面
    def open(self, url, pagetitle):
        self._open(url, pagetitle)

    #登录方式选择
    def click_loginway(self):
        log_info.info("点击密码登录")
        self.find_element(*self.login_way).click()

    #输入账号
    def input_username(self, username):
        log_info.info("输入账号")
        self.find_element(*self.username).clear()
        self.find_element(*self.username).send_keys(username)

    #输入密码
    def input_password(self, password):
        log_info.info("输入密码")
        self.find_element(*self.password).clear()
        self.find_element(*self.password).send_keys(password)

    #点击登录
    def click_login(self):
        log_info.info("点击登录")
        self.find_element(*self.login_btn).click()

    #登录成功文本
    def show_userid(self):
        exit_text=self.find_element(*self.logout).text
        log_info.info("登录成功")
        return exit_text

    #账号注销
    def click_exit(self):
        self.find_element(*self.logout).click()
        log_info.info("账号注销")

    #登录失败提示
    def Mismatch(self):
        msg_text=self.find_element(*self.login_msg).text
        #log_info.info(msg_text)
        return msg_text

    #帐号为空
    def username_air(self):
        user_air=self.find_element(*self.user_air).text
        #log_info.info(user_air)
        return user_air

    #密码为空
    def password_air(self):
        password_text=self.find_element(*self.pw_air).text
        #log_info.info(password_text)
        return password_text




