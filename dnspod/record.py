#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Record(object):
    '''
    DNSPod record
    '''

    TYPE_A = 'A'
    TYPE_NS = 'NS'

    LINE_DEFAULT = '默认'

    def __init__(self, dictionary):
        for k, v in dictionary.iteritems():
            # transform key name from Record.List to Record.Info
            key_transform = {
                'name': 'sub_domain',
                'line': 'record_line',
                'type': 'record_type',
            }
            if k in key_transform:
                k = key_transform[k]
            setattr(self, k, v)

class RecordAPI(object):
    '''DNSPod API start with **Record.\***'.'''

    def __init__(self, api):
        self._api = api

    def list(self, domain_id):
        '''
        Get the record list of specfic domain
        '''
        r = self._api.do_post('Record.List', domain_id=domain_id)
        record_list = []
        for record in r['records']:
            record['domain_id'] = domain_id
            record_list.append(Record(record))
        return record_list

    def ddns(self, domain_id, record_id, sub_domain, record_line, value):
        '''
        Update record dynamically
        '''
        record = self.info(domain_id, record_id)
        # If everything stay the same, no need to update
        if record.sub_domain == sub_domain and \
           record.record_line == record_line and \
           record.value == value:
            return
        self._api.do_post('Record.Ddns', domain_id=domain_id,
                          record_id=record_id, sub_domain=sub_domain,
                          record_line=record_line, value=value)

    def info(self, domain_id, record_id):
        r = self._api.do_post('Record.Info', domain_id=domain_id,
                              record_id=record_id)
        return Record(r['record'])
