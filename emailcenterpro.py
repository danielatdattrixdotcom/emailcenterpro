from hashlib import sha1
import hmac
import binascii
from time import strftime, gmtime
from urllib import urlencode
import urllib2
import json
from urllib2 import HTTPError

# This is the sole function that should be imported. It returns the EmailCenterPro object which will configure itself
def ecp_connect(key, secret, url, **kwargs):
    return EmailCenterPro(key, secret, url, **kwargs)


class EmailCenterPro(object):
    def __init__(self, key, secret, url, **kwargs):
        self._key = key
        self._secret = secret
        self._url = url

        self._args = {}
        for k, v in kwargs.items():
            self._args[k] = v

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

    def clear(self, clear_args=None):
        """
        Clears last object, action and held return data.
        With first parameter being not None it clears the set arguments as well.
        """
        if clear_args is not None:
            self._args = {}

        self._object = None
        self._action = []
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


class account(CoreEcpObject):
    @request_action
    def account(self, **kwargs):
        return self

    @request_action
    def update(self, **kwargs):
        return self

    @request_action
    def cancel(self, **kwargs):
        return self

    @request_action
    def stats(self, **kwargs):
        return self

    @request_action
    def changeLevel(self, **kwargs):
        return self


class attachment(CoreEcpObject):
    @request_action
    def attachment(self, **kwargs):
        return self

    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def download(self, **kwargs):
        return self

    @request_action
    def preview(self, **kwargs):
        return self

    @request_action
    def view(self, **kwargs):
        return self


class call(CoreEcpObject):
    @request_action
    def add(self, **kwargs):
        return self

    @request_action
    def delete(self, **kwargs):
        return self

    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def call(self, **kwargs):
        return self


class chat(CoreEcpObject):
    @request_action
    def add(self, **kwargs):
        return self

    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def chat(self, **kwargs):
        return self


class contact(CoreEcpObject):
    @request_action
    def contact(self, **kwargs):
        return self

    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def complete(self, **kwargs):
        return self

    @request_action
    def add(self, **kwargs):
        return self

    @request_action
    def delete(self, **kwargs):
        return self

    @request_action
    def update(self, **kwargs):
        return self


class conversation(CoreEcpObject):
    @request_action
    def conversation(self, **kwargs):
        return self

    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def assign(self, **kwargs):
        return self

    @request_action
    def move(self, **kwargs):
        return self

    @request_action
    def mark(self, **kwargs):
        return self

    @request_action
    def lock(self, **kwargs):
        return self

    @request_action
    def unlock(self, **kwargs):
        return self

    @request_action
    def star(self, **kwargs):
        return self

    @request_action
    def unstar(self, **kwargs):
        return self

    @request_action
    def ticket(self, **kwargs):
        return self

    @request_action
    def message_respond(self, **kwargs):
        return self

    @request_action
    def purge(self, **kwargs):
        return self


class folder(CoreEcpObject):
    @request_action
    def list(self, **kwargs):
        return self


class history(CoreEcpObject):
    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def renew(self, **kwargs):
        return self


class invoice(CoreEcpObject):
    @request_action
    def list(self, **kwargs):
        return self


class key(CoreEcpObject):
    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def issue(self, **kwargs):
        return self

    @request_action
    def revoke(self, **kwargs):
        return self


class mailbox(CoreEcpObject):
    @request_action
    def mailbox(self, **kwargs):
        return self

    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def add(self, **kwargs):
        return self

    @request_action
    def update(self, **kwargs):
        return self

    @request_action
    def delete(self, **kwargs):
        return self

    @request_action
    def verifyPop(self, **kwargs):
        return self

    @request_action
    def findPopServer(self, **kwargs):
        return self


class message(CoreEcpObject):
    @request_action
    def message(self, **kwargs):
        return self

    @request_action
    def send(self, **kwargs):
        return self

    @request_action
    def save(self, **kwargs):
        return self

    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def breakThread(self, **kwargs):
        return self

    @request_action
    def headers(self, **kwargs):
        return self

    @request_action
    def quoted(self, **kwargs):
        return self

    @request_action
    def discardDraft(self, **kwargs):
        return self

        # TODO Implement import action in a uniform manner


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


class note(CoreEcpObject):
    @request_action
    def add(self, **kwargs):
        return self

    @request_action
    def delete(self, **kwargs):
        return self

    @request_action
    def list(self, **kwargs):
        return self


class partner(CoreEcpObject):
    @request_action
    def authenticate(self, **kwargs):
        return self

    @request_action
    def revoke(self, **kwargs):
        return self


class popAccount(CoreEcpObject):
    @request_action
    def update(self, **kwargs):
        return self

    @request_action
    def verify(self, **kwargs):
        return self

    @request_action
    def findServer(self, **kwargs):
        return self

    @request_action
    def list(self, **kwargs):
        return self


class preference(CoreEcpObject):
    @request_action
    def get(self, **kwargs):
        return self

    @request_action
    def set(self, **kwargs):
        return self


class search(CoreEcpObject):
    @request_action
    def search(self, **kwargs):
        return self

    @request_action
    def get(self, **kwargs):
        return self

    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def save(self, **kwargs):
        return self

    @request_action
    def delete(self, **kwargs):
        return self


class smtpServer(CoreEcpObject):
    @request_action
    def update(self, **kwargs):
        return self

    @request_action
    def delete(self, **kwargs):
        return self

    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def verify(self, **kwargs):
        return self


class tag(CoreEcpObject):
    @request_action
    def complete(self, **kwargs):
        return self

    @request_action
    def add(self, **kwargs):
        return self

    @request_action
    def set(self, **kwargs):
        return self

    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def rename(self, **kwargs):
        return self

    @request_action
    def delete(self, **kwargs):
        return self


class template(CoreEcpObject):
    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def delete(self, **kwargs):
        return self

    @request_action
    def add(self, **kwargs):
        return self

    @request_action
    def update(self, **kwargs):
        return self

    @request_action
    def send(self, **kwargs):
        return self

    @request_action
    def template(self, **kwargs):
        return self

    @request_action
    def render(self, **kwargs):
        return self

    @request_action
    def inputFields(self, **kwargs):
        return self

    @request_action
    def renderText(self, **kwargs):
        return self


class ticket(CoreEcpObject):
    @request_action
    def ticket(self, **kwargs):
        return self


class user(CoreEcpObject):
    @request_action
    def list(self, **kwargs):
        return self

    @request_action
    def resetPassword(self, **kwargs):
        return self

    @request_action
    def resetKey(self, **kwargs):
        return self

    @request_action
    def delete(self, **kwargs):
        return self

    @request_action
    def add(self, **kwargs):
        return self

    @request_action
    def update(self, **kwargs):
        return self

    @request_action
    def user(self, **kwargs):
        return self


class utility(CoreEcpObject):
    @request_action
    def test(self, **kwargs):
        return self

    @request_action
    def context(self, **kwargs):
        return self

    @request_action
    def refreshSession(self, **kwargs):
        return self
