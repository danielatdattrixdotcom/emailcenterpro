class Account(object):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.name = ''
        self.owner = ''
        self.paymentProfile = None
        self.preferences = {}
        self.invoices = []
        if len(args) == 1:
            self.__dict__.update(args[0])
        self.__dict__.update(kwargs)

class Attachment(object):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.fileName = ''
        self.fileType = ''
        self.fileSize = ''
        if len(args) == 1:
            self.__dict__.update(args[0])
        self.__dict__.update(kwargs)