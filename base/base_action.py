from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        """
        功能：找到loc对应的元素，点击它
        :param loc: 类型为元组，包含两个元素，第一个元素是查找的方式比如By.XPATH，第二个元素是XPATH对应的值
        :return: 点击找到的元素
        """
        self.find_element(loc).click()

    def input_text(self, loc, text):
        """
         功能：找到loc对应的元素，输入text文字
        :param loc: 类型为元组，包含两个元素，第一个元素是查找的方式比如By.XPATH，第二个元素是XPATH对应的值
        :param text: 要输入的字符串
        :return: 给找到的元素输入text值
        """
        self.find_element(loc).send_keys(text)

    def find_element(self, loc):
        """
        查找元素
        :param loc: 类型为元组，包含两个元素，第一个元素是查找的方式比如By.XPATH，第二个元素是XPATH对应的值
        :return: 返回一个元素
        """
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_feature(value)
        print(by, value)
        return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(by, value))

    def find_elements(self, loc):
        """
        查找元素
        :param loc: 类型为元组，包含两个元素，第一个元素是查找的方式比如By.XPATH，第二个元素是XPATH对应的值
        :return: 返回元素列表
        """
        by = loc[0]
        value = loc[1]
        if by == "By.XPATH":
            value = self.make_xpath_feature(value)
        return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_elements(by, value))

    def make_xpath_unit_feature(self, loc):
        """
        拼接xpath中间的部分
        """
        args = loc.split(", ")
        # xpath查找的属性名
        key_index = 0
        # 属性值
        value_index = 1
        # 是按照什么方式查找，0表示使用contains方法，1表示使用精确查找
        option_index = 2

        if len(args) == 2:
            feature_middle = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + " and "
        elif len(args) == 3:
            if args[option_index] == "1":
                feature_middle = "@" + args[key_index] + "='" + args[value_index] + "'" + " and "
            elif args[option_index] == "0":
                feature_middle = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + " and "

        return feature_middle

    def make_xpath_feature(self, loc):
        """
        参数loc的值为'@xxx,xxx'，表示要使用contains方法的xpath，
        '@xxx,xxx,1'：表示使用精确查找
        '@xxx,xxx,0'，表示要使用contains方法的xpath，
        """
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            feature = self.make_xpath_unit_feature(loc)
        else:
            for i in loc:
                feature += self.make_xpath_unit_feature(i)

        feature = feature.rstrip(" and ")
        result = feature_start + feature + feature_end

        return result

    def screenshot(self, file_name):
        self.driver.get_screenshot_as_file("./screen/" + file_name + ".png")
        
    def find_toast(self, message, screen_name, is_screenshot=False, timeout=10.0, time=0.1):
        """
        获取toast全部内容
        :param message: 预期要获取到的toast部分提示信息
        :param tiemout:WebDriverWait寻找toast的总共时间
        :param tiem:每隔多长时间寻找toast一次
        :return: 返回找到的toast提示信息
        """
        message = "text, " + message
        element = self.find_element((By.XPATH, message), 20, 0.1)
        if is_screenshot:
            self.screenshot(screen_name)
        # print(element.text)
        return element.text

    def is_toast_exist(self, message, screen_name, is_screenshot=False, timeout=10.0, time=0.1):
        """
        根据message查找toast是否存在
        :param message: toast的部分或者全部提示内容
        :return: 如果message存在，返回True，否则返回False
        """
        try:
            self.find_toast(message, screen_name, is_screenshot, timeout, time)
            return True
        except Exception:
            return False
            
    def press_keycode(self, keycode):
        """
        重写press_keycode，整合keyevent(keycode)
        :param message: 需要按的键，对应的keycode
        :return: 无
        """
        if "automationName" not in self.driver.desired_capabilities.keys():
            self.driver.keyevent(keycode)
        elif desired_capabilities["automationName"] == "Uiautomator2":
            self.driver.press_keycode(keycode)
        