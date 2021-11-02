from api.baseapi import BaseApi
from api.wework import Wework
import pytest
def api(fun):
    def magic(*args, **kwargs):
        base_api: BaseApi = args[0]

        method=fun.__name__

        base_api.params=kwargs

        req=base_api.api_load('../api/department.yaml')[method]

        return base_api.api_send(req)
        # fun(*args, **kwargs)

    return magic



class Department(Wework):
    secret = 'e5QDaymap7Ymhmp_wyL7yqv2BM22Sx6iv6pLwo3X6Uc'
    # def __init__(self):
    #     self.secret ='e5QDaymap7Ymhmp_wyL7yqv2BM22Sx6iv6pLwo3X6Uc'

    def __init__(self):
        self.data = self.yaml_load('../api/department.yaml')
        self.secret = self.data['secret']


    def creat(self, params, **kwargs):
        self.params['params'] = params
        return self.api_send(self.data['creat'])


    def get(self,**kwargs):
        userid = "dfmfdsdfdddfsffddf"
        self.params['userid'] = userid
        return self.api_send(self.data['get'])


