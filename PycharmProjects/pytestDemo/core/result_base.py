import requests
import json as complexjson
from common.logger import logger
class ResultBase():
    def __init__(self):
        # 存储请求是否成功，默认为 False
        self.success = False
        # 存储错误信息，默认为 None
        self.error = None
        # 存储返回的消息，默认为 None
        self.message = None
        # 存储返回的数据，默认为 None
        self.data = None
        # 存储返回的状态码，默认为 None
        self.status_code = None
        # 存储可能的 token，默认为 None
        self.token = None
        # 存储原始响应，默认为 Noneresponse
        self.response = None

        self.json = None

    def set_success(self, success):
        self.success = success

    def set_error(self, error):
        self.error = error

    def set_message(self, message):
        self.message = message

    def set_data(self, data):
        self.data = data

    def set_status_code(self, status_code):
        self.status_code = status_code

    def set_token(self, token):
        self.token = token

    def set_response(self, response):
        self.response = response

    def get_response_json(self):
        if self.response:
            try:
                return self.response.json()
            except ValueError:
                return None
        else:
            return None

    def get_response_text(self):
        if self.response:
            return self.response.text()
        else:
            return None


