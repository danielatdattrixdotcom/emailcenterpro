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
    def __init__(self, auth_key, secret, url, **kwargs):
        self._key = auth_key
        self._secret = secret
        self._url = url

        self._request_method = 'POST'

        self._args = {}
        for k, v in kwargs.items():
            self._args[k] = v

        self.clear()

        self.account = account(self)
        self.attachment = attachment(self)
        self.call = call(self)
        self.chat = chat(self)
        self.contact = contact(self)
        self.conversation = conversation(self)
        self.folder = folder(self)
        self.history = history(self)
        self.invoice = invoice(self)
        self.key = key(self)
        self.mailbox = mailbox(self)
        self.message = message(self)
        self.metrics = metrics(self)
        self.note = note(self)
        self.partner = partner(self)
        self.popAccount = popAccount(self)
        self.preference = preference(self)
        self.search = search(self)
        self.smtpServer = smtpServer(self)
        self.tag = tag(self)
        self.template = template(self)
        self.ticket = ticket(self)
        self.user = user(self)
        self.utility = utility(self)

    def makeRequest(self, content):
        api_action = '/%s/%s' % (self._object, '/'.join(self._action))
        arguments = self._args
        arguments.update(content)

        content = urlencode(arguments)
        date = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        body = '\n'.join(['POST', api_action, content, date])
        headers = {'Authorization': 'ECP ' + self._key + ':' +
                                    binascii.b2a_base64(hmac.new(self._secret, body, sha1).digest())[:-1], 'Date': date}
        action_url = self._url + api_action

        try:
            if self._request_method == 'POST':
                request = urllib2.Request(action_url, content, headers=headers)
                response = urllib2.urlopen(request)
                self._data = response.read()
            else:
                request = urllib2.Request('%s?%s' % (action_url, content))
                request.add_header('Authorization', headers['Authorization'])
                self._data = urllib2.urlopen(request).read()
        except HTTPError as e:
            self._data = '{"http_error": "%s" }' % (e.code)

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
def request_action(method='POST'):
    def decorator(action_method):
        def wrapper(self, **kwargs):
            self.connection._request_method = method
            return self._request(action_method.__name__.split('_'), **kwargs)
        return wrapper
    return decorator




# This object is the base for all objects. Anything that applies to all objects lives here
class CoreEcpObject(object):
    def __init__(self, connection):
        self.connection = connection

    def _request(self, action, **kwargs):
        self.connection._object = self.__class__.__name__
        self.connection._action = action
        self.connection.makeRequest(kwargs)
        return json.load(self.connection)


class account(CoreEcpObject):
    @request_action
    def account(self, **kwargs): pass

    @request_action
    def update(self, **kwargs): pass

    @request_action
    def cancel(self, **kwargs): pass

    @request_action('GET')
    def stats(self, **kwargs): pass

    @request_action
    def changeLevel(self, **kwargs): pass


class attachment(CoreEcpObject):
    @request_action
    def attachment(self, **kwargs): pass

    @request_action
    def list(self, **kwargs): pass

    @request_action
    def download(self, **kwargs): pass

    @request_action
    def preview(self, **kwargs): pass

    @request_action
    def view(self, **kwargs): pass


class call(CoreEcpObject):
    @request_action
    def add(self, **kwargs): pass

    @request_action
    def delete(self, **kwargs): pass

    @request_action
    def list(self, **kwargs): pass

    @request_action
    def call(self, **kwargs): pass


class chat(CoreEcpObject):
    @request_action
    def add(self, **kwargs): pass

    @request_action
    def list(self, **kwargs): pass

    @request_action
    def chat(self, **kwargs): pass


class contact(CoreEcpObject):
    @request_action
    def contact(self, **kwargs): pass

    @request_action
    def list(self, **kwargs): pass

    @request_action
    def complete(self, **kwargs): pass

    @request_action
    def add(self, **kwargs): pass

    @request_action
    def delete(self, **kwargs): pass

    @request_action
    def update(self, **kwargs): pass


class conversation(CoreEcpObject):
    @request_action
    def conversation(self, **kwargs): pass

    @request_action
    def list(self, **kwargs): pass

    @request_action
    def assign(self, **kwargs): pass

    @request_action
    def move(self, **kwargs): pass

    @request_action
    def mark(self, **kwargs): pass

    @request_action
    def lock(self, **kwargs): pass

    @request_action
    def unlock(self, **kwargs): pass

    @request_action
    def star(self, **kwargs): pass

    @request_action
    def unstar(self, **kwargs): pass

    @request_action
    def ticket(self, **kwargs): pass

    @request_action
    def message_respond(self, **kwargs): pass

    @request_action
    def purge(self, **kwargs): pass


class folder(CoreEcpObject):
    @request_action
    def list(self, **kwargs): pass


class history(CoreEcpObject):
    @request_action
    def list(self, **kwargs): pass

    @request_action
    def renew(self, **kwargs): pass


class invoice(CoreEcpObject):
    @request_action
    def list(self, **kwargs): pass


class key(CoreEcpObject):
    @request_action
    def list(self, **kwargs): pass

    @request_action
    def issue(self, **kwargs): pass

    @request_action
    def revoke(self, **kwargs): pass


class mailbox(CoreEcpObject):
    @request_action
    def mailbox(self, **kwargs): pass

    @request_action
    def list(self, **kwargs): pass

    @request_action
    def add(self, **kwargs): pass

    @request_action
    def update(self, **kwargs): pass

    @request_action
    def delete(self, **kwargs): pass

    @request_action
    def verifyPop(self, **kwargs): pass

    @request_action
    def findPopServer(self, **kwargs): pass


class message(CoreEcpObject):
    @request_action
    def message(self, **kwargs): pass

    @request_action
    def send(self, **kwargs): pass

    @request_action
    def save(self, **kwargs): pass

    @request_action
    def list(self, **kwargs): pass

    @request_action
    def breakThread(self, **kwargs): pass

    @request_action
    def headers(self, **kwargs): pass

    @request_action
    def quoted(self, **kwargs): pass

    @request_action
    def discardDraft(self, **kwargs): pass

    # TODO Implement import action in a uniform manner


class metrics(CoreEcpObject):
    @request_action
    def mailbox_traffic(self, **kwargs): pass

    @request_action
    def mailbox_responsetime(self, **kwargs): pass

    @request_action
    def mailbox_breakdown(self, **kwargs): pass

    @request_action
    def mailbox_trafficdistribution(self, **kwargs): pass

    @request_action
    def mailbox_useractivity(self, **kwargs): pass

    @request_action
    def usersonline(self, **kwargs): pass


class note(CoreEcpObject):
    @request_action
    def add(self, **kwargs): pass

    @request_action
    def delete(self, **kwargs): pass

    @request_action
    def list(self, **kwargs): pass


class partner(CoreEcpObject):
    @request_action
    def authenticate(self, **kwargs): pass

    @request_action
    def revoke(self, **kwargs): pass


class popAccount(CoreEcpObject):
    @request_action
    def update(self, **kwargs): pass

    @request_action
    def verify(self, **kwargs): pass

    @request_action
    def findServer(self, **kwargs): pass

    @request_action
    def list(self, **kwargs): pass


class preference(CoreEcpObject):
    @request_action
    def get(self, **kwargs): pass

    @request_action
    def set(self, **kwargs): pass


class search(CoreEcpObject):
    @request_action
    def search(self, **kwargs): pass

    @request_action
    def get(self, **kwargs): pass

    @request_action
    def list(self, **kwargs): pass

    @request_action
    def save(self, **kwargs): pass

    @request_action
    def delete(self, **kwargs): pass


class smtpServer(CoreEcpObject):
    @request_action
    def update(self, **kwargs): pass

    @request_action
    def delete(self, **kwargs): pass

    @request_action
    def list(self, **kwargs): pass

    @request_action
    def verify(self, **kwargs): pass


class tag(CoreEcpObject):
    @request_action
    def complete(self, **kwargs): pass

    @request_action
    def add(self, **kwargs): pass

    @request_action
    def set(self, **kwargs): pass

    @request_action
    def list(self, **kwargs): pass

    @request_action
    def rename(self, **kwargs): pass

    @request_action
    def delete(self, **kwargs): pass


class template(CoreEcpObject):
    @request_action
    def list(self, **kwargs): pass

    @request_action
    def delete(self, **kwargs): pass

    @request_action
    def add(self, **kwargs): pass

    @request_action
    def update(self, **kwargs): pass

    @request_action
    def send(self, **kwargs): pass

    @request_action
    def template(self, **kwargs): pass

    @request_action
    def render(self, **kwargs): pass

    @request_action
    def inputFields(self, **kwargs): pass

    @request_action
    def renderText(self, **kwargs): pass


class ticket(CoreEcpObject):
    @request_action
    def ticket(self, **kwargs): pass


class user(CoreEcpObject):
    @request_action
    def list(self, **kwargs): pass

    @request_action
    def resetPassword(self, **kwargs): pass

    @request_action
    def resetKey(self, **kwargs): pass

    @request_action
    def delete(self, **kwargs): pass

    @request_action
    def add(self, **kwargs): pass

    @request_action
    def update(self, **kwargs): pass

    @request_action
    def user(self, **kwargs): pass


class utility(CoreEcpObject):
    @request_action
    def test(self, **kwargs): pass

    @request_action
    def context(self, **kwargs): pass

    @request_action
    def refreshSession(self, **kwargs): pass
