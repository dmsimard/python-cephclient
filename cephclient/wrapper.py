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
#

import cephclient.client as client
import cephclient.exceptions as exceptions

try:
    import json
except ImportError:
    import simplejson as json

class CephWrapper(client.CephClient):
    def __init__(self, **params):
        super(CephWrapper, self).__init__(**params)
        self.user_agent = 'python-cephclient-wrapper'

    ###
    # root GET calls
    ###
    def get_df(self, **kwargs):
        try:
            detail = kwargs['detail']
            del kwargs['detail']
            return self.get('df?detail={0}'.format(detail), **kwargs)
        except KeyError as e:
            return self.get('df', **kwargs)

    def get_fsid(self, **kwargs):
        return self.get('fsid', **kwargs)

    def get_health(self, **kwargs):
        try:
            detail = kwargs['detail']
            del kwargs['detail']
            return self.get('health?detail={0}'.format(detail), **kwargs)
        except KeyError as e:
            return self.get('health', **kwargs)

    def get_quorum_status(self, **kwargs):
        return self.get('quorum_status', **kwargs)

    def get_report(self, **kwargs):
        return self.get('report', **kwargs)

    def get_status(self, **kwargs):
        return self.get('status', **kwargs)

    ###
    # auth GET calls
    ###
    def auth_export(self, **kwargs):
        try:
            entity = kwargs['entity']
            del kwargs['entity']
        except KeyError as e:
            raise exceptions.MissingRequiredArgument(e)

        return self.get('auth/export?entity={0}'.format(entity), **kwargs)

    def auth_get(self, **kwargs):
        try:
            entity = kwargs['entity']
            del kwargs['entity']
        except KeyError as e:
            raise exceptions.MissingRequiredArgument(e)

        return self.get('auth/get?entity={0}'.format(entity), **kwargs)

    def auth_get_key(self, **kwargs):
        try:
            entity = kwargs['entity']
            del kwargs['entity']
        except KeyError as e:
            raise exceptions.MissingRequiredArgument(e)

        return self.get('auth/get-key?entity={0}'.format(entity), **kwargs)

    def auth_list(self, **kwargs):
        return self.get('auth/list', **kwargs)

    def auth_print_key(self, **kwargs):
        try:
            entity = kwargs['entity']
            del kwargs['entity']
        except KeyError as e:
            raise exceptions.MissingRequiredArgument(e)

        return self.get('auth/print-key?entity={0}'.format(entity), **kwargs)

    ###
    # config-key GET calls
    ###
    def config_key_exists(self, **kwargs):
        try:
            key = kwargs['key']
            del kwargs['key']
        except KeyError as e:
            raise exceptions.MissingRequiredArgument(e)

        return self.get('config-key/exists?key={0}'.format(key), **kwargs)

    def config_key_get(self, **kwargs):
        try:
            key = kwargs['key']
            del kwargs['key']
        except KeyError as e:
            raise exceptions.MissingRequiredArgument(e)

        return self.get('config-key/get?key={0}'.format(key), **kwargs)

    def config_key_list(self, **kwargs):
        return self.get('config-key/list', **kwargs)

    ###
    # mds GET calls
    ###

    def mds_compat_show(self, **kwargs):
        return self.get('mds/compat/show', **kwargs)

    def mds_dump(self, **kwargs):
        try:
            epoch = kwargs['epoch']
            del kwargs['epoch']
            return self.get('mds/dump?epoch={0}'.format(epoch), **kwargs)
        except KeyError as e:
            return self.get('mds/dump', **kwargs)

    def mds_getmap(self, **kwargs):
        try:
            epoch = kwargs['epoch']
            del kwargs['epoch']
            return self.get('mds/getmap?epoch={0}'.format(epoch), **kwargs)
        except KeyError as e:
            return self.get('mds/getmap', **kwargs)

    def mds_stat(self, **kwargs):
        return self.get('mds/stat', **kwargs)

    ###
    # osd GET calls
    ###
    def osd_blacklist_ls(self, **kwargs):
        return self.get('osd/blacklist/ls', **kwargs)

    def osd_crush_dump(self, **kwargs):
        return self.get('osd/crush/dump', **kwargs)

    def osd_crush_rule_dump(self, **kwargs):
        return self.get('osd/crush/rule/dump', **kwargs)

    def osd_crush_rule_list(self, **kwargs):
        return self.get('osd/crush/rule/list', **kwargs)

    def osd_crush_rule_ls(self, **kwargs):
        return self.get('osd/crush/rule/ls', **kwargs)

    def osd_dump(self, **kwargs):
        try:
            epoch = kwargs['epoch']
            del kwargs['epoch']
            return self.get('osd/dump?epoch={0}'.format(epoch), **kwargs)
        except KeyError as e:
            return self.get('osd/dump', **kwargs)

    def osd_find(self, **kwargs):
        try:
            id = kwargs['id']
            del kwargs['id']
        except KeyError as e:
            raise exceptions.MissingRequiredArgument(e)

        return self.get('osd/find?id={0}'.format(id), **kwargs)

    def osd_getcrushmap(self, **kwargs):
        # Could not get this to work yet
        raise exceptions.FunctionNotImplemented()

    def osd_getmap(self, **kwargs):
        # Could not get this to work yet
        raise exceptions.FunctionNotImplemented()

    def osd_getmaxosd(self, **kwargs):
        return self.get('osd/getmaxosd', **kwargs)

    def osd_ls(self, **kwargs):
        try:
            epoch = kwargs['epoch']
            del kwargs['epoch']
            return self.get('osd/ls?epoch={0}'.format(epoch), **kwargs)
        except KeyError as e:
            return self.get('osd/ls', **kwargs)

    def osd_lspools(self, **kwargs):
        try:
            auid = kwargs['auid']
            del kwargs['auid']
            return self.get('osd/lspools?auid={0}'.format(auid), **kwargs)
        except KeyError as e:
            return self.get('osd/lspools', **kwargs)

    def osd_map(self, **kwargs):
        raise exceptions.FunctionNotImplemented()

    def osd_perf(self, **kwargs):
        return self.get('osd/perf', **kwargs)

    def osd_pool_get(self, **kwargs):
        try:
            pool = kwargs['pool']
            del kwargs['pool']

            var = kwargs['var']
            del kwargs['var']

        except KeyError as e:
            raise exceptions.MissingRequiredArgument(e)

        return self.get('osd/pool/get?pool={0}&var={1}'.format(
            pool, var), **kwargs)

    def osd_pool_stats(self, **kwargs):
        try:
            pool = kwargs['pool']
            del kwargs['pool']
            return self.get('osd/pool/stats?pool={0}'.format(pool), **kwargs)
        except KeyError as e:
            return self.get('osd/pool/stats', **kwargs)

    def osd_stat(self, **kwargs):
        return self.get('osd/stat', **kwargs)

    def osd_tree(self, **kwargs):
        try:
            epoch = kwargs['epoch']
            del kwargs['epoch']
            return self.get('osd/tree?epoch={0}'.format(epoch), **kwargs)
        except KeyError as e:
            return self.get('osd/tree', **kwargs)

    ###
    # mon GET calls
    ###
    def mon_dump(self, **kwargs):
        try:
            epoch = kwargs['epoch']
            del kwargs['epoch']
            return self.get('mon/dump?epoch={0}'.format(epoch), **kwargs)
        except KeyError as e:
            return self.get('mon/dump', **kwargs)

    def mon_getmap(self, **kwargs):
        # Could not get this to work yet
        raise exceptions.FunctionNotImplemented()

    def mon_stat(self, **kwargs):
        # TODO: Seems broken ? Returns null.
        return self.get('mon/stat', **kwargs)

    def mon_status(self, **kwargs):
        return self.get('mon_status', **kwargs)

    ###
    # pg GET calls
    ###
    def pg_debug(self, **kwargs):
        try:
            debugop = kwargs['debugop']
            del kwargs['debugop']
        except KeyError as e:
            raise exceptions.MissingRequiredArgument(e)

        return self.get('pg/debug?debugop={0}'.format(debugop), kwargs)

    def pg_dump(self, **kwargs):
        raise exceptions.FunctionNotImplemented()

    def pg_dump_json(self, **kwargs):
        raise exceptions.FunctionNotImplemented()

    def pg_dump_pools_json(self, **kwargs):
        raise exceptions.FunctionNotImplemented()

    def pg_dump_stuck(self, **kwargs):
        raise exceptions.FunctionNotImplemented()

    def pg_getmap(self, **kwargs):
        # Could not get this to work yet
        raise exceptions.FunctionNotImplemented()

    def pg_map(self, **kwargs):
        # Could not get this to work yet
        raise exceptions.FunctionNotImplemented()

    def pg_stat(self, **kwargs):
        return self.get('pg/stat', **kwargs)