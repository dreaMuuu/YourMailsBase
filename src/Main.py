from MailsBase import MailsBase
from functions import returnWithoutClones, returnOnlyValid, yesOrNo, openFile, saveFile
import sys
import time
import easygui

actualBasePath = ""
newBasePath = ""
newEmails = []


def run():
    print("> YourMailsBase - version 1.0.0 - copyrights @ Piotr Filipek, dreamalltime")
    print("> Before using app make sure that your base is preapred correctly")
    print("> Choose .txt file with your base: ")
    input("> Press ENTER to open files window...")
    actualBasePath = openFile()
    if yesOrNo("> Are you sure you want to use " + actualBasePath + " file?"):
        actualBase = MailsBase(actualBasePath)
        actualBase.loadEmailAddresses()
        newEmails = actualBase.getMails()
    else:
        print("> Ok, so i am closing program")
        time.sleep(2)
        sys.exit()
    if yesOrNo("> Do you want to delete clones?"):
        newEmails = returnWithoutClones(newEmails)
    else:
        print("> Ok, so i am not deleting clones")
    if yesOrNo("> Do you want to delete incorrect email addresses?"):
        newEmails = returnOnlyValid(newEmails)
    else:
        print("> Ok, so i am not deleting incorrect email addresses.")
    print("> Where should I save your base?")
    input("> Press ENTER to open files window...")
    newBasePath = saveFile()
    newBase = MailsBase(newBasePath)
    newBase.pushMails(newEmails)
    newBase.saveBase()
    print("> Your email addresses base is actual. You will find it here: " + newBasePath)
    input("Press ENTER to finish...")
