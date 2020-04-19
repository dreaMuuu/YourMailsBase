from MailsBase import MailsBase
from functions import returnWithoutClones, returnOnlyValid, yesOrNo, openFile, saveFile
import sys
import time
import easygui

currentBasePath = ""
newBasePath = ""
newEmails = []

print("> YourMailsBase - version 1.0.0 - copyrights @ Piotr Filipek")
time.sleep(1)
print("> Before using app make sure that your base is preapred correctly")
print("> Choose .txt file with your base: ")
input("> Press any key to open files window...")
currentBasePath = openFile()
if yesOrNo("> Are you sure you want to use " + currentBasePath + " file?"):
    actualBase = MailsBase(currentBasePath)
    actualBase.loadEmailAddresses()
    newEmails = actualBase.getMails()
else:
    print("> Ok, so i am closing program")
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
input("> Press any key to open files window...")
newBasePath = saveFile()
newBase = MailsBase(newBasePath)
newBase.pushMails(newEmails)
newBase.saveBase()
print("> Your email addresses base is actual. You will find it here: " + newBasePath)
