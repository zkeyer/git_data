
import allure
import pytest
from testcases.conftest import api_data
from common.logger import logger

allure.step("步骤1 ==>> 用户登陆")
def step1(username):
    logger.info("步骤1 ==> 登陆用户{}".format(username))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口测试")
@allure.feature("用户登陆模块")
class Test_admin_User_login():
    @allure.story("用例--admin登陆用户")
    @allure.description("该用例是针对获取admin用户登陆时接口的测试")
    @allure.title("测试数据：【{username},{password},{uuid},{except_code},{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("username, password, uuid, except_code, except_msg", api_data["test_new_User_login"])
    def test_user_login(self,admin_login, username, password, uuid, except_code, except_msg):
        logger.info("-------------开始执行用例{}-------------")
        result = admin_login
        if result is not None:
            respone_code = result.get("code")
            assert respone_code == 200
            assert result.get("msg") == except_msg, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.get("code")))



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_admin_login.py"])
