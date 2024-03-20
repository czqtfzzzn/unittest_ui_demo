import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from conf.chrome_options import options
from conf.logging_config import getLogger


# driver 浏览器对象生成
def open_browser(type_):
    driver_dict = {
        'Chrome': ['Chrome', 'chrome', '谷歌'],
        'Firefox': ['Firefox', 'fox', '火狐']
    }
    driver = None
    for driver_type, name_list in driver_dict.items():
        if type_ in name_list:
            if driver_type == "Chrome":
                driver = getattr(webdriver, driver_type)()
            else:
                # print(driver_type)
                driver = getattr(webdriver, driver_type)()
    if driver is None:
        driver = getattr(webdriver, "Chrome")(options=options())
    return driver


class WebKeys:
    def __init__(self):
        self.driver = None
        self.log = getLogger()

    # 打开浏览器
    def open_browser(self, type_):
        self.driver = open_browser(type_)
        # 设置隐式等待 5 s
        self.driver.implicitly_wait(5)

    # 访问 url
    def open(self, url):
        self.driver.get(url)

    # 定位元素
    def location(self, by, value):
        return self.driver.find_element(by, value)

    # input 输入
    def input(self, by, value, txt):
        el = self.location(by, value)
        el.clear()
        el.send_keys(txt)

    # 点击
    def click(self, by, value):
        self.location(by, value).click()

    # 鼠标悬停
    def move_to(self, by, value):
        ActionChains(self.driver).move_to_element(self.location(by, value)).perform()

    # 强制等待
    def wait(self, time_):
        try:
            time.sleep(int(time_))
        except:
            time.sleep(2)

    # 显示等待
    def e_wait(self, by, value):
        return WebDriverWait(self.driver, 5, 0.5).until(
            lambda element: self.driver.find_element(by, value), message='元素查找失败'
        )

    # 关闭浏览器
    def quit(self):
        self.driver.quit()

    # 进入 frame 内嵌窗体
    def to_frame(self, by, value):
        self.driver.switch_to.frame(self.location(by, value))

    # 回到默认窗体
    def to_default(self):
        self.driver.switch_to.default_content()

    # 生成新的浏览器
    def new_window(self):
        self.driver.switch_to.new_window('window')

    # 生成新的标签页
    def new_tab(self):
        self.driver.switch_to.new_window('tab')

    # 页面句柄切换
    def switch_handle(self, num):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[int(num)])

    # 获取当前URL
    def get_url(self):
        return self.driver.current_url

    # 通过ActionChains类实现移动到指定的元素的操作。
    def demo(self, by, value):
        ActionChains(self.driver).scroll_to_element(self.location(by, value)).perform()

    def assert_info(self, ass_dict):
        if ass_dict['value'] in getattr(self, ass_dict['fun'])():
            self.log.info('断言：流程成功')
            return True
        else:
            self.log.info('断言：流程失败')
            return False
