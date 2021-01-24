import os
import allure
import json

from apis.base_api import BaseApi
from common.config import root_path
from common.log import Log

log = Log.get_logger("manger_department")


class ManageDepartment(BaseApi):
    def __init__(self):
        BaseApi.__init__(self)
        application_name = "contacts"
        # 判断当前token是否过期
        token_path = os.path.join(root_path, "conf", "contacts_access_token.txt")
        # token_path = "../../conf/contacts_access_token.txt"
        self.judge_access_token_is_valid(application_name, token_path)
        self.access_token = self.func.red_access_token_txt(token_path)
        # print("<<access_token>>:", self.access_token)

    def create_department(self, url, payload):
        """创建部门"""

        with allure.step("获取创建新部门请求参数"):
            params = {
                "access_token": self.access_token
            }
        log.info("url: " + str(url))
        log.info("payload:  {}".format(payload))
        with allure.step("发出创建新部门的请求"):
            self.send_post_json(url, payload, params=params)

    def update_department(self, url, payload):
        """更新部门"""

        with allure.step("获取更新部门请求参数"):
            params = {
                "access_token": self.access_token
            }
        log.info("url: " + str(url))
        log.info("payload:  {}".format(payload))
        with allure.step("发出更新部门的请求"):
            self.send_post_json(url, payload, params=params)

    def delete_department(self, url, param):
        with allure.step("发送删除部门请求参数"):
            params = {
                "access_token": self.access_token
            }
            params.update(param)
        log.info("url: " + str(url))
        log.info("params: " + str(params.get("id")))

        with allure.step("发送删除部门的请求"):
            self.send_get(url, params=params)

    def get_department_list(self, url, param):
        with allure.step("获取部门列表请求参数"):
            params = {
                "access_token": self.access_token
            }
            params.update(param)
        log.info("url: " + str(url))
        log.info("params: " + str(params))

        with allure.step("发送部门列表的请求"):
            self.send_get(url, params=params)


if __name__ == '__main__':
    d = ManageDepartment()
