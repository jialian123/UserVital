#_*_encoding:utf-8_*_

import re
import hashlib
from urllib.parse import urlencode,unquote
import requests
requests.packages.urllib3.disable_warnings()
import math
import json

header = {
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
    'User-Agent': 'okhttp/3.12.6'
}
timeout = 10

class BaseRequest:
    def send_post(self,url,params,data,need_hash=False):
        res = {
            'http_code': None,
            'duration': None,
            'data': None
        }
        if need_hash:
            params['hash'] = self.get_hash(params)
        response = requests.post(url=url,headers=header,params=params,data=data,timeout=timeout,verify=False)
        second = response.elapsed.seconds
        millisecond = math.ceil(response.elapsed.microseconds / 1000)
        res['http_code'] = response.status_code
        res['duration'] = str(second * 1000 + millisecond)
        try:
            res['data'] = json.loads(response.content)
        except:
            res['data'] = response.content
        return res


    def send_get(self,url,params,need_hash=False):
        res = {
            'http_code': None,
            'duration': None,
            'data': None
        }
        if need_hash:
            params['hash'] = self.get_hash(params)
        response = requests.get(url=url,headers=header,params=params,timeout=timeout,verify=False)
        second = response.elapsed.seconds
        millisecond = math.ceil(response.elapsed.microseconds / 1000)
        res['http_code'] = response.status_code
        res['duration'] = str(second * 1000 + millisecond)
        try:
            res['data'] = json.loads(response.content)
        except:
            res['data'] = response.content
        return res

    def get_hash(self,params):
        url_params = re.sub(r"\r\n","",unquote(urlencode(params)) + "305%daf5g7ra05$#+6%pm!ud922u!(_t#elidt7q2t")
        return hashlib.md5(url_params.encode(encoding='UTF-8')).hexdigest()

request = BaseRequest()