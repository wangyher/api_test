import sys
import time
import pytest
import subprocess

sys.path.append("../")
current_time = time.strftime("%Y%m%d", time.localtime(time.time()))

if __name__ == "__main__":
    # allure 报告生成路径
    report_path = "./report/report_{}".format(current_time)
    report_html_path = report_path + "/html"

    # 生成 allure 测试报告
    pytest.main(['-sq', '--disable-warnings', '--alluredir', report_path, "./testcases"])
    command = "allure generate --clean " + report_path + " -o " + report_html_path
    print(subprocess.getstatusoutput(command))

