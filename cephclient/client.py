#   Copyright 2010 Jacob Kaplan-Moss
#   Copyright 2011 OpenStack Foundation
#   Copyright 2011 Piston Cloud Computing, Inc.
#   Copyright 2013 David Moreau Simard
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   Author: David Moreau Simard <moi@dmsimard.com>
#   Credit: python-novaclient
#

"""
A ceph-rest-api python interface that handles REST calls and responses.
"""

import logging
import requests

from cephclient import exceptions

try:
    import json
except ImportError:
    import simplejson as json

class CephClient(object):

    USER_AGENT = 'python-cephclient'

    def __init__(self, **params):
        """
        Initialize the class, get the necessary parameters
        """
        self.params = params
        self.log = self.log_wrapper()

        self.log.debug("Params: {0}".format(str(self.params)))

        self.endpoint = self.params['endpoint']
        if 'timeout' not in self.params:
            self.timeout = None

        self.http = requests.Session()

    def _request(self, url, method, **kwargs):
        kwargs.setdefault('headers', kwargs.get('headers', {}))
        kwargs['headers']['User-Agent'] = self.USER_AGENT
        kwargs['headers']['Accept'] = 'application/json'
        if 'body' in kwargs:
            kwargs['headers']['Content-Type'] = 'application/json'
            kwargs['data'] = json.dumps(kwargs['body'])
            del kwargs['body']
        if self.timeout is not None:
            kwargs.setdefault('timeout', self.timeout)

        self.log.debug("{0} URL: {1}{2} - {3}".format(method,
                                                        self.endpoint,
                                                        url,
                                                        str(kwargs)))

        resp = self.http.request(
            method,
            self.endpoint + url,
            **kwargs)

        if resp.text:
            try:
                body = json.loads(resp.text)
            except ValueError:
                body = None
        else:
            body = None

        return resp, body

    def get(self, url, **kwargs):
        return self._request(url, 'GET', **kwargs)

    def post(self, url, **kwargs):
        return self._request(url, 'POST', **kwargs)

    def put(self, url, **kwargs):
        return self._request(url, 'PUT', **kwargs)

    def delete(self, url, **kwargs):
        return self._request(url, 'DELETE', **kwargs)

    @staticmethod
    def urls(key):
        """
        Provides a map of available URLs through more convenient keys
        """
        map = {
            'fsid': 'fsid',
            'cluster_health': 'health',
            'monitor_status': 'mon_status',
            'osd_listids': 'osd/ls',
            'osd_lspools': 'osd/lspools',
            'osd_tree':  'osd/tree',
            'pg_status': 'pg/stat',
            'disk_free': 'df',
            'osd_stat': 'osd/stat',
            'report': 'report',
            'osd_details': 'osd/dump',
            'osd_perf': 'osd/perf',
        }

        if key not in map:
            raise exceptions.UrlNotMappedException()

        return map[key]

    def log_wrapper(self, verbosity = False):
        """
        Wrapper to set logging parameters for output
        """
        log = logging.getLogger("client.py")

        # Set the log format and log level
        if self.params["debug"]:
            log.setLevel(logging.DEBUG)
        else:
            log.setLevel(logging.INFO)

        # Set the log format. Also, error and critical log messages should be sent to stderr
        stream = logging.StreamHandler()
        logformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%b %d %H:%M:%S')
        stream.setFormatter(logformat)

        log.addHandler(stream)
        return log