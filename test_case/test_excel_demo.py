import unittest
from conf.data_excel import DataExcel
from ddt import ddt, data
from web_keys.web_keys import WebKeys

# 读取excel数据
e_data = DataExcel('test_login.xlsx').read_excel()
web = WebKeys()


@ddt
class LoginTest(unittest.TestCase):
    def tearDown(self):
        web.quit()
        web.log.info("关闭浏览器")

    @data(*e_data['登录流程'])
    def test_login(self, item_dict):
        self.pub_case(item_dict)

    # @data(*e_data['修改信息流程'])
    # def test_changeinfo(self, item_dict):
    #     self.pub_case(item_dict)

    # 执行测试步骤
    def pub_case(self, item_dict):
        for num, value in item_dict.items():
            if 'assert' in value['key']:
                self.asserts(value['key'], value['value'])
            else:
                getattr(web, value['key'])(**value['value'])
                web.log.info(value['value'])

    # 进行断言处理
    def asserts(self, ass_key, ass_dict):
        self.assertTrue(getattr(web, ass_key)(ass_dict))
        web.log.info('断言结束')


# if __name__ == '__main__':
#     unittest.main()
