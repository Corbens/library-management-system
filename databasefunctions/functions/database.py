###database.py
import datetime


def getBooks():
    """returns a list of all the books from database.txt"""
    f = open("database.txt", "r")
    books = []
    for b in f:
        books.append(b)
    f.close()
    print("successfully collected books")
    return books


def getLogs():
    """returns a list of all the logs from logfile.txt"""
    f = open("logfile.txt", "r")
    logs = []
    for l in f:
        logs.append(l)
    f.close()
    print("successfully collected logs")
    return logs


def updateDatabase(bookid, whatToUpdate):
    """takes two variables bookid and whatToUpdate and updates the column in
    the database about wether the book is on loan or not with the variable
    whatToUpdate:
    bookid = the id of the book being updated
        whatToUpdate = what the book's loan status is being updated to
                       (e.g. 0 or memberid)"""
    books = getBooks() 
    for i in range(0, len(books)):
        bookDetails = books[i].split(",")
        if bookDetails[0] == bookid: 
            bookDetails[5] = whatToUpdate +"\n"
            updatedBooks = ','.join([str(elem) for elem in bookDetails]) 
            books[i] = updatedBooks
            break
    f = open('database.txt', 'w')
    f.writelines(books)
    f.close()


def updateLogfile(bookid, bookName, bookStatus):
    """takes three variables bookid, bookName and bookStatus and adds a new
    entry to the logfile with the data of the current date, bookid, bookName
    and bookStatus:
        bookid = the id of the book being added to the logs
        bookName = the title of the book being added to the logs
        bookStatus = a string 0 or 1 determining wether the book was returned
                     or checked out respectively"""
    currentDate = datetime.date.today()
    logList = [datetime.date.today(), bookid, bookName, str(bookStatus)+"\n"]
    logFile = ','.join([str(elem) for elem in logList]) 
    f = open("logfile.txt", "a")
    f.write(logFile)
    f.close()


if __name__=="__main__":
    #the following allows you to test the functions getBooks and getLogs
    print(getBooks()) 
    print("\n")
    print(getLogs()) 

    #the following allows you to test the functions updateDatabase and updateLogfile with your own inputs
    bookid = input("\nEnter book id: ") 
    whatToUpdate = input("Enter update status: ") 
    updateDatabase(bookid, whatToUpdate) 
    bookName = input("\nEnter book name: ") 
    bookStatus = input("Enter book status: ") 
    updateLogfile(bookid, bookName, bookStatus) 
    
