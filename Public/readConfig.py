# _*_ coding:utf-8 _*_
import configparser
from Public import getPathInfo

class Read_Config(object):
    """
    读取配置文件信息
    """
    def __init__(self):
        config_path=getPathInfo.join_cwd('config.ini')      #拼接路径
        self.config = configparser.ConfigParser()           #调用配置文件方法
        self.config.read(config_path)                       #读取配置文件

    def get_info(self, group_name, key):
        """
        读取配置文件config中指定组的键值
        :param group_name:组名
        :param key: key值
        """
        return self.config.get(group_name, key)

if __name__ == '__main__':
    print(Read_Config().get_info('HTTP','baseurl'))         #测试一下，读取配置文件的方法是否可用
