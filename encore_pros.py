import pymysql as db
conn=db.connect("localhost","root","","encore")
cur=conn.cursor()

def viewlogic():
    viewqry="""select * from prospect"""
    cur.execute(viewqry)
    rs=cur.fetchall()
    for row in rs:
        for col in row:
             print(col,end="\t")
        print()
.
def insertlogic():
    prospId=input("Enter prospect ID")
    prospName=input("Enter prospect name")
    prospPhone=input("Enter prospect contact number")
    prospAddress=input("Enter prospect address")
    interestedModel=input("Enter the Model in which the prospect is interested .")
    interestedColor=input("Enter the Model colour.")
    dateOfVisit=input("Enter the date of visit.")
    priority=input("Enter priority")
    gender=input("Enter gender")

    insqry=f"insert into prospect values({prospId},'{prospName}','{prospPhone}','{prospAddress}','{interestedModel}','{interestedColor}','{dateOfVisit}','{priority}','{gender}')"#This program is created by Sachin.
    if cur.execute(insqry):
        print("Record inserted")
    conn.commit()
    viewlogic()

def searchlogic():
    print("""1)Prospect Id
             2)By Priority""")
    s=int(input("By which you want to search prospect:"))
    if s==1: 
        prospId=input("Enter prospId to search")
        serqry=f"select * from prospect where prospId={prospId}"
        cur.execute(serqry)
        rs=cur.fetchall()
        for i in rs:
            for j in i:
                print(j,end=" ")
    elif s==2:
        Priority=input("Enter Priority to search")
        serqry=f"select * from prospect where Priority='{Priority}'"
        cur.execute(serqry)
        rs=cur.fetchall()
        for i in rs:
            for j in i:
                print(j,end=" ")
    else:
        print("Invalid input")
             
def updatelogic():
    viewlogic()
    print("""1)Phone
             2)Model 
             3)Color
             4)Priority""")
    u=int(input("By which you want to update prospect:"))

    prospId=input("Enter prospId to update record")
    if u==1:
        prospPhone=input("Enter the contact")
        upqry=f"update prospect set prospPhone='{prospPhone}' where prospId={prospId}"
        cur.execute(upqry)
        rs=cur.fetchall()
        for i in rs:
            for j in i:
                print(j,end=" ")
        viewlogic()
    elif u==2:
        interestedModel=input("Enter the new interested Model")
        upqry=f"update prospect set interestedModel='{interestedModel}' where prospId={prospId}"
        cur.execute(upqry)
        rs=cur.fetchall()
        for i in rs:
            for j in i:
                print(j,end=" ")
        viewlogic()
    elif u==3:
        interestedColor=input("Enter the new interested Color")
        upqry=f"update prospect set interestedColor='{interestedColor}' where prospId={prospId}"
        cur.execute(upqry)
        rs=cur.fetchall()
        for i in rs:
            for j in i:
                print(j,end=" ")
        viewlogic()
    elif u==4:
        priority=input("Enter the new priority")
        upqry=f"update prospect set priority='{priority}' where prospId={prospId}"
        cur.execute(upqry)
        rs=cur.fetchall()
        for i in rs:
            for j in i:
                print(j,end=" ")
        viewlogic()
    else:
        print("Invalid Input")

    viewlogic()

def login():
    print("Enter userName and userPass to login")
    userName=input("Enter the userName:-")
    userPass=input("Enter the Password:-")
    logqry=f"select userName,userPass from employee where status='Activated',userType='Monitor'" 
    cur.execute(logqry)

def signout():
    print("Signout Successfully")
    cur.close()
    conn.close()

def passchange():
    passqry=f"select * from employee where userType='{Monitor}'"
    cur.execute(passqry)
    rs=cur.fetchall()
    for i in rs:
        for j in i:
            print(j,end=" ")
    userName=input("Enter the userName")
    userPass=input("Enter new Password:-")
    upqry=f"update prospect set userPass='{userPass}' where userName={userName}"
    cur.execute(upqry)
    rs=cur.fetchall()
    for i in rs:
        for j in i:
            print(j,end=" ")
    print("Password Changed")


print("Login as Monitor")
userName=input("Enter the userName:-")
userPass=input("Enter the Password:-")
logqry=f"select userName,userPass from employee where status='Activated'and userType='Monitor'" 
cur.execute(logqry)
while (f"userName and userPass in employee"):
        print(""" 
        1)Add New Prospect
        2)Search Prospect
        3)Update Prospect
        4)View All Prospect
        5)Change Own Password
        6)Signout
        """)
        k=int(input("Select from above menu:-"))
        if k==1:
            insertlogic()
        elif k==2:
            searchlogic()
        elif k==3:
            updatelogic()
        elif k==4:
            viewlogic()
        elif k==5:
            passchange()
        elif k==6:
            print("Signout Successfully")
            k==None
        cur.close()
        conn.close()
