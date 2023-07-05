###bookcheckout.py
import sys
sys.path.append('functions')
import functions.database as d


def validMember(userid):
    """takes a variable userid and returns true if it is valid. otherwise false
    userid = the id being checked if valid or not"""
    try:
        userid = int(userid) #checks if string can be converted into an integer
    except ValueError:
        return False
    if userid>999 and userid<10000: #checks userid is only 4 digits long
        return True
    else:
        return False


def checkoutBooks(bookToWithdraw, memberid):
    """takes two variables bookToWithdraw and memeberid and checks out a book 
    updating the log file and text file with the relevant information and
    returning a 0, 1 or 2 dependent on the result of the checkout:
        bookToWithdraw = the book being checked outs unique id 
        memberid = the id of the person checking the book out"""
    books = d.getBooks() 
    for i in range(0,len(books)): 
        bookDetails = books[i].split(",")
        if bookToWithdraw == bookDetails[0]: 
            if(int(bookDetails[5]) == 0):
                d.updateDatabase(bookToWithdraw, memberid)
                d.updateLogfile(bookDetails[0], bookDetails[2], "1")
                return 0 #successfully checked out
            else:
                return 1 #already on loan
    else:
        return 2 #book not found
        

if __name__=="__main__":
    #the following allows you to test the function member id
    #should return true if a valid memberid otherwise return false
    memberid = input("Enter memberid: ") 
    print(validMember(memberid)) 

    #the following allows you to test the function checkoutBooks
    #should return 0 if book is not already on loan, 1 if book is already on loan, 2 if bookToWithdraw is >32 (out of database range)
    memberid = input("\nEnter memberid: ") 
    bookid = input("Enter bookid: ") 
    print(checkoutBooks(bookid, memberid)) 
    