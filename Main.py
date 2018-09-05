import os
import sys

# SAPI Maker  
# By RDIL  
# Under The MIT License  

codeMode = input("Press 1 then press enter if this is your first time running the script, otherwise press 2 and then Enter - ")
if(codeMode == "1"):
    texttowrite = input("What would you like your computer to say? Enter it here: ")
else:
    texttowrite = input("Please open the file labled SAPI.vbs and delete any text inside it.  Then type in what you want to be said here: ")
sapifile = open("SAPI.vbs", "a")
sapifile.write('Dim message, sapi\n')
sapifile.write('message="'+texttowrite+'"\n')
sapifile.write('Set sapi=CreateObject("sapi.spvoice")\n')
sapifile.write('sapi.Speak message\n')
sapifile.close()

os.system("start SAPI.vbs")  

sys.exit()
