#!/usr/bin/env python
#-*- coding: utf-8 -*-

class InfoAPI(object):
    '''DNSPod API start with **Info.\***.'''

    def __init__(self, api):
        '''Initalize object with BaseAPI

        :param api: Instance of `BaseAPI`
        '''
        self._api = api

    def version(self):
        '''Get API version

        :return: API version
        :rtype: str
        '''
        r = self._api.do_post('Info.Version')
        return r['status']['message']
