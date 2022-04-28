
#import encore_pros
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

def viewlogic_emp():
    viewqry="""select * from employee"""
    cur.execute(viewqry)
    rs=cur.fetchall()
    for row in rs:
        for col in row:
             print(col,end="\t")
        print()

def insertlogic_emp():
    print("""1)Monitor
             2)Admin""")
    i=int(input("Enter which type of User Account you want to Add"))
    if i==1:
        userName=input("Enter userName")
        userPass=input("Enter userPass")
        userType="Monitor"
        fullName=input("Enter Fullname ")
        prospPhone=input("Enter prospect contact number")
        email=input("Enter Email")
        status=input("Enter status")
        insqry=f"insert into prospect values('{userName}','{userPass}','{userType}','{fullName}','{prospPhone}','{email}','{status}')"#This program is created by Sachin.
        if cur.execute(insqry):
            print("Record inserted")
        conn.commit()
        viewlogic_emp()

    if i==2:
        userName=input("Enter userName")
        userPass=input("Enter userPass")
        userType="Admin"
        fullName=input("Enter Fullname ")
        prospPhone=input("Enter prospect contact number")
        email=input("Enter Email")
        status=input("Enter status")
        insqry=f"insert into prospect values('{userName}','{userPass}','{userType}','{fullName}','{prospPhone}','{email}','{status}')"#This program is created by Sachin.
        if cur.execute(insqry):
            print("Record inserted")
        conn.commit()
        viewlogic_emp()

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

def passwordlogic():
    print("""1)Self
             2)Other""")
    p=int(input("Whom Password you want to Change:-"))
    if p==1:
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
        viewlogic_emp()

    if p==2:
        passqry=f"select * from employee where userType='{Admin}'"
        cur.execute(passqry)
        rs=cur.fetchall()
        for i in rs:
            for j in i:
                print(j,end=" ")
        userName=input("Enter the userName")
        userPass=input("Enter new Password:-")
        upqry=f"update employee set userPass='{userPass}' where userName={userName}"
        cur.execute(upqry)
        rs=cur.fetchall()
        for i in rs:
            for j in i:
               print(j,end=" ")
        viewlogic_emp()


def acti_deacti():
    userName=input("Enter the userName:-")
    acqry=f"update employee set status='Deactivated' where userName={userName}"
    cur.execute(acqry)
    rs=cur.fetchall()
    for i in rs:
        for j in i:
            print(j,end=" ")
    viewlogic_emp()        


# def login():
#     print("Enter userName and userPass to login")
#     userName=input("Enter the userName:-")
#     userPass=input("Enter the Password:-")
#     logqry=f"select userName,userPass from employee where status='Activated'" 
#     cur.execute(logqry)


print("Login")
userName=input("Enter the userName:-")
userPass=input("Enter the Password:-")
logqry=f"select userName,userPass from employee where status='Activated'"
cur.execute(logqry)
while (f"userName and userPass in employee"):

    print(""" 
    1)Create User Account
    2)View All Users(Employees)
    3)View All Prospects
    4)Change Password
    5)Search Prospect
    6)Signout
    """)
    k=int(input("Select from above menu:-"))
    if k==1:
        insertlogic_emp()
    elif k==2:
        viewlogic_emp()
    elif k==3:
        viewlogic()
    elif k==4:
        passwordlogic()
    elif k==5:
        searchlogic()
    elif k==6:
        print("Signout Successfully")
        k=None
    cur.close()
    conn.close()

