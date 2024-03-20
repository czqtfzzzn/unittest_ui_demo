import pathlib
import openpyxl


# excel 读取
# excel 读取数据处理
# excel 写入

class DataExcel:
    def __init__(self, data_filename):
        self.filepath = f'{pathlib.Path(__file__).parents[1].resolve()}/test_data/{data_filename}'
        # print(self.filepath)

    # 解析数据
    def argument(self, value):
        # 参数解析处理，将str的xxx=xxx的格式转换为字典的形态，然后通过**的方式传入到对应的操作方法之中
        da = dict()
        if value:  # 因为value可能为none，所以要提前判断一下
            str_temp = value.split(';')  # 可能参数有多个，基于;进行分割，所以提前分割好参数的数量
            for temp in str_temp:
                # temp: by=id    value=kw     txt=xxxxx
                t = temp.split('=', 1)  # 基于=进行1次分割操作
                da[t[0]] = t[1]  # 将分割后的t的两个元素，作为key和value，进行保存
                # data["type_"] = "Chrome"  # 对字典中的指定key进行value的赋值，于是data={"type_":"Chrome"}
        return da

    # 读取excel
    def read_excel(self):
        self.data_dict = {}
        excel = openpyxl.load_workbook(self.filepath)
        sheets = excel.sheetnames  # 获取所有的sheet页的名字
        for name in sheets:
            self.data_dict[name] = []
            sheet = excel[name]
            # 单个测试用例字典
            self.item_dict = {}
            for values in sheet.values:
                if type(values[0]) is int:
                    self.item_dict[values[0]] = {
                        'key': values[1],
                        'value': self.argument(values[2])
                    }
                if type(values[0]) is not int:
                    if self.item_dict != {}:
                        self.data_dict[name].append(self.item_dict)
                    self.item_dict = {}
        # print(self.data_dict)
        return self.data_dict

# de = DataExcel('test_login.xlsx')
# de.read_excel()
