python-cephclient
=================

A client library in python for the Ceph REST API.

This is currently a work in progress.

TODO
=================

- Finish the GET methods
- Implement POST, PUT and DELETE methods
- Publish on pypi
- ~~Support plain text, XML AND JSON responses~~
- Add CLI support ?
- Documentation

CLIENT
=================

The client takes care of sending calls to the API through HTTP and handle the
responses.

WRAPPER
=================

The wrapper extends the client and provides helper functions to communicate with
the API.

HOW TO USE
=================

Instanciate CephWrapper:

    wrapper = CephWrapper(
        endpoint = 'http://apiserver:5000/api/v0.1/',
        debug = True # Optionally increases the verbosity of the client
    )

Do your request and specify the reponse type you are expecting.

Either 'json', 'xml' or 'text' (default) are available.

__text__

    response, body = wrapper.get_fsid(body = 'text')
    print(response)

    ====

    d5252e7d-75bc-4083-85ed-fe51fa83f62b


__json__

    response, body = wrapper.get_fsid(body = 'json')
    print(json.dumps(body, indent=4, separators=(',', ': ')))

    ====

    {
        "status": "OK",
        "output": {
            "fsid": "d5252e7d-75bc-4083-85ed-fe51fa83f62b"
        }
    }


__xml__

    response, body = wrapper.get_fsid(body = 'xml')
    print(etree.tostring(body, pretty_print=True))

    ====

    <response>
      <output>
        <fsid><fsid>d5252e7d-75bc-4083-85ed-fe51fa83f62b</fsid></fsid>
      </output>
      <status>
        OK
      </status>
    </response>