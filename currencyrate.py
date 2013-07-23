import urllib2, os, sys
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://www.exchangerate.com/').read())

print "\nWelcome, please input your currencies using their 3-digit ISO codes.(USD, AUS, EUR, etc.)"

base = raw_input("\nWhat currency are you using now?").upper()
base = base.replace(" ","")

new = raw_input("\nWhat currency do you want to convert it to?").upper()
new = new.replace(" ","")

much = raw_input("\nHow much do you want to convert?(enter numbers only):")
much = much.replace(" ","")

if much.isdigit() == False:
	print "\nPlease use numbers only. Program will restart"
	os.system("currencyrate.py")
	sys.exit()
	
base_value = None
for cell in soup.findAll('td'):
    if base == cell.text:
         base_value = cell.nextSibling.text

new_value = None		 
for cell in soup.findAll('td'):
    if new == cell.text:
         new_value = cell.nextSibling.text
		 
if not base_value:
	print "\nOops! It look like you entered a non-valid currency. Program will restart"
	os.system("currencyrate.py")
	sys.exit()

if not new_value:
	print "\nOops! It look like you entered a non-valid currency. Program will restart"
	os.system("currencyrate.py")
	sys.exit()

base_value = float(base_value)
new_value = float(new_value)
how_much = float(much)

worth = (new_value/base_value) * how_much


print "\n%s %s is worth ~%.2f %s." % (much, base, worth, new)
