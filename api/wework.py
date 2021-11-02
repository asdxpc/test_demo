from api.baseapi import BaseApi
import requests

class Wework(BaseApi):
     corpid = 'ww64aee6fd9ad7e31d'
     token = dict()
     token_time = dict
     secret =''

     def get_access_token(self,secret=secret):
         if secret is None:
             return self.token[secret]
         if secret not in self.token.keys():
             self.token[secret] =self.get_token(secret)
             return self.token[secret]


     @classmethod
     def get_token(cls,secret):
         base_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
         r = requests.get(base_url,
                          params={'corpid':cls.corpid,
                                  'corpsecret':secret}
                          )
         print(r.json())
         return r.json()['access_token']




if __name__ =='__main__':
    secret = 'e5QDaymap7Ymhmp_wyL7yqv2BM22Sx6iv6pLwo3X6Uc'
    a =Wework().get_access_token(secret)
    print(a)
    Wework()._p

