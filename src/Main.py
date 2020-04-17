from MailsBase import MailsBase
from functions import returnWithoutClones, returnOnlyValid

currentBasePath = ""
newBasePath = ""
newEmails = []

print("Before using app, be sure your emailsList is in txt file in right place (how to prepare emails list you can read in readme")
print("Pass name of file with current base with extension: ")
currentBasePath = input(">")
print("Are you sure you want to use " + currentBasePath + " file? Y/N")
# decision
actualBase = MailsBase(currentBasePath)
actualBase.loadEmailAddresses()
newEmails = actualBase.getMails()
print("Pass name of new file containing Emails Base with extension")
newBasePath = input(">")
print("Do you want to delete clones? Y/N")
newEmails = returnWithoutClones(newEmails)
print(newEmails)
print("Do you want to delete incorrect email addresses? Y/N")
newEmails = returnOnlyValid(newEmails)
print(newEmails)
newBase = MailsBase(newBasePath)
newBase.pushMails(newEmails)
newBase.saveBase()
print("Your email addresses base is actual. You will find it as: " + newBasePath)
