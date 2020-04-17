class MailsBase:

    def __init__(self, path):
        self.path = "./lists/" + path
        self.mails = []

    def loadEmailAddresses(self):
        file = open(self.path, "r")
        self.mails = file.readlines()
        file.close()

    def saveBase(self):
        file = open(self.path, "w")
        file.write(self.mails)
        file.close()

    def getMails(self):
        return self.mails

    def pushMails(self, mails):
        self.mails = mails
