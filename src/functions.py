from validate_email import validate_email
from colorama import init
from termcolor import colored
import easygui
import time


def returnWithoutClones(currentEmails):
    newEmails = []
    countOfClones = 0
    for mail in currentEmails:
        if not (mail in newEmails):
            newEmails.append(mail)
        else:
            print(printArrow() + colored(" deleted clone", 'green'))
            countOfClones += 1
            time.sleep(0.2)
    print(printArrow() + " Count of deleted clones: " +
          colored(str(countOfClones), 'green'))
    return newEmails


def returnOnlyValid(currentEmails):
    newEmails = []
    countOfInvalid = 0
    for mail in currentEmails:
        if validate_email(mail):
            newEmails.append(mail)
        else:
            print(printArrow() + colored(" deleted invalid address", 'green'))
            countOfInvalid += 1
            time.sleep(0.2)
    print(printArrow() + " Count of deleted not valid addresses: " +
          colored(str(countOfInvalid), 'green'))
    return newEmails


def yesOrNo(question):
    while True:
        reply = str(input(question + ' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        elif reply[0] == 'n':
            return False


def printWelcomeMessage():
    print(colored("# YourMailsBase - version 1.0.0 - copyrights @ Piotr Filipek, dreamalltime #", 'cyan'))


def printArrow():
    return colored('>', 'magenta')


def openFile():
    return easygui.fileopenbox(title="Choose your base file", default="*.txt")


def saveFile():
    return easygui.filesavebox(
        title="Choose where to save your base", default='mails.txt')
