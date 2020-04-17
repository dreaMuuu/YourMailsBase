from email_validator import validate_email, EmailNotValidError


def returnWithoutClones(currentEmails):
    newEmails = []
    for index in currentEmails:
        if not (currentEmails[index] in newEmails):
            newEmails.append(currentEmails[index])
    return newEmails


def returnOnlyValid(currentEmails):
    newEmails = []
