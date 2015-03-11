python-cephclient is a python module to communicate with `Ceph's REST API`_ (``ceph-rest-api``).

.. _Ceph's REST API: http://ceph.com/docs/master/man/8/ceph-rest-api/

This is currently a work in progress.

ABOUT
==================================================

Client
--------------------------------------------------

The cephclient class takes care of sending calls to the API through HTTP and
handle the responses. It supports queries for JSON, XML, plain text or binary.

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

Installation does not work ?

python-cephclient depends on lxml which itself
depends on some packages. To install lxml's dependencies on Ubuntu::

    apt-get install python-dev libxml2-dev libxslt-dev


Instanciate CephWrapper::

    from cephclient.wrapper import *

    wrapper = CephWrapper(
        endpoint = 'http://apiserver:5000/api/v0.1/',
        debug = True # Optionally increases the verbosity of the client
    )

Do your request and specify the reponse type you are expecting.

Either ``json``, ``xml``, ``text`` (default) or ``binary`` are available.

json::

    response, body = wrapper.get_fsid(body = 'json')
    print('Response: {0}, Body:\n{1}'.format(response, json.dumps(body, indent=4, separators=(',', ': '))))

    ====

    Response: <Response [200]>, Body:
    {
        "status": "OK",
        "output": {
            "fsid": "d5252e7d-75bc-4083-85ed-fe51fa83f62b"
        }
    }


xml::

    response, body = wrapper.get_fsid(body = 'xml')
    print('Response: {0}, Body:\n{1}'.format(reponse, etree.tostring(body, pretty_print=True)))

    ====

    Response: <Response [200]>, Body:
    <response>
      <output>
        <fsid><fsid>d5252e7d-75bc-4083-85ed-fe51fa83f62b</fsid></fsid>
      </output>
      <status>
        OK
      </status>
    </response>



text::

    response, body = wrapper.get_fsid(body = 'text')
    print('Response: {0}, Body:\n{1}'.format(response, body))

    ====

    Response: <Response [200]>, Body:
    d5252e7d-75bc-4083-85ed-fe51fa83f62b

binary::

    response, body = wrapper.mon_getmap(body = 'binary')
    # < Do something binary with 'body' >


RELEASE NOTES
==================================================
**0.1.0.5**

dmsimard:
- Add missing dependency on the requests library
- Some PEP8 and code standardization cleanup
- Add root "PUT" methods
- Add mon "PUT" methods
- Add mds "PUT" methods
- Add auth "PUT" methods

Donald Talton:
- Add osd "PUT" methods

**0.1.0.4**

- Fix setup and PyPi installation

**0.1.0.3**

- GET API calls under '/tell' have been implemented.
- GET API calls are are in root (/) have been renamed to be coherent with incoming future development

**0.1.0.2**

- Implemented or fixed missing GET calls (All API GET calls that are not under the '/tell' namespace are now supported)
- Client can optionally raise an exception when requesting a unsupported body type for a provided API call (ex: requesting json through the wrapper for a call that is known to only return binary will raise an exception)
- Client now supports binary type responses (ex: crush map, mon map, etc)
- Improved the README (!)


**0.1.0.1**

- First public release of python-cephclient
