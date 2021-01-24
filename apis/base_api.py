import requests

from common.config import root_path, Config
from common.log import Log
from common.common_func import CommonFunction

log = Log.get_logger(name="base_api")


class BaseApi:
    def __init__(self):
        self.cf = Config()
        self.func = CommonFunction()

    def send_post_json(self, url, json_obj, params=None):
        if params:
            self.res = requests.post(url, json=json_obj, params=params)
        else:
            self.res = requests.post(url, json=json_obj)

    def send_get(self, url, params):
        self.res = requests.get(url, params=params)

    def get_response(self):
        return self.res.json()

    def get_access_token(self, application_name):
        """获取access_token"""

        # 请求参数获取
        token_url = self.cf.get_access("token_url")
        corp_id = self.cf.get_access("corp_id")
        corp_secret = self.cf.get_secret("{}_secret".format(application_name))

        params = {
            "corpid": corp_id,
            "corpsecret": corp_secret
        }
        # 请求access_token接口
        response = requests.get(token_url, params=params)

        access_token = response.json().get("access_token")
        log.info("获取access_token成功！")

        # 将获取到的token存入文件中，暂时存入TXT文件中
        txt_file_name = application_name + "_access_token.txt"
        self.func.write_access_token_to_txt(txt_file_name, access_token)

    def judge_access_token_is_valid(self, application_name, token_path):
        """判断access_toekn是否过期"""

        ip_url = self.cf.get_access("ip_url")
        access_token = self.func.red_access_token_txt(token_path)
        params = {
            "access_token": access_token
        }

        res = requests.get(ip_url, params=params)

        # 判断access_token是否过期
        if res.json().get("errcode") in [40014, 41001, 42001]:
            log.info("access_token已过期，正在重新生成......")
            self.get_access_token(application_name)


if __name__ == '__main__':
    token_path = "../conf/contacts_access_token.txt"
    b = BaseApi()
    b.judge_access_token_is_valid("contactss", token_path)
