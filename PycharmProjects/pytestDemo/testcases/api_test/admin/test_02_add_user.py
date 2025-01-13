import pytest
import allure
from operation.user import add_user
from testcases.conftest import api_data
from common.logger import logger


@allure.step("步骤1 ==>> 新增用户")
def step_1(add_usernick,add_username,add_password):
    logger.info("步骤1 ==>> 新增用户 ==>> {}, {}, {}".format(add_usernick,add_username,add_password))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("新增用户模块")
class Test_add_user():
    """新增用户"""
    @allure.story("用例--注册用户信息")
    @allure.description("该用例是针对获取用户注册接口的测试")
    @allure.title(
        "测试数据：【 {add_usernick},{add_username},{add_password}, {except_code}, {except_msg}】")
    @pytest.mark.single
    @pytest.mark.usefixtures("delete_add_user")
    @pytest.mark.parametrize("add_usernick,add_username,add_password, except_code, except_msg",api_data["test_add_User"])
    def test_add_user(self,admin_login_token,add_usernick,add_username,add_password, except_code, except_msg):
        logger.info("-------------开始执行用例-------------")
        res_token = admin_login_token
        step_1(add_usernick, add_username, add_password)
        if res_token is not None:
            result = add_user(add_usernick,add_username,add_password,res_token)
            assert result.response.status_code == int(except_code)
            assert result.msg == except_msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_add_user.py"])