def deleteClones(currentEmails):
    newEmails = []
    for index in currentEmails:
        if not (currentEmails[index] in newEmails):
            newEmails.append(currentEmails[index])
    return newEmails
