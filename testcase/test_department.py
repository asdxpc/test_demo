from api.baseapi import BaseApi
from api.department import Department
from api.wework import Wework
import pytest
from jsonpath import jsonpath
import allure
class TestDepartment:
    data = BaseApi().api_load('test.yaml')

    params = [{
        "userid": "djksdshf",
        "name": "dfgdwwsdhfd",
        "mobile": "+86 13800504510",
        "department": [1, 2],

    }, {
        "userid": "dfjsfsfsfb",
        "name": "dghsfsfd",
        "alias": "jackxzfgfhang",
        "mobile": "+86 13800525110",
        "department": [1, 2]
    }]

    def setup(self):
        self.department = Department()


    @allure.step('测试')
    @pytest.mark.parametrize('userid',['dfmfdsdfdddfsffddf','djkfhdsjfdss'])
    def test_get(self,userid):
        self.department.params['useird'] =userid
        self.department.api_steps(self.data)

    @pytest.mark.parametrize('params',params)
    def test_creat(self,params,**kwargs):
        self.department.params['params'] = params
        self.department.api_steps(self.data['creat'])

    def test_get1(self):
        self.department.params['userid'] = 'djkhf'
        self.department.api_steps(self.data)


