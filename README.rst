python-cephclient is a python module to communicate with `Ceph's REST API`_ (``ceph-rest-api``).

.. _Ceph's REST API: http://ceph.com/docs/master/man/8/ceph-rest-api/

This is currently a work in progress.

ABOUT
==================================================

Client
--------------------------------------------------

The cephclient class takes care of sending calls to the API through HTTP and
handle the responses. It supports queries for JSON, XML or plain text.

Wrapper
--------------------------------------------------

The wrapper class extends the client and provides helper functions to
communicate with the API.

Nothing prevents you from calling the client directly exactly like the wrapper
does.
The wrapper exists for convenience.

Development, Feedback, Bugs
--------------------------------------------------

Want to contribute ? Feel free to send pull requests !

Have problems, bugs, feature ideas ?
I am using the github `issue tracker`_ to manage them.

.. _issue tracker: https://github.com/dmsimard/python-cephclient/issues


HOW TO USE
==================================================

Installation
----------------
Install the package through pip::

    pip install python-cephclient


Instanciate CephWrapper::

    from cephclient import *

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