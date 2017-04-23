#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Domain(object):
    '''
    DNSPod domain
    '''

    def __init__(self, dictionary):
        for k, v in dictionary.iteritems():
            setattr(self, k, v)

class DomainAPI(object):
    '''DNSPod API start with **Domain.\***.'''

    def __init__(self, api):
        '''Initalize object with BaseAPI

        :param api: Instance of `BaseAPI`
        '''
        self._api = api

    def info(self, domain_id=None, domain=None):
        '''Get information for a specific domain.

        Specify a domain by either ``domain_id`` or ``domain``, if both are
        specified, then ``domain_id`` is used.
        
        :param str domain_id: Domain ID
        :param str domain: Domain
        :return: Domain object
        '''
        if domain_id != None:
            r = self._api.do_post('Domain.Info', domain_id=domain_id)
        elif domain != None:
            r = self._api.do_post('Domain.Info', domain=domain)
        else:
            # TODO throw exception
            pass
        return Domain(r['domain'])
