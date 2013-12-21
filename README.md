python-cephclient
=================

A client library in python for the Ceph REST API.

This is currently a work in progress.

USAGE
=================

    client = CephClient(
        debug = True,
        endpoint = 'http://apiserver:5000/api/v0.1/',
    )

    response, body = client.get(client.urls('fsid'), body = True)
    print(json.dumps(body, indent=4, separators=(',', ': ')))

    #####

    Dec 21 16:51:46 - client.py - DEBUG - Params: {'debug': True, 'endpoint': 'http://apiserver:5000/api/v0.1/'}
    Dec 21 16:51:46 - client.py - DEBUG - Requesting URL: http://apiserver:5000/api/v0.1/fsid - {'headers': {'Content-Type': 'application/json', 'Accept': 'application/json', 'User-Agent': 'python-cephclient'}, 'data': 'true'}
    {
        "status": "OK",
        "output": {
            "fsid": "d5252e7d-75bc-4083-85ed-fe51fa83f62b"
        }
    }