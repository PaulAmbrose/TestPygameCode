# Interface creator
# Paul Ambrose 18/10/2022
# Program to create re-usable code for creating interfaces for python programs

# modules
import os
import datetime

# introduction
print("Interface Code Creator")

# get basic parameters
buttonNumber = input("How many buttons would you like? >> ")
windowWidth = input("How wide would you like your interface to be? >>")
windowHeight = input("How tall would you like your interface to be? >>")
filePath = os.getcwd() + "\output"
# https://www.w3schools.com/python/python_datetime.asp
dateStamp = datetime.datetime.now()
formattedDate = dateStamp.strftime("%y%m%d")

# created textfile
# https://www.pythontutorial.net/python-basics/python-create-text-file/
with open(filePath + '\interface_' + formattedDate + ".py", 'w') as f:
    f.write('Create a new text file!')

# populate textfile
