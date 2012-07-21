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

        # Default request type is POST
        self._request_method = 'POST'

        # Setup optional persistent arguments
        self._args = {}
        for k, v in kwargs.items():
            self._args[k] = v

        self.clear()

        # All the objects get initialized
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
        # Combine persistent arguments with those passed in.
        # Passed arguments can override persistent ones
        arguments = self._args
        arguments.update(content)
        content = urlencode(arguments)

        api_action = '/%s/%s' % (self._object, '/'.join(self._action))

        def create_auth_headers(self):
            date = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            body = '\n'.join([self._request_method, api_action, content, date])
            headers = {'Authorization': 'ECP ' + self._key + ':' +
                                        binascii.b2a_base64(hmac.new(self._secret, body, sha1).digest())[:-1], 'Date': date}
            return headers

        action_url = self._url + api_action
        try:
            if self._request_method == 'POST':
                request = urllib2.Request(action_url, content, headers=create_auth_headers(self))
                response = urllib2.urlopen(request)
                self._data = response.read()
            else:
                request = urllib2.Request('%s?%s' % (action_url, content))
                headers = create_auth_headers(self)
                request.add_header('Authorization', headers['Authorization'])
                request.add_header('Date', headers['Date'])
                self._data = urllib2.urlopen(request).read()
        except HTTPError as e:
            self._data = '{"http_error": "%s" }' % (e.code)

    def clear(self, clear_args=None):
        """ Clears last object, action and held return data.
            With first parameter being not None it clears the set arguments as well.
        """
        if clear_args is not None:
            self._args = {}

        self._object = None
        self._action = []
        self._data = None

    def read(self):
        """ For compatibility with JSON decoding
        """
        return self._data

# On methods where the end result is a reply from the API we enforce it with a decorator that also controls request type
def get_request(action_method):
    def wrapper(action_object, **kwargs):
        action_object.connection._request_method = 'GET'
        return action_object._request(action_method.__name__.split('_'), **kwargs)
    return wrapper

def post_request(action_method):
    def wrapper(action_object, **kwargs):
        action_object.connection._request_method = 'POST'
        return action_object._request(action_method.__name__.split('_'), **kwargs)
    return wrapper

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
    @post_request
    def account(self, **kwargs): pass

    @post_request
    def update(self, **kwargs): pass

    @post_request
    def cancel(self, **kwargs): pass

    @get_request
    def stats(self, **kwargs): pass

    @post_request
    def changeLevel(self, **kwargs): pass


class attachment(CoreEcpObject):
    @post_request
    def attachment(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

    @post_request
    def download(self, **kwargs): pass

    @post_request
    def preview(self, **kwargs): pass

    @post_request
    def view(self, **kwargs): pass


class call(CoreEcpObject):
    @post_request
    def add(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

    @post_request
    def call(self, **kwargs): pass


class chat(CoreEcpObject):
    @get_request
    def add(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

    @post_request
    def chat(self, **kwargs): pass


class contact(CoreEcpObject):
    @post_request
    def contact(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

    @post_request
    def complete(self, **kwargs): pass

    @post_request
    def add(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass

    @post_request
    def update(self, **kwargs): pass


class conversation(CoreEcpObject):
    @post_request
    def conversation(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): print 'fffff'

    @post_request
    def assign(self, **kwargs): pass

    @post_request
    def move(self, **kwargs): pass

    @post_request
    def mark(self, **kwargs): pass

    @post_request
    def lock(self, **kwargs): pass

    @post_request
    def unlock(self, **kwargs): pass

    @post_request
    def star(self, **kwargs): pass

    @post_request
    def unstar(self, **kwargs): pass

    @post_request
    def ticket(self, **kwargs): pass

    @post_request
    def message_respond(self, **kwargs): pass

    @post_request
    def purge(self, **kwargs): pass


class folder(CoreEcpObject):
    @post_request
    def list(self, **kwargs): pass


class history(CoreEcpObject):
    @post_request
    def list(self, **kwargs): pass

    @post_request
    def renew(self, **kwargs): pass


class invoice(CoreEcpObject):
    @post_request
    def list(self, **kwargs): pass


class key(CoreEcpObject):
    @post_request
    def list(self, **kwargs): pass

    @post_request
    def issue(self, **kwargs): pass

    @post_request
    def revoke(self, **kwargs): pass


class mailbox(CoreEcpObject):
    @post_request
    def mailbox(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

    @post_request
    def add(self, **kwargs): pass

    @post_request
    def update(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass

    @post_request
    def verifyPop(self, **kwargs): pass

    @post_request
    def findPopServer(self, **kwargs): pass


class message(CoreEcpObject):
    @post_request
    def message(self, **kwargs): pass

    @post_request
    def send(self, **kwargs): pass

    @post_request
    def save(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

    @post_request
    def breakThread(self, **kwargs): pass

    @post_request
    def headers(self, **kwargs): pass

    @post_request
    def quoted(self, **kwargs): pass

    @post_request
    def discardDraft(self, **kwargs): pass

    # TODO Implement import action in a uniform manner


class metrics(CoreEcpObject):
    @post_request
    def mailbox_traffic(self, **kwargs): pass

    @post_request
    def mailbox_responsetime(self, **kwargs): pass

    @post_request
    def mailbox_breakdown(self, **kwargs): pass

    @post_request
    def mailbox_trafficdistribution(self, **kwargs): pass

    @post_request
    def mailbox_useractivity(self, **kwargs): pass

    @post_request
    def usersonline(self, **kwargs): pass


class note(CoreEcpObject):
    @post_request
    def add(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass


class partner(CoreEcpObject):
    @post_request
    def authenticate(self, **kwargs): pass

    @post_request
    def revoke(self, **kwargs): pass


class popAccount(CoreEcpObject):
    @post_request
    def update(self, **kwargs): pass

    @post_request
    def verify(self, **kwargs): pass

    @post_request
    def findServer(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass


class preference(CoreEcpObject):
    @post_request
    def get(self, **kwargs): pass

    @post_request
    def set(self, **kwargs): pass


class search(CoreEcpObject):
    @post_request
    def search(self, **kwargs): pass

    @post_request
    def get(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

    @post_request
    def save(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass


class smtpServer(CoreEcpObject):
    @post_request
    def update(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

    @post_request
    def verify(self, **kwargs): pass


class tag(CoreEcpObject):
    @post_request
    def complete(self, **kwargs): pass

    @post_request
    def add(self, **kwargs): pass

    @post_request
    def set(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

    @post_request
    def rename(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass


class template(CoreEcpObject):
    @post_request
    def list(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass

    @post_request
    def add(self, **kwargs): pass

    @post_request
    def update(self, **kwargs): pass

    @post_request
    def send(self, **kwargs): pass

    @post_request
    def template(self, **kwargs): pass

    @post_request
    def render(self, **kwargs): pass

    @post_request
    def inputFields(self, **kwargs): pass

    @post_request
    def renderText(self, **kwargs): pass


class ticket(CoreEcpObject):
    @post_request
    def ticket(self, **kwargs): pass


class user(CoreEcpObject):
    @post_request
    def list(self, **kwargs): pass

    @post_request
    def resetPassword(self, **kwargs): pass

    @post_request
    def resetKey(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass

    @post_request
    def add(self, **kwargs): pass

    @post_request
    def update(self, **kwargs): pass

    @post_request
    def user(self, **kwargs): pass


class utility(CoreEcpObject):
    @post_request
    def test(self, **kwargs): pass

    @post_request
    def context(self, **kwargs): pass

    @post_request
    def refreshSession(self, **kwargs): pass
