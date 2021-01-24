import configparser
import os


root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config:
    def __init__(self, filename="default.conf"):
        self.cf = configparser.ConfigParser()
        self.cf.read(os.path.join(root_path, "conf", filename))

    def get_runtime(self, option):
        return self.cf.get("runtime", option)

    def get_access(self, option):
        return self.cf.get("access", option)

    def get_secret(self, option):
        """获取各应用的密钥"""
        return self.cf.get("secret", option)


if __name__ == '__main__':
    c = Config()
    print(c.get_runtime(option="log_dir"))
    print(c.get_runtime(option="timeout"))
    print(c.get_access("token_url"))
