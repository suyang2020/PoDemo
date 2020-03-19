from appium import webdriver


def base_driver():
    """连接手机，获取driver"""
    server = r'http://localhost:4723/wd/hub'  # Appium Server, 端口默认为4723
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        'platformVersion': '5.1.1',
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
        'unicodeKeyboard': True,
        'reserKeyBoard': True,
        'noReset': True,
        'fullReset': False
    }
    driver = webdriver.Remote(server, desired_capabilities)  # 连接手机和APP
    return driver

