class Account(object):
    def __init__(self, **kwargs):
        self.id = None
        self.name = ''
        self.owner = ''
        self.paymentProfile = None
        self.preferences = {}
        self.invoices = []
        self.__dict__.update(kwargs)
