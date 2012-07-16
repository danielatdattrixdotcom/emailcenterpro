from hashlib import sha1
import hmac
import binascii
from time import strftime, gmtime
from urllib import urlencode
import urllib2
import json
from urllib2 import HTTPError

# This is the sole function that should be imported. It returns the EmailCenterPro object which will configure itself
def ecp_connect(key, secret, url):
    return EmailCenterPro(key, secret, url)


class EmailCenterPro(object):
    def __init__(self, key, secret, url):
        self._key = key
        self._secret = secret
        self._url = url

        self.clear()

        self.folder = folder(self)
        self.metrics = metrics(self)

    def makeRequest(self, content):
        #TODO Make this use a list and support the nested actions
        api_action = '/%s/%s' % (self._object, '/'.join(self._action))
        arguments = self._args
        arguments.update(content)

        content = urlencode(arguments)
        date = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        body = '\n'.join(['POST', api_action, content, date])
        headers = {'Authorization': 'ECP ' + self._key + ':' +
                                    binascii.b2a_base64(hmac.new(self._secret, body, sha1).digest())[:-1], 'Date': date}
        action_url = self._url + api_action
        request = urllib2.Request(action_url, content, headers=headers)
        try:
            response = urllib2.urlopen(request)
            self._data = response.read()
        except HTTPError as e:
            self._data = urllib2.urlopen(e.filename).read()

    def clear(self):
        self._object = None
        self._action = []
        self._args = {}
        self._data = None

    def read(self):
        return self._data


# On methods where the end result is a reply from the API we enforce it with a decorator
def request_action(action_method):
    def wrapper(self, *args, **kwargs):
        return action_method(self, *args, **kwargs)._request(action_method.__name__.split('_'), **kwargs)
    return wrapper

# This object is the base for all objects. Anything that applies to all objects lives here
class CoreEcpObject(object):
    def __init__(self, connection):
        self.connection = connection
        self.connection._object = self.__class__.__name__

    def _request(self, action, **kwargs):
        self.connection._action = action
        self.connection.makeRequest(kwargs)
        return json.load(self.connection)

# Some actions are simple very common and actions that need the the basics should use this
class CommonEcpObject(CoreEcpObject):
    @request_action
    def list(self, **kwargs):
        return self

class folder(CommonEcpObject):
    pass

class metrics(CoreEcpObject):

    @request_action
    def mailbox_traffic(self, **kwargs):
        return self

    @request_action
    def mailbox_responsetime(self, **kwargs):
        return self

    @request_action
    def mailbox_breakdown(self, **kwargs):
        return self

    @request_action
    def mailbox_trafficdistribution(self, **kwargs):
        return self

    @request_action
    def mailbox_useractivity(self, **kwargs):
        return self

    @request_action
    def usersonline(self, **kwargs):
        return self
