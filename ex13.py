import re

file = open('emails.txt', "r")
file = file.read()

eAddress = re.findall(r'[\w\"\.-@]*[\w\"\w.-]+@[\w\.-]+\.[\w]+', file)
print (eAddress)
