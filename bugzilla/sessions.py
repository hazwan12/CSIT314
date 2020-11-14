import datetime

class Sessions:

    def __init__(self):
        self.user = None

    def activate(self, email):
        self.user = email
        self.session_created = datetime.datetime.now()

    def deactivate(self):
        self.__init__()