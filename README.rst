python-cephclient
==================================================

A client library in python for the Ceph REST API (``ceph-rest-api``).

This is currently a work in progress.

INSTALL
==================================================
Install the package through pip:::

    pip install python-cephclient


ABOUT
==================================================

Client
----------------

The client takes care of sending calls to the API through HTTP and handle the
responses.

Wrapper
----------------

The wrapper extends the client and provides helper functions to communicate with
the API.

HOW TO USE
==================================================

Instanciate CephWrapper::

    wrapper = CephWrapper(
        endpoint = 'http://apiserver:5000/api/v0.1/',
        debug = True # Optionally increases the verbosity of the client
    )

Do your request and specify the reponse type you are expecting.

Either ``json``, ``xml`` or ``text`` (default) are available.

text::

    response, body = wrapper.get_fsid(body = 'text')
    print(response)

    ====

    d5252e7d-75bc-4083-85ed-fe51fa83f62b


json::

    response, body = wrapper.get_fsid(body = 'json')
    print(json.dumps(body, indent=4, separators=(',', ': ')))

    ====

    {
        "status": "OK",
        "output": {
            "fsid": "d5252e7d-75bc-4083-85ed-fe51fa83f62b"
        }
    }


xml::

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

TODO
==================================================

- Finish the GET methods
- Implement PUT (write) methods
- Documentation