'''
    读取ini配置文件中的logging，实现日志的输出和记录
        要读取配置文件，需要通过logging.config来实现
    配置ini文件的相对绝对路径，就是根据工程路径来获取它的绝对路径。
        基于pathLib库来实现文件路径的获取
'''
import logging.config
import pathlib

# 封装日志记录器的函数
def getLogger():
    # 读取配置文件
    # logging.config.fileConfig(path, encoding='utf-8')
    # 获取当前文件所在的路径
    file_path = pathlib.Path(__file__)
    # 获取当前文件的上一级
    dir = file_path.parents[0].resolve()  # 返回路径对象
    # 基于上一级获取到log_conf.ini文件
    file = dir / 'log_conf.ini'
    logging.config.fileConfig(file, encoding='utf-8')
    # 获取记录器
    logger = logging.getLogger()
    return logger  # 一定记得要return，不然无法获取logger对象，来实现日志的输出记录


# 获取记录器
# logger = getLogger()
# logger.debug('这是配置文件的debug')
# logger.info('这是配置文件的info')
# logger.error('这是配置文件的error')

