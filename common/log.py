import logging
import time
import os
import sys

from common.config import Config, root_path


class Log:
    @classmethod
    def config_log(cls, name=None):
        cf = Config()
        log_dir = os.path.join(root_path, cf.get_runtime("log_dir"))
        current_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        log_file = os.path.join(log_dir, current_time + ".log")

        # 获取一个标准的logger, 配置loglevel
        cls.logger = logging.getLogger(name)
        cls.logger.setLevel(eval("logging." + cf.get_runtime("log_level").upper()))

        # 建立不同handler
        fh = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        ch = logging.StreamHandler()

        # 定义输出格式
        ft = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(ft)
        ch.setFormatter(ft)

        # 把定制handler 添加到我们logger
        cls.logger.addHandler(fh)
        cls.logger.addHandler(ch)

    @classmethod
    def get_logger(cls, name=None):
        cls.config_log(name)
        return cls.logger


if __name__ == "__main__":
    l = Log.get_logger()
    print(type(l))
    l.info("abc")
    l.debug("hello, debug")

