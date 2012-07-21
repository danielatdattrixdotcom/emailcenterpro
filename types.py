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
    TYPE_NOTE = 0
    TYPE_CALL = 1
    TYPE_CHAT = 2
    TYPE_CONTACT = 3

    def __init__(self, *args, **kwargs):
        self.id = None
        self.phoneNumber = ''
        self.duration = ''
        self.contactId = ''
        self.incoming = None
        self.userId = ''
        self.date = None
        self.noteText = ''
        self.type = None
        super(CallNote, self).__init__(*args, **kwargs)


class ChatNote(Type):
    TYPE_NOTE = 0
    TYPE_CALL = 1
    TYPE_CHAT = 2
    TYPE_CONTACT = 3

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
        self.type = None
        super(ChatNote, self).__init__(*args, **kwargs)


class Contact(Type):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.name = ''
        self.details = []
        super(Contact, self).__init__(*args, **kwargs)