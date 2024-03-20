'''
    options类或者是函数的形态，专门用于管理options相关设置。一定记得在末尾要使用return来返回。
'''
from selenium import webdriver

def options():
    # 创建一个options对象，进行浏览器的设置项定义。什么浏览器就创建对应的options对象即可
    options = webdriver.ChromeOptions()
    # 页面加载策略
    # options.page_load_strategy = 'normal'

    # 想要添加设置项的时候，常用的两个添加设置方法
    # options.add_experimental_option()  # 添加试验性质的参数，意味着可能存在不稳定的情况，但是实际上没有发现有什么不稳定。
    # options.add_argument()  # 添加常规参数

    # 窗体最大化
    # options.add_argument('start-maximized')
    # 窗体的指定坐标启动：该方法只能针对未最大化窗体的浏览器进行设置。
    # options.add_argument('window-position=300,600')
    # 窗体的初始化尺寸定义
    # options.add_argument('window-size=1000,1200')

    # 自动化测试黄条警告去除
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    # options.add_experimental_option('disable-infobars') # 只有python27的版本才有效，现在看到可以直接忽略。

    # 无头模式：浏览器不以界面形态来运行。但是实际上，该执行的相关操作依旧还是会正常执行。这种模式可以降低GPU和CPU资源的耗费。无头模式在特定的场景下可能会出现BUG
    # options.add_argument('--headless')

    # 账号密码保存弹窗的去除
    prefs = {
        'credentials_enable_service': False,
        'profile.password_manager_enable': False
    }
    options.add_experimental_option('prefs', prefs)

    # 加载用户本地缓存信息
    '''
        selenium默认启动的浏览器，是不会加载本地缓存信息的。也就意味着Selenium启动的浏览器是完全全新且独立的浏览器，不会与本地的数据进行任何的交互
            1. 全新浏览器访问系统时会有验证码的风险。
            2. 验证码本身是用于防止自动化脚本恶意访问的，所以Selenium不处理验证码
        如果想要避免验证码的风险，其中一种手段就是加载本地缓存信息。
        想要绕过登录，加载本地缓存是一个最直接的方法，但是前提是网站本身具备有保存登录状态的功能。
        要通过Selenium调用本地缓存，一定要提前将浏览器全部关闭，再启动自动化脚本，否则会报错。
    '''
    # options.add_argument(r'--user-data-dir=C:\Users\15414\AppData\Local\Google\Chrome\User Data')

    # 启动隐身模式
    # options.add_argument('incognito')

    # 去除控制台的多余信息：首选此方法
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # 进一步去除系统多余信息，去除多余日志的第二道保险
    options.add_argument('--log_level=3')
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')

    # 对options设置好以后一定要记得用return返回。
    return options