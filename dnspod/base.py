#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests

class BaseAPI(object):
    '''BaseAPI is used by every other API objects.

    BaseAPI hold informations that will used by other API objects during every
    API operation.
    '''

    LANG_EN = 'en'
    LANG_CN = 'cn'
    DEFAULT_API_URL = 'https://dnsapi.cn/'

    def __init__(self, login_token, lang=LANG_EN, api_url=DEFAULT_API_URL):
        '''Initialize object with DNSPod account and options

        :param str login_token: API security token. (token_id + ',' + token_string)
        :param str lang: Error returning language. By default, ``LANG_EN`` is
                         used, avaliable values: ``LANG_EN``, ``LANG_CN``
        :param str api_url: API url, default: ``DEFAULT_API_URL``
        '''
        self.login_token = login_token
        self.format = 'json'
        self.lang = lang
        self.api_url = api_url

    def do_post(self, interface, **params):
        common_param = {
            'login_token': self.login_token,
            'format': self.format,
            'lang': self.lang,
        }
        params.update(common_param)
        r = requests.post(self.api_url + interface, data=params)
        data = r.json()
        if data['status']['code'] != '1':
            # TODO throw exception
            pass
        return data
