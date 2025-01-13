import pytest
from testcases.conftest import api_data
from api.user import user
import allure
from common.logger import logger



allure.step("步骤1 ==>> 用户登陆")
def step_login(username):
    logger.info("步骤1 ==> 登陆用户{}".format(username))


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return api_data.get(testcase_name)


@pytest.fixture(scope="session")
def admin_login_json(username='admin', password='admin123', uuid='3f580c31d49c4f8cab1636187cc50157'):
    json = {
        "username": username,
        "password": password,
        "uuid": uuid
    }
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    res = user.login(json=json, headers=header)
    step_login(username)
    yield res.json()

@pytest.fixture(scope="session")
def admin_login_token(username='admin', password='admin123', uuid='3f580c31d49c4f8cab1636187cc50157'):
    json = {
        "username": username,
        "password": password,
        "uuid": uuid
    }
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    res = user.login(json=json, headers=header)
    res_token = res.json().get("token")
    print("获取到 token:", res_token)
    yield res_token



