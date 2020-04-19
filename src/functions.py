from validate_email import validate_email
import easygui
import time


def returnWithoutClones(currentEmails):
    newEmails = []
    countOfClones = 0
    for mail in currentEmails:
        if not (mail in newEmails):
            newEmails.append(mail)
        else:
            print("> deleted clone")
            countOfClones += 1
            time.sleep(0.2)
    print("Count of deleted clones: " + str(countOfClones))
    return newEmails


def returnOnlyValid(currentEmails):
    newEmails = []
    countOfInvalid = 0
    for mail in currentEmails:
        if validate_email(mail):
            newEmails.append(mail)
        else:
            print("> deleted invalid address")
            countOfInvalid += 1
            time.sleep(0.2)
    print("Count of deleted not valid addresses: " + str(countOfInvalid))
    return newEmails


def yesOrNo(question):
    while "Press only Y or N!":
        reply = str(input(question + ' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False


def openFile():
    return easygui.fileopenbox(title="Choose your base file")


def saveFile():
    return easygui.filesavebox(
        title="Choose where to save your base", default='mails.txt')
