import json,allure

from jsonpath import jsonpath
import requests, yaml

from api.log import Get_log


class BaseApi():
    params = {}

    @classmethod
    def format(cls, r):
        cls.r = r
        Get_log().log_info(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))

    @classmethod
    def yaml_load(cls, path):
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)

    def jsonpath(self, path, r=None, **kwargs):
        if r is None:
            r = self.r.json()
        try:
            return jsonpath(r, path)[0]
        except :
            Get_log().log_error(r['errcode'])


    def api_load(self, path):
        return self.yaml_load(path)

    def api_send(self, req: dict):
        req['params']['access_token'] = self.get_token(self.secret)
        # 模板替换
        raw = yaml.dump(req)
        for key, value in self.params.items():
            raw = raw.replace(f'${{{key}}}', repr(value))
            print(raw)
        req = yaml.safe_load(raw)
        print(req)

        r = requests.request(
            method=req['method'],
            url=req['url'],
            params=req['params'],
            json=req.get('json')
        )
        self.format(r)
        return r.json()

    def api_steps(self, steps: list):
        for step in steps:
            raw = yaml.dump(step)
            for key, value in self.params.items():
                raw = raw.replace(f'${{{key}}}', repr(value))
            step = yaml.safe_load(raw)
            if isinstance(step, dict):
                if 'method' in step.keys():
                    Get_log().log_info('正在测试'+ step['method'])
                    allure.attach(step['method']+'测试')
                    method = step['method'].split('.')[-1]
                    getattr(self, method)(**step)
                if "path" in step.keys():
                    self.code = getattr(self, 'jsonpath')(**step)
                if 'assertion' in step.keys():
                    try:
                        assert self.code == step['assertion']
                    except Exception as e:
                        Get_log().log_error(self.code)
                        allure.attach(self.code)
                        raise e
