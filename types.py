NOTE_TYPE_NOTE = 0
NOTE_TYPE_CALL = 1
NOTE_TYPE_CHAT = 2
NOTE_TYPE_CONTACT = 3

class Type(object):
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.__dict__.update(args[0])
        self.__dict__.update(kwargs)


class Account(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.name = ''
        self.owner = ''
        self.paymentProfile = None
        self.preferences = {}
        self.invoices = []
        super(Account, self).__init__(*args, **kwargs)


class Attachment(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.fileName = ''
        self.fileType = ''
        self.fileSize = ''
        super(Attachment, self).__init__(*args, **kwargs)


class CallNote(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.phoneNumber = ''
        self.duration = ''
        self.contactId = ''
        self.incoming = None
        self.userId = ''
        self.date = None
        self.noteText = ''
        self.type = NOTE_TYPE_CALL
        super(CallNote, self).__init__(*args, **kwargs)


class ChatNote(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.emailAddress = ''
        self.duration = ''
        self.contactId = ''
        self.chatId = ''
        self.department = ''
        self.service = ''
        self.userId = ''
        self.date = None
        self.noteText = ''
        self.type = NOTE_TYPE_CHAT
        super(ChatNote, self).__init__(*args, **kwargs)


class Contact(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.name = ''
        self.details = []
        super(Contact, self).__init__(*args, **kwargs)


class Conversation(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.subject = ''
        self.userId = ''
        self.mailboxId = ''
        self.folder = ''
        self.messageDate = None
        self.actionDate = None
        self.snippet = ''
        self.unread = None
        self.locks = []
        self.messageCount = ''
        self.noteCount = ''
        self.historyCount = ''
        self.spamScore = ''
        self.histories = []
        self.messages = []
        self.notes = []
        self.tags = []
        self.ticket = None
        self.contacts = []
        self.richContacts = []
        super(Conversation, self).__init__(*args, **kwargs)


class History(Type):
    ACTION_RECEIVED = 1
    ACTION_SENT = 8
    ACTION_REPLIED = 9
    ACTION_FORWARDED = 10
    ACTION_SWITCHED = 4
    ACTION_ASSIGNED = 5
    ACTION_TAGGED = 6
    ACTION_DETAGGED = 7
    ACTION_NOTED = 11
    ACTION_CONTACT_NOTED = 28
    ACTION_CHANGED_FOLDER = 12
    ACTION_STARRED = 15
    ACTION_CALLED = 16
    ACTION_TICKETED = 17
    ACTION_DRAFTED = 18
    ACTION_LOGIN = 20
    ACTION_LOGOUT = 21
    ACTION_CHAT = 24
    ACTION_META_CHANGE_MAILBOX = 25
    ACTION_META_CHANGE_USER = 26
    ACTION_META_CHANGE_SETTING = 27

    def __init__(self, *args, **kwargs):
        self.id = None
        self.messageId = ''
        self.conversationId = ''
        self.note = ''
        self.userId = ''
        self.actionId = ''
        self.timestamp = None
        self.reference = ''
        self.mailboxId = ''
        super(History, self).__init__(*args, **kwargs)


class Mailbox(Type):
    FOLDER_INBOX = 0
    FOLDER_ARCHIVE = 1
    FOLDER_SPAM = 2
    FOLDER_SENT = 3 #Magic
    FOLDER_TRASH = 4
    FOLDER_DRAFT = 5 #Magic

    def __init__(self, *args, **kwargs):
        self.id = None
        self.mailUser = ''
        self.domain = ''
        self.fromName = ''
        self.internalName = ''
        self.replyTo = ''
        self.signature = ''
        self.count = ''
        self.pop_accounts = []
        self.users = []
        self.preferences = {}
        super(Mailbox, self).__init__(*args, **kwargs)


class Message(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.mailboxId = ''
        self.fromAddr = ''
        self.fromName = ''
        self.toAddr = ''
        self.subject = ''
        self.date = ''
        self.replyTo = ''
        self.cc = ''
        self.bcc = ''
        self.owner = ''
        self.folder = ''
        self.sent = ''
        self.unread = ''
        self.quoted = ''
        self.quotedText = ''
        self.indexed = ''
        self.size = ''
        self.hasAttachment = ''
        self.spamScore = ''
        self.messageIdHeader = ''
        self.draft = ''
        self.snippet = ''
        self.plainBody = ''
        self.htmlBody = ''
        self.conversationId = ''
        self.attachments = ''
        self.tags = ''
        self.histories = ''
        self.contacts = ''
        self.templates = ''
        super(Message, self).__init__(*args, **kwargs)


class Note(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.userId = ''
        self.date = None
        self.noteText = ''
        self.type = None
        super(Note, self).__init__(*args, **kwargs)


class PopAccount(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.accountNickname = ''
        self.server = ''
        self.username = ''
        self.password = ''
        self.port = ''
        self.leaveCopy = None
        self.useSsl = None
        self.selfSigned = None
        self.importOldMail = None
        self.lastSuccessful = None
        self.active = None
        super(PopAccount, self).__init__(*args, **kwargs)


class Rule(Type):
    OPERATOR_EQUALS = 1
    OPERATOR_CONTAINS = 2
    OPERATOR_STARTS_WITH = 3
    OPERATOR_ENDS_WITH = 4
    OPERATOR_BEFORE = 5
    OPERATOR_AFTER = 6
    OPERATOR_BETWEEN = 7
    OPERATOR_NEWER_THAN = 8
    OPERATOR_OLDER_THAN = 9
    OPERATOR_TODAY = 23
    OPERATOR_YESTERDAY = 24
    OPERATOR_USER_ME = 16
    OPERATOR_USER_NOBODY = 17
    OPERATOR_NOT_EQUALS = 18
    OPERATOR_NOT_CONTAINS = 19
    OPERATOR_IN = 20
    OPERATOR_TRUE = 21
    OPERATOR_FALSE = 22

    TYPE_USER = 1
    TYPE_MAILBOX = 2
    TYPE_MESSAGE_DATE = 3
    TYPE_ACTION_DATE = 4
    TYPE_TAG = 5
    TYPE_SUBJECT = 6
    TYPE_FROM = 7
    TYPE_TO = 8
    TYPE_CC = 9
    TYPE_RECIPIENT = 10
    TYPE_FOLDER = 11
    TYPE_HAS_ATTACHMENT = 12
    TYPE_ATTACHMENT_NAME = 13
    TYPE_BODY = 14
    TYPE_ACTION = 15
    TYPE_NOTE = 16
    TYPE_SENDER = 17
    TYPE_UNREAD = 18
    TYPE_STARRED = 19
    TYPE_TICKETED = 20
    TYPE_CONVERSATION = 21
    TYPE_MESSAGE = 22
    TYPE_CONTACT = 23
    TYPE_TEMPLATE = 24
    TYPE_MESSAGE_FIRST = 25
    TYPE_CREATOR = 30
    TYPE_MIME_TYPE = 31
    TYPE_SENT = 40
    TYPE_DRAFT = 41

    def __init__(self, *args, **kwargs):
        self.type = None
        self.operator = None
        self.values = []
        super(Rule, self).__init__(*args, **kwargs)


class SmartFolder(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.shared = None
        self.rules = []
        self.name = ''
        super(SmartFolder, self).__init__(*args, **kwargs)


class SmtpServer(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.server = ''
        self.nickname = ''
        self.username = ''
        self.port = None
        self.useSsl = None
        self.authenticate = None
        self.selfSigned = None
        super(SmtpServer, self).__init__(*args, **kwargs)


class Template(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.mailboxId = ''
        self.name = ''
        self.body = ''
        self.plainBody = ''
        self.tags = []
        self.attachments = []
        super(Template, self).__init__(*args, **kwargs)


class Ticket(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.conversationId = ''
        self.customId = ''
        self.url = ''
        super(Ticket, self).__init__(*args, **kwargs)


class User(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.firstName = ''
        self.lastName = ''
        self.username = ''
        self.password = ''
        self.role = None
        self.contactEmail = ''
        self.smsNumber = ''
        self.defaultMailbox = ''
        self.rssKey = ''
        self.signature = ''
        self.preferences = {}
        self.alerts = []
        self.mailboxes = []
        super(User, self).__init__(*args, **kwargs)
