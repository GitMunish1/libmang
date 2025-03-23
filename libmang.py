import mysql.connector as sc

# Connect to MySQL server and create database if not exists
mydb = sc.connect(host='localhost', user='root', password='me.coder@123')
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS LIBRARY")
mycursor.execute("USE LIBRARY")

# Create table for books
rec = """
CREATE TABLE IF NOT EXISTS BOOK (
    bno INTEGER PRIMARY KEY,
    bname VARCHAR(50) NOT NULL,
    bauth VARCHAR(50) NOT NULL,
    bprice INTEGER NOT NULL,
    bqty INTEGER NOT NULL
)
"""
mycursor.execute(rec)

# Re-establish connection for working with the database
mycon = sc.connect(host='localhost', user='root', password='me.coder@123', database='LIBRARY')
mycur = mycon.cursor()


# Function to insert book record
def insertbook():
    bno = int(input("Enter Book Code: "))
    bname = input("Enter Book Name: ")
    bauth = input("Enter Book Author: ")
    bprice = int(input("Enter Book Price: "))
    bqty = int(input("Enter Book Quantity: "))

    qry = "INSERT INTO BOOK VALUES (%s, %s, %s, %s, %s)"
    data = (bno, bname, bauth, bprice, bqty)

    mycur.execute(qry, data)
    mycon.commit()
    print("\t\tRecord ADDED successfully...")


# Function to display book records
def displaybook():
    qry = "SELECT * FROM BOOK"
    mycur.execute(qry)
    data = mycur.fetchall()

    count = mycur.rowcount
    print("\t\tTotal Book Records:", count, "\n")
    for (bno, bname, bauth, bprice, bqty) in data:
        print(f"Book Code:\t{bno}")
        print(f"Book Name:\t{bname}")
        print(f"Book Author:\t{bauth}")
        print(f"Book Price:\t{bprice}")
        print(f"Book Quantity:\t{bqty}\n")


# Function to search book records
def searchbook():
    bno = int(input("Enter book number to be searched: "))
    qry = "SELECT * FROM BOOK WHERE bno = %s"
    rec = (bno,)

    mycur.execute(qry, rec)
    data = mycur.fetchall()

    if data:
        print("\t\tBook Records Found:\n")
        for (bno, bname, bauth, bprice, bqty) in data:
            print(f"Book Code:\t{bno}")
            print(f"Book Name:\t{bname}")
            print(f"Book Author:\t{bauth}")
            print(f"Book Price:\t{bprice}")
            print(f"Book Quantity:\t{bqty}\n")
    else:
        print("\t\t\tRECORD NOT FOUND!")


# Function to delete book records
def deletebook():
    bno = int(input("Enter book number to be deleted: "))
    qry = "SELECT * FROM BOOK WHERE bno = %s"
    rec = (bno,)

    mycur.execute(qry, rec)
    data = mycur.fetchall()

    if data:
        print("\t\tBook Records Found:\n")
        for (bno, bname, bauth, bprice, bqty) in data:
            print(f"Book Code:\t{bno}")
            print(f"Book Name:\t{bname}")
            print(f"Book Author:\t{bauth}")
            print(f"Book Price:\t{bprice}")
            print(f"Book Quantity:\t{bqty}\n")

        opt = input("Are you SURE to DELETE the above record (Y/N)? ")
        if opt.lower() == 'y':
            delete_query = "DELETE FROM BOOK WHERE bno = %s"
            mycur.execute(delete_query, rec)
            mycon.commit()
            print("\n\t\tRecord Deleted Successfully...")
    else:
        print("\t\t\tRECORD NOT FOUND!")


# Function to update book records
def updatebook():
    bno = int(input("Enter book number to be updated: "))
    qry = "SELECT * FROM BOOK WHERE bno = %s"
    rec = (bno,)

    mycur.execute(qry, rec)
    data = mycur.fetchall()

    if data:
        print("\t\tBook Records Found:\n")
        for (bno, bname, bauth, bprice, bqty) in data:
            print(f"Book Code:\t{bno}")
            print(f"Book Name:\t{bname}")
            print(f"Book Author:\t{bauth}")
            print(f"Book Price:\t{bprice}")
            print(f"Book Quantity:\t{bqty}\n")

        opt = input("Are you SURE to UPDATE the above record (Y/N)? ")
        if opt.lower() == 'y':
            bname = input("Enter New Book Name: ")
            bauth = input("Enter New Book Author: ")
            bprice = int(input("Enter New Book Price: "))
            bqty = int(input("Enter New Book Quantity: "))

            update_query = "UPDATE BOOK SET bname = %s, bauth = %s, bprice = %s, bqty = %s WHERE bno = %s"
            rec = (bname, bauth, bprice, bqty, bno)
            mycur.execute(update_query, rec)
            mycon.commit()
            print("\n\t\tRecord Updated Successfully...")
    else:
        print("\t\t\tRECORD NOT FOUND!")


# Menu for Library Management System
while True:
    print("\n\t\tLIBRARY BOOK RECORD MANAGEMENT\n")
    print("\t1. Add New Book Record")
    print("\t2. Display Book Records")
    print("\t3. Search Book Record")
    print("\t4. Delete Book Record")
    print("\t5. Update Book Record")
    print("\t6. EXIT")

    choice = int(input("Enter choice (1-6): "))
    if choice == 1:
        insertbook()
    elif choice == 2:
        displaybook()
    elif choice == 3:
        searchbook()
    elif choice == 4:
        deletebook()
    elif choice == 5:
        updatebook()
    elif choice == 6:
        mycon.close()
        print("\nThanks! Have a nice day...")
        break
    else:
        print("\t!!! Wrong choice. Please enter a choice between 1 and 6.")

