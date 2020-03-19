from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SearchPage(BaseAction):
    # 搜索按钮
    search_button = By.ID, r"com.android.settings:id/search"
    # 搜索内容
    search_text = By.XPATH, ["text, 搜索", "text, 搜索…, 1"]

    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def click_search(self):
        self.click(self.search_button)

    def input_content(self, text):
        self.input_text(self.search_text, text)

    def click_back(self):
        self.click(self.back_button)


