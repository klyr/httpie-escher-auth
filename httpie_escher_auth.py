"""
Escher auth plugin for HTTPie.
"""
from urllib.parse import urlparse
from httpie.plugins import AuthPlugin

from escherauth.escherauth import EscherRequestsAuth

__version__ = '0.2.0'
__author__ = 'Julien Barbot'
__license__ = 'Cisco'


class EscherAuthRequestWrapper(object):
    def __init__(self, scope, options, escher_client):
        self._e = EscherRequestsAuth(scope, options, escher_client)

    def __call__(self, r):
        parsed_uri = urlparse(r.url)
        r.headers['Host'] = parsed_uri.netloc

        return self._e(r)


class EscherAuthPlugin(AuthPlugin):
    name = 'Escher auth'
    auth_type = 'escher'
    description = 'Set the right format for Escher auth request'
    auth_require = False
    prompt_password = False

    def get_auth(self, username=None, password=None):
        if "/" in username:
            scope = username.split("/")
            escher_key = scope.pop()
            scope = "/".join(scope)

        escher_client = {'api_key': escher_key, 'api_secret': password}

        options = {}
        return EscherAuthRequestWrapper(scope, options, escher_client)
