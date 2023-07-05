###bookreturn.py
import sys
sys.path.append('functions')
import functions.database as d


def returnBooks(bookToReturn):
    """takes a variable bookToReturn and attempts to return a book updating
    the logfile and database if successful. returns a 0, 1 or 2 dependent
    on the result of the book return:  
        bookToReturn = the id of the book being returned"""
    books = d.getBooks() 
    for i in range(0,len(books)):
        bookDetails = books[i].split(",")
        if bookToReturn == bookDetails[0]:
            if(int(bookDetails[5]) != 0):
                d.updateDatabase(bookToReturn, "0")
                d.updateLogfile(bookDetails[0], bookDetails[2], "0")
                return 0 #successfully returned
            else:
                return 1 #already been returned
    return 2 #book not found
    

if __name__=="__main__":
    #the following allows you to test the function returnBooks
    #should return 0 if book is already on loan, 1 if book is not already on loan, 2 if bookToReturn is >32 (out of database range)
    returningBook = str(input("enter book id: ")) 
    print(returnBooks(returningBook)) 
