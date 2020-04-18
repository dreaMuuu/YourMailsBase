from MailsBase import MailsBase
from functions import returnWithoutClones, returnOnlyValid, yesOrNo
import sys

currentBasePath = ""
newBasePath = ""
newEmails = []

print("Before using app, be sure your emailsList is in txt file in right place (how to prepare emails list you can read in readme")
print("Pass name of file with current base with extension: ")
currentBasePath = input(">")
if yesOrNo("Are you sure you want to use " + currentBasePath + " file?"):
    actualBase = MailsBase(currentBasePath)
    actualBase.loadEmailAddresses()
    newEmails = actualBase.getMails()
else:
    print("Ok, so i am closing program")
    sys.exit()
print("Pass name of new file containing Emails Base with extension")
newBasePath = input(">")
if yesOrNo("Do you want to delete clones?"):
    newEmails = returnWithoutClones(newEmails)
else:
    print("Ok, so i am not deleting clones")
if yesOrNo("Do you want to delete incorrect email addresses?"):
    newEmails = returnOnlyValid(newEmails)
else:
    print("Ok, so i am not deleting incorrect email addresses.")
newBase = MailsBase(newBasePath)
newBase.pushMails(newEmails)
newBase.saveBase()
print("Your email addresses base is actual. You will find it as: " + newBasePath)
