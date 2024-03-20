'''
    读取ini配置文件中的内容，实现对配置项的自动配置
    读取ini格式的文件，需要调用configparser库。也是官方自带库。
'''
import configparser
import pathlib


# 读取配置文件
def read(filename):
    # 获取配置文件
    file = pathlib.Path(__file__).parents[0].resolve() / filename
    # 通过configparser实现对ini文件的读取。
    conf = configparser.ConfigParser()  # 创建一个配置文件对象
    conf.read(file)  # 读取指定的配置文件
    # 获取ini文件中的相关内容
    values = dict(conf.items('conf'))  # 基于section来获取指定的配置项，转为dict类型
    # print(values)
    return values
# read('email_conf.ini')
