import pytest
import allure
from common.logger import logger
from testcases.conftest import api_data
from operation.user import new_login_user,get_user_info
from operation.user import add_user


@allure.step("步骤1 ==>> 新增用户")

def step_1(add_usernick,add_username,add_password):
    logger.info("步骤1 ==>> 新增用户 ==>> {}, {}, {}".format(add_usernick,add_username,add_password))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取用户信息模块")
class Test_get_user_info():
    """获取用户信息"""
    @allure.story("用例--获取用户信息")
    @allure.description("该用例是获取用户信息的测试")
    @allure.title("测试数据：【 {add_usernick},{add_username},{add_password}, {except_code}, {except_msg}】")
    @pytest.mark.single
    # @pytest.mark.usefixtures("delete_get_user_info")
    @pytest.mark.parametrize("add_usernick,add_username,add_password, except_code, except_msg",api_data["test_get_User_info"])
    def test_get_user_info(self,admin_login_token,add_usernick,add_username,add_password, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        res_token = admin_login_token
        add_user(add_usernick,add_username,add_password,res_token)

        step_1(add_usernick,add_username,add_password)
        if res_token is not None:
            result = get_user_info(res_token)
            res_json = result.get_response_json()
            nicknames = [row["nickName"] for row in res_json["rows"]]
            assert add_usernick in nicknames
            assert result.response.status_code == int(except_code)
            assert result.msg == except_msg




if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_get_user_info.py"])