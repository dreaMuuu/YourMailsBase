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


def yesOrNo(question):
    while "Press only Y or N!":
        reply = str(input(question + ' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False
