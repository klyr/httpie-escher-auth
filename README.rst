httpie-escher-auth
==================

This is a plugin for Escher authentication for HTTPie.

Installation
------------

.. code-block:: bash

    $ pip install https://github.com/klyr/httpie-escher-auth/releases/download/0.1.0/httpie_escher_auth-0.1.0-py3-none-any.whl

Example usage
-------------

.. code-block:: bash

    $ http --auth-type=escher \
           --auth='global/internalservices/scn_request/378aebee-cbd7-4bf5-80ce-1e7d1dfc7e0e:cG91ZXQtcHJvdXQK' \
           https://something.test/api/users
