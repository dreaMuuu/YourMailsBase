from validate_email import validate_email
from colorama import init
from termcolor import colored
import easygui
import time
import sys


def returnWithoutClones(currentEmails):
    newEmails = []
    countOfClones = 0
    for mail in currentEmails:
        mail.lower()
        if not (mail in newEmails):
            newEmails.append(mail)
            print(printArrow() + " " + colored(mail, 'green'))
        else:
            print(printArrow() + " " + colored("(deleted) " + mail, 'red'))
            countOfClones += 1
        time.sleep(0.05)
    print(printArrow() + " ---------------")
    print(printArrow() + " Count of deleted clones: " +
          colored(str(countOfClones), 'green'))
    print(printArrow() + " At this moment your base have: " +
          colored(str(len(newEmails)), 'green') + " addresses")
    return newEmails


def returnOnlyValid(currentEmails):
    newEmails = []
    countOfInvalid = 0
    for mail in currentEmails:
        if validate_email(mail):
            newEmails.append(mail)
            print(printArrow() + " " + colored(mail, 'green'))
        else:
            print(printArrow() + " " + colored("(deleted) " + mail, 'red'))
            countOfInvalid += 1
        time.sleep(0.05)
    print(printArrow() + " ---------------")
    print(printArrow() + " Count of deleted not valid addresses: " +
          colored(str(countOfInvalid), 'green'))
    print(printArrow() + " At this moment your base have: " +
          colored(str(len(newEmails)), 'green') + " addresses")
    return newEmails


def yesOrNo(question):
    while True:
        print(printArrow(), end="")
        reply = str(input(question + ' (y/n): ')).lower().strip()
        try:
            if reply[0] == 'y':
                return True
            elif reply[0] == 'n':
                return False
        except:
            pass


def printWelcomeMessage():
    print(colored("# YourMailsBase - version 1.0.0 - copyrights @ Piotr Filipek, dreamalltime #", 'cyan'))


def printArrow():
    return colored('>>', 'magenta')


def openFile():
    error = " You didint choose file! Do you want to try again? (If no i will close the program)"
    repeater = True
    while repeater:
        path = easygui.fileopenbox(
            title="Choose your base file", default="*.txt")
        if path is None:
            if not yesOrNo(error):
                print(printArrow() + " Ok, so i am closing program.")
                sys.exit()
        else:
            repeater = False
    return path


def saveFile():
    error = " You didint choose path! Do you want to try again? (If no i will close the program)"
    repeater = True
    while repeater:
        path = easygui.filesavebox(
            title="Choose where to save your base", default='mails.txt')
        if path is None:
            if not yesOrNo(error):
                print(printArrow() + " Ok, so i am closing program.")
                sys.exit()
        else:
            repeater = False
    return path
