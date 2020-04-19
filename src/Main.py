from MailsBase import MailsBase
from functions import returnWithoutClones, returnOnlyValid, saveFile, openFile, yesOrNo, printArrow, printWelcomeMessage
from termcolor import colored
from colorama import init
import sys
import time
import easygui

actualBasePath = ""
newBasePath = ""
newEmails = []


def run():
    printWelcomeMessage()
    print(printArrow() +
          " Before using app make sure that your mail addresses base is preapred correctly.")
    print(printArrow() +
          " Full instructions of using this app you will find in instructions.txt file.")
    print(printArrow() +
          " Choose .txt file with your base: ")
    print(printArrow(), end='')
    input(" Press ENTER to open files window...")
    actualBasePath = openFile()
    print(printArrow(), end='')
    if yesOrNo(" Are you sure you want to use " + actualBasePath + " file?"):
        actualBase = MailsBase(actualBasePath)
        actualBase.loadEmailAddresses()
        newEmails = actualBase.getMails()
    else:
        print(printArrow() +
              " Ok, so i am closing program")
        time.sleep(2)
        sys.exit()
    print(printArrow(), end='')
    if yesOrNo(" Do you want to delete clones?"):
        newEmails = returnWithoutClones(newEmails)
    else:
        print(printArrow() +
              " Ok, so i am not deleting clones")
    print(printArrow(), end='')
    if yesOrNo(" Do you want to delete invalid email addresses?"):
        newEmails = returnOnlyValid(newEmails)
    else:
        print(printArrow() +
              " Ok, so i am not deleting incorrect email addresses.")
    print(printArrow() +
          " Where should I save your base?")
    print(printArrow(), end='')
    input(" Press ENTER to open files window...")
    newBasePath = saveFile()
    newBase = MailsBase(newBasePath)
    newBase.pushMails(newEmails)
    newBase.saveBase()
    print(printArrow() +
          " Your email addresses base is actual. You will find it here: " + newBasePath)
    print(printArrow() +
          colored(" Thanks for using this App :)", 'green'))
    print(printArrow(), end='')
    input(" Press ENTER to finish...")
