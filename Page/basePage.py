# _*_ coding:utf-8 _*_
import time,os
from selenium.webdriver.support.ui import WebDriverWait             #导入显示等待等待
from selenium.webdriver.support import expected_conditions as EC    #导入判断方法
from Public import getPathInfo,log

log_info =log.logger                                                #log方法

class BasePage(object):
    """
    基本类，用于所有页面的继承
    """
    def __init__(self, driver):
        self.driver = driver

    def _open(self, url, pagetitle):
        """
        打开网页
        :param url: 网址
        :param pagetitle: 关键字
        """
        self.driver.maximize_window()               #浏览器最大化
        self.driver.implicitly_wait(30)             #显示等待
        self.driver.get(url)                        #打开指定网站
        assert pagetitle in self.driver.title, log_info.error("页面源码中不存在该关键字！")   #断言打开页面是否正确

    def find_element(self, *loc):
        """
        重写定位元素
        """
        try:
            #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))                   #判断元素是否存在
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())  #判断元素是否存在
            return self.driver.find_element(*loc)                   #返回定位元素
        except Exception as e:
            log_info.error('%s页面未找到%s元素' % (self, loc))
            self.get_windows_img()                                  #截图

    def switch_frame(self, loc):
        """
        切换frame
        """
        return self.driver.switch_to.frame(loc)

    def script(self, src):
        """
        定义script方法,用于执行js脚本
        """
        self.driver.execute_script(src)

    def get_windows_img(self):
        """
        截图
        """
        image_path=getPathInfo.join_cwd('Report\\Images\\')             #拼接截图存放目录
        if not os.path.exists(image_path):                              #判断目录是否存在
            os.mkdir(image_path)                                        #创建目录文件
        nowtime=time.strftime("%Y%m%d%H%M%S")                           #当前时间变量
        image_name=image_path +nowtime+ '.png'                          #截图路径
        try:
            self.driver.get_screenshot_as_file(image_name)              #截图
            log_info.info("截图保存地址:%s" % image_name)
            print('screenshot:', nowtime+'.png')                        #打印screenshot关键字，报告中显示截图
        except NameError as e:
            log_info.error("截图保存失败! %s" % e)
            #self.get_windows_img()

