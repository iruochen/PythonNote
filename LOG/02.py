'''

1. 需求

现在有以下几个日志记录的需求

    1） 要求将所有级别的所有日志都写入磁盘文件
    2） all.log 文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
    3） error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
    4） 要求all.log在每天凌晨进行日志切割
'''

import logging
import logging.handlers
import datetime

# 定义logger
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

# 为两个不同的文件设置不同的Handler
rf_handler = logging.handlers.TimedRotatingFileHandler("all.log", when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - &(levelname)s - %(message)s"))

f_handler = logging.FileHandler("error.log")
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# 把相应的处理器组装到logger上
logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
