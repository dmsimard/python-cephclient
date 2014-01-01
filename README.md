python-cephclient
=================

A client library in python for the Ceph REST API.

This is currently a work in progress.

TODO
=================

- Finish the GET methods
- Implement POST, PUT and DELETE methods
- Support plain text, XML AND JSON responses
- Documentation

CLIENT USAGE
=================

The client takes care of sending calls to the API through HTTP and handle the
response.

    client = CephClient(
        endpoint = 'http://apiserver:5000/api/v0.1/',
    )

    response, body = client.get('fsid', body = True)
    print(json.dumps(body, indent=4, separators=(',', ': ')))

    ====

    {
        "status": "OK",
        "output": {
            "fsid": "d5252e7d-75bc-4083-85ed-fe51fa83f62b"
        }
    }

WRAPPER USAGE
=================

The wrapper extends the client and provides helper functions to communicate with
the API.

    wrapper = CephWrapper(
        endpoint = 'http://apiserver:5000/api/v0.1/',
    )

    response, body = wrapper.get_fsid(body = True)
    print(json.dumps(body, indent=4, separators=(',', ': ')))

    ====

    {
        "status": "OK",
        "output": {
            "fsid": "d5252e7d-75bc-4083-85ed-fe51fa83f62b"
        }
    }