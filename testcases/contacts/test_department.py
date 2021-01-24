import pytest
import allure
import json

from common.read_excel import get_excel_data
from apis.contacts.mange_department import ManageDepartment


class TestDepartment:
    @pytest.mark.parametrize("cases", get_excel_data("contacts_manage", "create_department"))
    @allure.story("创建部门管理")
    @pytest.mark.run(order=1)
    def test_creat_department(self, cases: dict):
        url = cases.get("case_url")
        payload = json.loads(cases.get("case_body"))
        expect = json.loads(cases.get("case_expect"))
        md = ManageDepartment()
        md.create_department(url, payload)
        res = md.get_response()
        assert res.get("errcode") == expect.get("errcode")

    @pytest.mark.parametrize("cases", get_excel_data("contacts_manage", "update_department"))
    @allure.story("更新部门管理")
    @pytest.mark.run(order=2)
    def test_update_department(self, cases: dict):
        url = cases.get("case_url")
        payload = json.loads(cases.get("case_body"))
        expect = json.loads(cases.get("case_expect"))
        md = ManageDepartment()
        md.update_department(url, payload)
        res = md.get_response()
        assert res.get("errcode") == expect.get("errcode")

    @pytest.mark.parametrize("cases", get_excel_data("contacts_manage", "get_department_list"))
    @allure.story("获取部门管理列表")
    @pytest.mark.run(order=3)
    def test_get_department_list(self, cases: dict):
        url = cases.get("case_url")
        param = json.loads(cases.get("case_params"))
        expect = json.loads(cases.get("case_expect"))
        md = ManageDepartment()
        md.get_department_list(url, param)
        res = md.get_response()
        # print(res)
        assert res.get("errcode") == expect.get("errcode")

    @pytest.mark.parametrize("cases", get_excel_data("contacts_manage", "delete_department"))
    @allure.story("删除部门管理")
    @pytest.mark.run(order=3)
    def test_delete_department(self, cases: dict):
        url = cases.get("case_url")
        param = json.loads(cases.get("case_params"))
        expect = json.loads(cases.get("case_expect"))
        md = ManageDepartment()
        md.delete_department(url, param)
        res = md.get_response()
        assert res.get("errcode") == expect.get("errcode")
