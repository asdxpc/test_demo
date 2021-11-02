from api.baseapi import BaseApi


def _path(path):


def api(fun,path):
    def magic(*args, **kwargs):
        base_api: BaseApi = args[0]

        method=fun.__name__

        base_api.params=kwargs
        req=base_api.api_load(path)[method]
        return base_api.api_send(req)
        # fun(*args, **kwargs)

    return magic