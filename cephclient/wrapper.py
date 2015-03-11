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
#   Authors: David Moreau Simard <moi@dmsimard.com>
#            Donald Talton <donald@thoughtstorm.net>
#

import cephclient.client as client
import cephclient.exceptions as exceptions


class CephWrapper(client.CephClient):
    def __init__(self, **params):
        super(CephWrapper, self).__init__(**params)
        self.user_agent = 'python-cephclient-wrapper'

    ###
    # root GET calls
    ###
    def df(self, detail=None, **kwargs):
        if detail is not None:
            return self.get('df?detail={0}'
                            .format(detail), **kwargs)
        else:
            return self.get('df', **kwargs)

    def fsid(self, **kwargs):
        return self.get('fsid', **kwargs)

    def health(self, detail=None, **kwargs):
        if detail is not None:
            return self.get('health?detail={0}'
                            .format(detail), **kwargs)
        else:
            return self.get('health', **kwargs)

    def quorum_status(self, **kwargs):
        return self.get('quorum_status', **kwargs)

    def report(self, tags=None, **kwargs):
        if tags is not None:
            return self.get('report?tags={0}'
                            .format(tags), **kwargs)
        else:
            return self.get('report', **kwargs)

    def status(self, **kwargs):
        return self.get('status', **kwargs)

    ###
    # root PUT calls
    ###
    def compact(self, **kwargs):
        return self.put('compact', **kwargs)

    def heap(self, heapcmd, **kwargs):
        return self.put('heap?heapcmd={0}'
                        .format(heapcmd), **kwargs)

    def injectargs(self, injected_args, **kwargs):
        return self.put('injectargs?injected_args={0}'
                        .format(injected_args), **kwargs)

    def log(self, logtext, **kwargs):
        return self.put('log?logtext={0}'
                        .format(logtext), **kwargs)

    def quorum(self, quorumcmd, **kwargs):
        return self.put('quorum?quorumcmd={0}'
                        .format(quorumcmd), **kwargs)

    def scrub(self, **kwargs):
        return self.put('scrub', **kwargs)

    def tell(self, target, args, **kwargs):
        return self.put('tell?target={0}&args={1}'
                        .format(target, args), **kwargs)

    ###
    # auth GET calls
    ###
    def auth_export(self, entity=None, **kwargs):
        if entity is not None:
            return self.get('auth/export?entity={0}'
                            .format(entity), **kwargs)
        else:
            return self.get('auth/export', **kwargs)

    def auth_get(self, entity, **kwargs):
        return self.get('auth/get?entity={0}'
                        .format(entity), **kwargs)

    def auth_get_key(self, entity, **kwargs):
        return self.get('auth/get-key?entity={0}'
                        .format(entity), **kwargs)

    def auth_list(self, **kwargs):
        return self.get('auth/list', **kwargs)

    def auth_print_key(self, entity, **kwargs):
        return self.get('auth/print-key?entity={0}'
                        .format(entity), **kwargs)

    ###
    # auth PUT calls
    ###
    """
    caps dictionary format:
    caps = {
        'mon': 'allow rwx',
        'osd': 'allow *',
        ...
    }
    """
    def auth_add(self, entity, caps={}, file=None, **kwargs):
        # XXX-TODO: Implement file input
        full_caps = list()
        if caps:
            for key in caps:
                permissions = caps[key].replace(' ', '+')
                full_caps.append('&caps={0}&caps={1}'
                                 .format(key, permissions))

        return self.put('auth/add?entity={0}{1}'
                        .format(entity, ''.join(full_caps)), **kwargs)

    def auth_caps(self, entity, caps={}, **kwargs):
        full_caps = list()
        if caps:
            for key in caps:
                permissions = caps[key].replace(' ', '+')
                full_caps.append('&caps={0}&caps={1}'
                                 .format(key, permissions))

        return self.put('auth/caps?entity={0}{1}'
                        .format(entity, ''.join(full_caps)), **kwargs)

    def auth_del(self, entity, **kwargs):
        return self.put('auth/del?entity={0}'
                        .format(entity), **kwargs)

    def auth_get_or_create(self, entity, caps={}, file=None, **kwargs):
        # XXX-TODO: Implement file input
        full_caps = list()
        if caps:
            for key in caps:
                permissions = caps[key].replace(' ', '+')
                full_caps.append('&caps={0}&caps={1}'.format(key, permissions))

        return self.put('auth/get-or-create?entity={0}{1}'
                        .format(entity, ''.join(full_caps)), **kwargs)

    def auth_get_or_create_key(self, entity, caps={}, **kwargs):
        # XXX-TODO: Implement file input
        full_caps = list()
        if caps:
            for key in caps:
                permissions = caps[key].replace(' ', '+')
                full_caps.append('&caps={0}&caps={1}'.format(key, permissions))

        return self.put('auth/get-or-create-key?entity={0}{1}'
                        .format(entity, ''.join(full_caps)), **kwargs)

    def auth_import(self, file):
        # XXX-TODO: Implement file input
        raise exceptions.FunctionNotImplemented()

    ###
    # config-key GET calls
    ###
    def config_key_exists(self, key, **kwargs):
        return self.get('config-key/exists?key={0}'
                        .format(key), **kwargs)

    def config_key_get(self, key, **kwargs):
        return self.get('config-key/get?key={0}'
                        .format(key), **kwargs)

    def config_key_list(self, **kwargs):
        return self.get('config-key/list', **kwargs)

    ###
    # mds GET calls
    ###
    def mds_compat_show(self, **kwargs):
        return self.get('mds/compat/show', **kwargs)

    def mds_dump(self, epoch=None, **kwargs):
        if epoch is not None:
            return self.get('mds/dump?epoch={0}'
                            .format(epoch), **kwargs)
        else:
            return self.get('mds/dump', **kwargs)

    def mds_getmap(self, epoch=None, **kwargs):
        kwargs['supported_body_types'] = ['binary']

        if epoch is not None:
            return self.get('mds/getmap?epoch={0}'
                            .format(epoch), **kwargs)
        else:
            return self.get('mds/getmap', **kwargs)

    def mds_stat(self, **kwargs):
        return self.get('mds/stat', **kwargs)

    ###
    # mds PUT calls
    ###
    def mds_add_data_pool(self, pool, **kwargs):
        return self.put('mds/add_data_pool?pool={0}'
                        .format(pool), **kwargs)

    def mds_cluster_down(self, **kwargs):
        return self.put('mds/cluster_down', **kwargs)

    def mds_cluster_up(self, **kwargs):
        return self.put('mds/cluster_up', **kwargs)

    def mds_compat_rm_compat(self, feature, **kwargs):
        return self.put('mds/compat/rm_compat?feature={0}'
                        .format(feature), **kwargs)

    def mds_compat_rm_incompat(self, feature, **kwargs):
        return self.put('mds/compat/rm_incompat?feature={0}'
                        .format(feature), **kwargs)

    def mds_deactivate(self, who, **kwargs):
        return self.put('mds/deactivate?who={0}'
                        .format(who), **kwargs)

    def mds_fail(self, who, **kwargs):
        return self.put('mds/fail?who={0}'
                        .format(who), **kwargs)

    def mds_newfs(self, metadata, data, sure, **kwargs):
        return self.put('mds/newfs?metadata={0}&data={1}&sure={2}'
                        .format(metadata, data, sure), **kwargs)

    def mds_remove_data_pool(self, pool, **kwargs):
        return self.put('mds/remove_data_pool?pool={0}'
                        .format(pool), **kwargs)

    def mds_rm(self, gid, who, **kwargs):
        return self.put('mds/rm?gid={0}&who={1}'
                        .format(gid, who), **kwargs)

    def mds_rmfailed(self, who, **kwargs):
        return self.put('mds/rmfailed?who={0}'
                        .format(who), **kwargs)

    def mds_set_allow_new_snaps(self, sure, **kwargs):
        """
        mds/set?key=allow_new_snaps&sure=
        """
        raise exceptions.FunctionNotImplemented()

    def mds_set_max_mds(self, maxmds, **kwargs):
        return self.put('mds/set_max_mds?maxmds={0}'
                        .format(maxmds), **kwargs)

    def mds_setmap(self, epoch, **kwargs):
        return self.put('mds/setmap?epoch={0}'
                        .format(epoch), **kwargs)

    def mds_stop(self, who, **kwargs):
        return self.put('mds/stop?who={0}'
                        .format(who), **kwargs)

    def mds_tell(self, who, args, **kwargs):
        return self.put('mds/tell?who={0}&args={1}'
                        .format(who, args), **kwargs)

    def mds_unset_allow_new_snaps(self, sure, **kwargs):
        """
        mds/unset?key=allow_new_snaps&sure=
        """
        raise exceptions.FunctionNotImplemented()

    ###
    # mon GET calls
    ###
    def mon_dump(self, epoch=None, **kwargs):
        if epoch is not None:
            return self.get('mon/dump?epoch={0}'
                            .format(epoch), **kwargs)
        else:
            return self.get('mon/dump', **kwargs)

    def mon_getmap(self, epoch=None, **kwargs):
        kwargs['supported_body_types'] = ['binary']

        if epoch is not None:
            return self.get('mon/getmap?epoch={0}'
                            .format(epoch), **kwargs)
        else:
            return self.get('mon/getmap', **kwargs)

    def mon_stat(self, **kwargs):
        kwargs['supported_body_types'] = ['text', 'xml']

        return self.get('mon/stat', **kwargs)

    def mon_status(self, **kwargs):
        return self.get('mon_status', **kwargs)

    ###
    # mon PUT calls
    ###
    def mon_add(self, name, addr, **kwargs):
        return self.put('mon/add?name={0}&addr={1}'
                        .format(name, addr), **kwargs)

    def mon_remove(self, name, **kwargs):
        return self.put('mon/remove?name={0}'
                        .format(name), **kwargs)

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

    def osd_dump(self, epoch=None, **kwargs):
        if epoch is not None:
            return self.get('osd/dump?epoch={0}'
                            .format(epoch), **kwargs)
        else:
            return self.get('osd/dump', **kwargs)

    def osd_find(self, id, **kwargs):
        return self.get('osd/find?id={0}'
                        .format(id), **kwargs)

    def osd_getcrushmap(self, epoch=None, **kwargs):
        kwargs['supported_body_types'] = ['binary']

        if epoch is not None:
            return self.get('osd/getcrushmap?epoch={0}'
                            .format(epoch), **kwargs)
        else:
            return self.get('osd/getcrushmap', **kwargs)

    def osd_getmap(self, epoch=None, **kwargs):
        kwargs['supported_body_types'] = ['binary']

        if epoch is not None:
            return self.get('osd/getmap?epoch={0}'
                            .format(epoch), **kwargs)
        else:
            return self.get('osd/getmap', **kwargs)

    def osd_getmaxosd(self, **kwargs):
        return self.get('osd/getmaxosd', **kwargs)

    def osd_ls(self, epoch=None, **kwargs):
        if epoch is not None:
            return self.get('osd/ls?epoch={0}'
                            .format(epoch), **kwargs)
        else:
            return self.get('osd/ls', **kwargs)

    def osd_lspools(self, auid=None, **kwargs):
        if auid is not None:
            return self.get('osd/lspools?auid={0}'
                            .format(auid), **kwargs)
        else:
            return self.get('osd/lspools', **kwargs)

    def osd_map(self, pool, object, **kwargs):
        return self.get('osd/map?pool={0}&object={1}'
                        .format(pool, object), **kwargs)

    def osd_perf(self, **kwargs):
        return self.get('osd/perf', **kwargs)

    def osd_pool_get(self, pool, var, **kwargs):
        return self.get('osd/pool/get?pool={0}&var={1}'
                        .format(pool, var), **kwargs)

    def osd_pool_stats(self, name=None, **kwargs):
        if name is not None:
            return self.get('osd/pool/stats?name={0}'
                            .format(name), **kwargs)
        else:
            return self.get('osd/pool/stats', **kwargs)

    def osd_stat(self, **kwargs):
        return self.get('osd/stat', **kwargs)

    def osd_tree(self, epoch=None, **kwargs):
        if epoch is not None:
            return self.get('osd/tree?epoch={0}'
                            .format(epoch), **kwargs)
        else:
            return self.get('osd/tree', **kwargs)

    ###
    # osd PUT calls
    ###
    def osd_blacklist(self, blacklistop, addr, expire, **kwargs):
        return self.put('osd/blacklist?blacklistop={0}&addr={1}&expire={2}'
                        .format(blacklistop, addr, expire), **kwargs)

    def osd_create(self, uuid, **kwargs):
        return self.put('osd/create?uuid={0}'
                        .format(uuid), **kwargs)

    def osd_crush_add(self, id, weight, args, **kwargs):
        return self.put('osd/crush/add?id={0}&weight={1}&args={2}'
                        .format(id, weight, args), **kwargs)

    def osd_crush_add_bucket(self, name, type, **kwargs):
        return self.put('osd/crush/add-bucket?name={0}&type={1}'
                        .format(name, type), **kwargs)

    def osd_crush_create_or_move(self, id, weight, args, **kwargs):
        return self.put('osd/crush/create-or-move?id={0}&weight={1}&args={2}'
                        .format(id, weight, args), **kwargs)

    def osd_crush_link(self, name, args, **kwargs):
        return self.put('osd/crush/link?name={0}&args={2}'
                        .format(name, args), **kwargs)

    def osd_crush_move(self, name, args, **kwargs):
        return self.put('osd/crush/move?name={0}&args={1}'
                        .format(name, args), **kwargs)

    def osd_crush_remove(self, name, ancestor, **kwargs):
        return self.put('osd/crush/remove?name={0}&ancestor={1}'
                        .format(name, ancestor), **kwargs)

    def osd_crush_reweight(self, name, weight, **kwargs):
        return self.put('osd/crush/reweight?name={0}&weight={1}'
                        .format(name, weight), **kwargs)

    def osd_crush_rm(self, name, ancestor, **kwargs):
        return self.put('osd/crush/rm?name={0}&ancestor={1}'
                        .format(name, ancestor), **kwargs)

    def osd_crush_rule_create_simple(self, name, root, type, **kwargs):
        return self.put(
            'osd/crush/rule/create-simple?name={0}&root={1}&type={2}'
            .format(name, root, type), **kwargs)

    def osd_crush_rule_rm(self, name, **kwargs):
        return self.put('osd/crush/rule/rm?name={0}'
                        .format(name), **kwargs)

    def osd_crush_set(self, id, name, weight, args, **kwargs):
        return self.put('osd/crush/set?id={0}&weight={1}&args={2}'
                        .format(id, name, weight, args), **kwargs)

    def osd_crush_tunables(self, profile, **kwargs):
        return self.put('osd/crush/tunables?profile={0}'
                        .format(profile), **kwargs)

    def osd_crush_unlink(self, name, ancestor, **kwargs):
        return self.put('osd/crush/unlink?name={0}&ancestor={1}'
                        .format(name, ancestor), **kwargs)

    def osd_deep_scrub(self, who, **kwargs):
        return self.put('osd/deep-scrub?who={0}'
                        .format(who), **kwargs)

    def osd_down(self, ids, **kwargs):
        return self.put('osd/down?ids={0}'
                        .format(ids), **kwargs)

    def osd_in(self, ids, **kwargs):
        return self.put('osd/in?ids={0}'
                        .format(ids), **kwargs)

    def osd_lost(self, id, sure, **kwargs):
        return self.put('osd/lost?id={0}&sure={1}'
                        .format(id, sure), **kwargs)

    def osd_out(self, ids, **kwargs):
        return self.put('osd/out?ids={0}'
                        .format(ids), **kwargs)

    def osd_pool_create(self, pool, pg_num, pgp_num, properties, **kwargs):
        return self.put(
            'osd/pool/create?pool={0}&pg_num={1}&pgp_num={2}&properties={3}'
            .format(pool, pg_num, pgp_num, properties), **kwargs)

    def osd_pool_delete(self, pool, sure, **kwargs):
        return self.put('osd/pool/delete?pool={0}&sure={1}'
                        .format(pool, sure), **kwargs)

    def osd_pool_param(self, pool, var, **kwargs):
        return self.put('osd/pool/get?pool={0}&var={1}'
                        .format(pool, var), **kwargs)

    def osd_pool_mksnap(self, pool, snap, **kwargs):
        return self.put('osd/pool/mksnap?pool={0}&snap={1}'
                        .format(pool, snap), **kwargs)

    def osd_pool_rename(self, srcpool, destpool, **kwargs):
        return self.put('osd/pool/rename?srcpool={0}&destpool={1}'
                        .format(srcpool, destpool), **kwargs)

    def osd_pool_rmsnap(self, pool, snap, **kwargs):
        return self.put('osd/pool/rmsnap?pool={0}&snap={1}'
                        .format(pool, snap), **kwargs)

    def osd_set_pool_param(self, pool, var, **kwargs):
        return self.put('osd/pool/set?pool={0}&var={1}'
                        .format(pool, var), **kwargs)

    def osd_set_pool_quota(self, pool, field, **kwargs):
        return self.put('osd/pool/set-quota?pool={0}&field={1}'
                        .format(pool, field), **kwargs)

    def osd_repair(self, pool, who, **kwargs):
        return self.put('osd/repair?who={0}'
                        .format(pool, who), **kwargs)

    def osd_reweight(self, id, weight, **kwargs):
        return self.put('osd/reweight?id={0}&weight={1}'
                        .format(id, weight), **kwargs)

    def osd_reweight_by_utilization(self, oload, **kwargs):
        return self.put('osd/reweight-by-utilization?oload={0}'
                        .format(oload), **kwargs)

    def osd_remove(self, ids, **kwargs):
        return self.put('osd/rm?ids={0}'
                        .format(ids), **kwargs)

    def osd_scrub(self, who, **kwargs):
        return self.put('osd/scrub?who={0}'
                        .format(who), **kwargs)

    def osd_set_key(self, key, **kwargs):
        return self.put('osd/set?key={0}'
                        .format(key), **kwargs)

    def osd_setmaxosd(self, newmax, **kwargs):
        return self.put('osd/setmaxosd?newmax={0}'
                        .format(newmax), **kwargs)

    def osd_thrash(self, num_epochs, **kwargs):
        return self.put('osd/thrash?num_epochs={0}'
                        .format(num_epochs), **kwargs)

    def osd_tier_add(self, pool, tierpool, **kwargs):
        return self.put('osd/tier/add?pool={0}&tierpool={1}'
                        .format(pool, tierpool), **kwargs)

    def osd_tier_cachemode(self, pool, mode, **kwargs):
        return self.put('osd/tier/cache-mode?pool={0}&mode={1}'
                        .format(pool, mode), **kwargs)

    def osd_tier_remove(self, pool, tierpool, **kwargs):
        return self.put('osd/tier/remove?pool={0}&tierpool={1}'
                        .format(pool, tierpool), **kwargs)

    def osd_tier_remove_overlay(self, pool, **kwargs):
        return self.put('osd/tier/remove-overlay?pool={0}'
                        .format(pool), **kwargs)

    def osd_tier_set_overlay(self, pool, overlaypool, **kwargs):
        return self.put('osd/tier/set-overlay?pool={0}&overlaypool={1}'
                        .format(pool, overlaypool), **kwargs)

    def osd_unset(self, key, **kwargs):
        return self.put('osd/unset?key={0}'
                        .format(key), **kwargs)

    ###
    # pg GET calls
    ###
    def pg_debug(self, debugop, **kwargs):
        kwargs['supported_body_types'] = ['text', 'xml']

        return self.get('pg/debug?debugop={0}'
                        .format(debugop), **kwargs)

    def pg_dump(self, dumpcontents=None, **kwargs):
        if dumpcontents is not None:
            return self.get('pg/dump?dumpcontents={0}'
                            .format(dumpcontents), **kwargs)
        else:
            return self.get('pg/dump', **kwargs)

    def pg_dump_json(self, dumpcontents=None, **kwargs):
        if dumpcontents is not None:
            return self.get('pg/dump_json?dumpcontents={0}'
                            .format(dumpcontents), **kwargs)
        else:
            return self.get('pg/dump_json', **kwargs)

    def pg_dump_pools_json(self, **kwargs):
        return self.get('pg/dump_pools_json', **kwargs)

    def pg_dump_stuck(self, stuckops=None, **kwargs):
        if stuckops is not None:
            return self.get('pg/dump_stuck?stuckops={0}'
                            .format(stuckops), **kwargs)
        else:
            return self.get('pg/dump_stuck', **kwargs)

    def pg_getmap(self, **kwargs):
        kwargs['supported_body_types'] = ['binary']

        return self.get('pg/getmap', **kwargs)

    def pg_map(self, pgid, **kwargs):
        return self.get('pg/map?pgid={0}'
                        .format(pgid), **kwargs)

    def pg_stat(self, **kwargs):
        return self.get('pg/stat', **kwargs)

    ###
    # tell GET calls
    ###
    def tell_debug_dump_missing(self, id, filename, **kwargs):
        return self.get('tell/{0}/debug_dump_missing?filename={1}'
                        .format(id, filename), **kwargs)

    def tell_dump_pg_recovery_stats(self, id, **kwargs):
        return self.get('tell/{0}/dump_pg_recovery_stats'
                        .format(id), **kwargs)

    def tell_list_missing(self, id, offset, **kwargs):
        return self.get('tell/{0}/list_missing?offset={1}'
                        .format(id, offset), **kwargs)

    def tell_query(self, id, **kwargs):
        return self.get('tell/{0}/query'
                        .format(id), **kwargs)

    def tell_version(self, id, **kwargs):
        return self.get('tell/{0}/version'
                        .format(id), **kwargs)
