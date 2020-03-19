import os, sys

import allure

sys.path.append(os.getcwd())
import pytest
from base.base_driver import base_driver
from page.search_page import SearchPage
from base.base_yml import yaml_to_list


# 将yaml里面的数据以列表形式返回
def param(test_name):
    """
    获得'login_data'这个文件中的key键对应的值
    :param key: yml文件中的一个键
    :return: 返回key键对应的值
    """ 
    return yaml_to_list("search_data", test_name)


class TestSearch:
    def setup(self):
        self.driver = base_driver()
        self.search_page = SearchPage(self.driver)

    @pytest.mark.parametrize("args", param("test_search"))
    def test_search(self, args):
        content = args["search_text"]
        screenshot_name = args["screenshot_name"]
        # 点击放大镜
        self.search_page.click_search()
        # 输入文字
        self.search_page.input_content(content)
        # 截图
        self.search_page.screenshot(screenshot_name)
        # 将截图上传到报告中
        allure.attach.file(r".\screen\%s.png"%screenshot_name, screenshot_name, attachment_type=allure.attachment_type.PNG)
        # 点击返回
        self.search_page.click_back()

    # @pytest.mark.parametrize("content", param("test_search1"))
    # def test_search1(self, content):
    #     # 点击放大镜
    #     self.search_page.click_search()
    #     # 输入文字
    #     self.search_page.input_content(content)
    #     # 点击返回
    #     self.search_page.click_back()



