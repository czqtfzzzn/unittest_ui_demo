from test_case.test_suite import *
from conf.email_send import SendMail

s_email = SendMail()


def run():
    # 定义参数
    type_ = "discover"
    pattern = "test_excel_demo.py"
    tester = "成紫乾"
    html_path = c_html(type_, pattern, tester)
    # print(html_path)
    e_title = "登录流程测试报告"
    e_txt = "成紫乾的测试报告，请查收"
    s_email.sendMail(e_title, e_txt, html_path)


if __name__ == '__main__':
    run()
