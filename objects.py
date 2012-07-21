import json
import types

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

    _type = types.Type

    def __init__(self, connection):
        self.connection = connection
        self.data = {}

    @post_request
    def __call__(self, *args, **kwargs): pass

    def __repr__(self):
        return str(self.data)

    def __iter__(self):
        return self.next()

    def next(self):
        try:
            for item in self.data[self._iterator_key]:
                yield self._type(item)
        except (AttributeError, KeyError):
            raise StopIteration

    def _request(self, action, **kwargs):
        self.connection._object = self.__class__.__name__
        self.connection._action = action
        self.connection.makeRequest(kwargs)
        self.data = json.load(self.connection)
        return self

class account(CoreEcpObject):

    _type = types.Account
    _iterator_key = 'accounts'

    @post_request
    def update(self, **kwargs): pass

    @post_request
    def cancel(self, **kwargs): pass

    @get_request
    def stats(self, **kwargs): pass

    @post_request
    def changeLevel(self, **kwargs): pass


class attachment(CoreEcpObject):

    _type = types.Attachment
    _iterator_key = 'attachments'

    @post_request
    def list(self, **kwargs): pass

    @post_request
    def download(self, **kwargs): pass

    @post_request
    def preview(self, **kwargs): pass

    @post_request
    def view(self, **kwargs): pass


class call(CoreEcpObject):

    _type = types.CallNote
    _iterator_key = 'calls'

    @post_request
    def add(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

class chat(CoreEcpObject):

    _type = types.ChatNote
    _iterator_key = 'chats'

    @get_request
    def add(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

class contact(CoreEcpObject):

    _type = types.Contact
    _iterator_key = 'contact'

    @get_request
    def list(self, **kwargs): pass

    @get_request
    def complete(self, **kwargs): pass

    @post_request
    def add(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass

    @post_request
    def update(self, **kwargs): pass


class conversation(CoreEcpObject):

    _type = types.Conversation
    _iterator_key = 'conversation'

    @post_request
    def list(self, **kwargs): pass

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

    _iterator_key = 'folders'

    @post_request
    def list(self, **kwargs): pass


class history(CoreEcpObject):

    _type = types.History
    _iterator_key = 'history'

    @post_request
    def list(self, **kwargs): pass

    @post_request
    def renew(self, **kwargs): pass


class invoice(CoreEcpObject):

    _iterator_key = 'invoices'

    @post_request
    def list(self, **kwargs): pass


class key(CoreEcpObject):
    """
        Useless until Session-based auth is implemented
    """
    @get_request
    def list(self, **kwargs): pass

    @post_request
    def issue(self, **kwargs): pass

    @post_request
    def revoke(self, **kwargs): pass


class mailbox(CoreEcpObject):

    _type = types.Mailbox
    _iterator_key = 'mailboxes'

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

    _type = types.Message
    _iterator_key = 'messages'

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

    _iterator_key = 'datasets'

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

    _type = types.Note
    _iterator_key = 'note'

    @post_request
    def add(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

# TODO partner needs clarification as to its use and inputs
class partner(CoreEcpObject):
    @post_request
    def authenticate(self, **kwargs): pass

    @post_request
    def revoke(self, **kwargs): pass


class popAccount(CoreEcpObject):

    _type = types.PopAccount
    _iterator_key = 'popAccount'

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

    _iterator_key = 'folders'

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

    _type = types.SmtpServer
    _iterator_key = 'smtpServer'

    @post_request
    def update(self, **kwargs): pass

    @post_request
    def delete(self, **kwargs): pass

    @post_request
    def list(self, **kwargs): pass

    @post_request
    def verify(self, **kwargs): pass


class tag(CoreEcpObject):

    _iterator_key = 'tag'

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

    _type = types.Template
    _iterator_key = 'templates'

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
    def render(self, **kwargs): pass

    @post_request
    def inputFields(self, **kwargs): pass

    @post_request
    def renderText(self, **kwargs): pass

# TODO Needs more documentation for use
class ticket(CoreEcpObject):
    pass

class user(CoreEcpObject):

    _type = types.User
    _iterator_key = 'users'

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

class utility(CoreEcpObject):
    @get_request
    def test(self, **kwargs): pass

    @get_request
    def context(self, **kwargs): pass

    @get_request
    def refreshSession(self, **kwargs): pass
