import mysql.connector
import hashlib
db = mysql.connector.connect(
     host="localhost",
     user="root",
     password="Ader1234",
     database="news_sites"
    )
mycursor =db.cursor()

def insert_new(newName,newPass):
    newName=str(newName)
    newPass.encode(encoding='UTF-8', errors='strict')
    hPasswordAttempt = hashlib.sha256(newPass.encode(encoding='UTF-8', errors='strict')).hexdigest()

    firstAddress = ("INSERT INTO usernames (usernames,password) VALUES(%s,%s)")
    values = [newName, hPasswordAttempt]
    mycursor.execute(firstAddress, values)
    db.commit()

def get_login(name,password):
    firstAddress=("SELECT password FROM usernames WHERE usernames =%s")
    values=(name,)
    mycursor.execute(firstAddress,values)
    enteredPassword=mycursor.fetchall()

    for x in enteredPassword:
        dbpassword=str(x[0])

    password.encode(encoding = 'UTF-8', errors = 'strict')
    hPasswordAttempt=hashlib.sha256(password.encode(encoding = 'UTF-8', errors = 'strict')).hexdigest()

    if hPasswordAttempt==dbpassword:
        return True
    else:
        return False

#print(hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest())

print(get_login("will2254","neewwe"))