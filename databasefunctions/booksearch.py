###booksearch.py
import sys
sys.path.append('functions')
import functions.database as d


def searchForID(id):
    """returns a list of books matching a given id:
        id = the book's unique id (string)"""
    books = d.getBooks() 
    searchedFor = []
    for i in range(0,len(books)): 
        bookDetails = books[i].split(",")
        if id == bookDetails[0]:
            searchedFor.append(bookDetails) 
    return(searchedFor)


def searchForISBN(isbn):
    """returns a list of books matching a given isbn:
        isbn = the book's isbn (string)"""
    books = d.getBooks()
    searchedFor = []
    for i in range(0,len(books)): 
        bookDetails = books[i].split(",")
        if isbn == bookDetails[1]:
            searchedFor.append(bookDetails) 
    return(searchedFor)


def searchForTitle(title):
    """returns a list of books matching a given title:
        title = the book's title (string)"""
    books = d.getBooks()
    searchedFor = []
    for i in range(0,len(books)): 
        bookDetails = books[i].split(",")
        if title.lower() == bookDetails[2].lower():
            searchedFor.append(bookDetails)
    return(searchedFor)


def searchForAuthor(author):
    """returns a list of books matching a given author:
        author = the book's author (string)"""
    books = d.getBooks()
    searchedFor = []
    for i in range(0,len(books)):
        bookDetails = books[i].split(",")
        if author.lower() == bookDetails[3].lower():
            searchedFor.append(bookDetails)
    return(searchedFor)


def searchForPurchasedate(purchaseDate):
    """returns a list of books matching a given purchase date:
        id = the book's purchase date (string) """
    books = d.getBooks()
    searchedFor = []
    for i in range(0,len(books)):
        bookDetails = books[i].split(",")
        if purchaseDate == bookDetails[4]:
            searchedFor.append(bookDetails) 
    return(searchedFor)


def searchForLoanedTo(loanedTo):
    """returns a list of books matching a given loan status:
        id = the book's on loan status, either a 0 or member id (string)"""
    books = d.getBooks() 
    searchedFor = []
    for i in range(0,len(books)):
        bookDetails = books[i].split(",")
        if (loanedTo+"\n")== bookDetails[5]:
            searchedFor.append(bookDetails) 
    return(searchedFor)


if __name__=="__main__":
    #the following allows you to test the search functions above
    idData = str(input("enter id: ")) 
    print(searchForID(idData)) 
    isbnData = str(input("\nenter isbn: ")) 
    print(searchForISBN(isbnData)) 
    titleData = str(input("\nenter title: ")) 
    print(searchForTitle(titleData)) 
    authorData = str(input("\nenter author: ")) 
    print(searchForAuthor(authorData)) 
    purchaseData = str(input("\nenter purchase date: ")) 
    print(searchForPurchasedate(purchaseData))
    onLoanData = str(input("\nenter loan status: ")) 
    print(searchForLoanedTo(onLoanData)) 
