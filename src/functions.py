from validate_email import validate_email


def returnWithoutClones(currentEmails):
    newEmails = []
    for mail in currentEmails:
        if not (mail in newEmails):
            newEmails.append(mail)
    return newEmails


def returnOnlyValid(currentEmails):
    newEmails = []
    for mail in currentEmails:
        if validate_email(mail):
            newEmails.append(mail)
    return newEmails


def returnOnlyExists(currentEmails):
    pass
