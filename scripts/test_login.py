import os, sys
import time
sys.path.append(os.getcwd())

import pytest
import allure
from base.base_driver import base_driver
#from page.login_page import LoginPage
from base.base_yml import yaml_to_list


def login_with_key(key):
    """
    获得'login_data'这个文件中的key键对应的值
    :param key: yml文件中的一个键
    :return: 返回key键对应的值
    """ 
    return yaml_to_list("login_data", key)
    

class TestLogin:


    @pytest.mark.parametrize("args", login_with_key('test_login_error'))
    def test_login_error(self, args):
        username = args['username']
        pwd = args['pwd']
        message = args['message']
        # 输入手机号
        print(username)
        # 输入密码
        print(pwd)
        # 点击登录
        print("点击登录")
        # 判断是否登录成功
        assert 1
    
    # @pytest.mark.parametrize("args", login_with_key('test_login_error1'))
    # def test_login_error1(self, args):
        # username = args['username']
        # pwd = args['pwd']
        # print(username, pwd)

