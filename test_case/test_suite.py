import os
import unittest
from HTMLTestReportCN import HTMLTestRunner
import time


# type_: 生成套件的方法 -- suite、discover
def c_cases(type_, pattern):
    print("生成套件")
    if type_ == "suite":
        suite = unittest.TestSuite()

    elif type_ == "discover":
        path = './'
        # 用例的获取方式：通过来discover方法获取测试用例集，并返回结果为测试套件。
        discover = unittest.defaultTestLoader.discover(start_dir=path,  # 用例获取的路径指定
                                                       pattern=pattern)  # 用例文件的命名规则
        return discover


# 执行测试套件，生成测试报告
def c_html(type_, pattern, tester):
    print("执行开始")
    # 配置测试报告的相关信息
    report_dir = './report/'  # 测试报告的保存路径
    report_title = '成紫乾的测试报告'  # 测试报告的名称
    report_description = '测试报告的描述信息，请查阅'  # 测试报告的描述信息
    '''
        测试报告的名称设置，如果是固定名称，则每次生成报告都会覆盖之前的测试报告文件
        所以测试报告的名称常见的一般是时间戳的方式来进行命名，避免历史报告被覆盖的情况
        但是如果你是使用多线程的方式来执行套件，生成测试报告，则一定要把时间戳的单位精确到毫秒级别
    '''
    report_file = f'{report_dir}reportCN_{time.time()}.html'  # 测试报告的名称及保存路径

    report_tester = tester  # 测试执行人：CN测试报告额外的参数
    # 判断测试报告的保存路径是否存在
    if not os.path.exists(report_dir):  # 判断测试报告的保存路径是否存在
        os.mkdir(report_dir)  # 创建文件夹
    # HTMLTestReportCN库实现的测试报告。

    discover = c_cases(type_, pattern)
    with open(report_file, 'wb') as file:
        runner = HTMLTestRunner(stream=file, title=report_title, description=report_description, tester=report_tester,
                                verbosity=2)
        runner.run(discover)
    return report_file
