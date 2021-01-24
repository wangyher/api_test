import os

from common.config import root_path
from common.log import Log

log = Log.get_logger(name="common_func")


class CommonFunction:

    def write_access_token_to_txt(self, filename, content):
        file_path = os.path.join(root_path, "conf", filename)
        with open(file_path, 'w') as f:
            f.write(content)
            log.info("access_token写入txt文件成功！")

    def red_access_token_txt(self, file_path):
        with open(file_path, 'r') as f:
            return f.readline()


if __name__ == '__main__':
    func = CommonFunction()
    file_path = "../conf/contacts_access_token.txt"
    print(func.red_access_token_txt(file_path))
