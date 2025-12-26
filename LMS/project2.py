import mysql.connector as a

# ---------- DATABASE CONNECTION ----------
con = a.connect(
    host="localhost",
    user="root",
    passwd="yourpassword",   # change if your MySQL password is different
    port=3306,
    auth_plugin="mysql_native_password"
)

c = con.cursor()

# ---------- DATABASE & TABLE CREATION ----------
c.execute("SHOW DATABASES")
dbs = c.fetchall()

found = False
for db in dbs:
    if db[0] == "library":
        found = True

if not found:
    c.execute("CREATE DATABASE library")

c.execute("USE library")

c.execute("""
CREATE TABLE IF NOT EXISTS books(
    bname VARCHAR(50),
    bcode VARCHAR(10),
    total INT,
    subject VARCHAR(50)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS issue(
    sname VARCHAR(50),
    regno VARCHAR(10),
    bcode VARCHAR(10),
    idate VARCHAR(10)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS submit(
    sname VARCHAR(50),
    regno VARCHAR(10),
    bcode VARCHAR(10),
    sdate VARCHAR(10)
)
""")

con.commit()

# ---------- FUNCTIONS ----------
def addbook():
    bn = input("Enter Book Name: ")
    bc = input("Enter Book Code: ")
    t = int(input("Total Books: "))
    s = input("Enter Subject: ")
    c.execute("INSERT INTO books VALUES (%s,%s,%s,%s)", (bn, bc, t, s))
    con.commit()
    print("Book added successfully!")

def issuebook():
    n = input("Enter Student Name: ")
    r = input("Enter Reg No: ")
    bc = input("Enter Book Code: ")
    d = input("Enter Issue Date: ")
    c.execute("INSERT INTO issue VALUES (%s,%s,%s,%s)", (n, r, bc, d))
    c.execute("UPDATE books SET total = total - 1 WHERE bcode = %s", (bc,))
    con.commit()
    print("Book issued successfully!")

def submitbook():
    n = input("Enter Student Name: ")
    r = input("Enter Reg No: ")
    bc = input("Enter Book Code: ")
    d = input("Enter Submit Date: ")
    c.execute("INSERT INTO submit VALUES (%s,%s,%s,%s)", (n, r, bc, d))
    c.execute("UPDATE books SET total = total + 1 WHERE bcode = %s", (bc,))
    con.commit()
    print("Book submitted successfully!")

def deletebook():
    bc = input("Enter Book Code to delete: ")
    c.execute("DELETE FROM books WHERE bcode = %s", (bc,))
    con.commit()
    print("Book deleted!")

def displaybooks():
    c.execute("SELECT * FROM books")
    data = c.fetchall()
    print("\nBOOK LIST")
    print("---------------------------")
    for i in data:
        print(i)

def displayissued():
    c.execute("SELECT * FROM issue")
    data = c.fetchall()
    print("\nISSUED BOOKS")
    print("---------------------------")
    for i in data:
        print(i)

# ---------- MAIN MENU ----------
while True:
    print("""
====== LIBRARY MANAGEMENT SYSTEM ======
1. Add Book
2. Issue Book
3. Submit Book
4. Delete Book
5. Display All Books
6. Display Issued Books
7. Exit
======================================
""")

    ch = input("Enter your choice (1-7): ")

    if ch == "1":
        addbook()
    elif ch == "2":
        issuebook()
    elif ch == "3":
        submitbook()
    elif ch == "4":
        deletebook()
    elif ch == "5":
        displaybooks()
    elif ch == "6":
        displayissued()
    elif ch == "7":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
