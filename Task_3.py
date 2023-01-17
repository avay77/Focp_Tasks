import random
import sys
import re

if len(sys.argv)!=2:
    print("Error: Missing command-line argument.")
    sys.exit()
try:
    f=open(sys.argv[1],"r")
except:
    print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")
    sys.exit()

w=open("students_email.txt","w")
 
def getData():
    recordlist=[]
    lines=f.readlines()
    for line in lines:
        record=line.strip()
        data=re.split(",",record,1)
        recordlist.append(data)
    dataSeparate(recordlist)

def dataSeparate(recordlist):
    for record in recordlist: 
        first_part=re.split("\s",record[0])
        last_part=re.split("\s",record[1])
        last_part.pop(0)    
        student_id=first_part[0]
        last_name=removeNonAlpha(first_part[1:])
        first_name=".".join(genFirstName(last_part))
        email=generateEmail(last_name,first_name)
        writeFile(student_id,email)

def removeNonAlpha(data):
    mainstr=""
    for i in data:
        for j in i:
            if j.isalpha()==True:
                mainstr+=j
    return mainstr.lower()

def genFirstName(data):
    mainstr=""
    for i in data:
        a=i[0]
        mainstr+=a.lower()
    return mainstr
    
def generateEmail(first_name,last_name):
    mail=str(last_name)+"."+str(first_name)+str(random.randint(1000,9999))+"@poppleton.ac.uk"
    return mail

def writeFile(student_id,email):
    w.write(f'{student_id} {email}\n')
    

getData()
f.close()
w.close()