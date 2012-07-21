from hashlib import sha1
import hmac
import binascii
from time import strftime, gmtime
from urllib import urlencode
import urllib2
from urllib2 import HTTPError
import objects

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
        self.account = objects.account(self)
        self.attachment = objects.attachment(self)
        self.call = objects.call(self)
        self.chat = objects.chat(self)
        self.contact = objects.contact(self)
        self.conversation = objects.conversation(self)
        self.folder = objects.folder(self)
        self.history = objects.history(self)
        self.invoice = objects.invoice(self)
        self.key = objects.key(self)
        self.mailbox = objects.mailbox(self)
        self.message = objects.message(self)
        self.metrics = objects.metrics(self)
        self.note = objects.note(self)
        self.partner = objects.partner(self)
        self.popAccount = objects.popAccount(self)
        self.preference = objects.preference(self)
        self.search = objects.search(self)
        self.smtpServer = objects.smtpServer(self)
        self.tag = objects.tag(self)
        self.template = objects.template(self)
        self.ticket = objects.ticket(self)
        self.user = objects.user(self)
        self.utility = objects.utility(self)

    def makeRequest(self, content):
        # Combine persistent arguments with those passed in.
        # Passed arguments can override persistent ones
        arguments = self._args
        arguments.update(content)
        content = urlencode(arguments)

        # We use filter here due to the __call__ method being a potential source of a request
        self._action = filter(None,self._action)
        if self._action[-1] != 'call':
            api_action = '/%s/%s' % (self._object, '/'.join(self._action))
        else:
            api_action = '/%s' % (self._object,)

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