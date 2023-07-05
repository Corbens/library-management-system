###bookweed.py
import sys
sys.path.append('functions')
import functions.database as d
import datetime


def weedBooks():
    """returns a list of books that are recommended to be removed
    based on their log data."""
    logs = d.getLogs()
    books = d.getBooks()
    currentDate = datetime.date.today()
    daysAllowed = 120 #sets the amount of days of unuse a book is allowed before it will be recommended to be removed
    usedBooks = [] #usedBooks = list of books used less than daysAllowed days ago
    daysSince = [] #daysSince = list of books used longer than daysAllowed days ago with the days since last used
    booksToBeWeeded = []
    booksToBeWeededDays = []

    for i in range(0, len(logs)): #adds data to usedBooks and daysSince according to the logfile dates
        logDetails = logs[i].split(",")
        logDate = logDetails[0]
        lastUsedDelta = ((datetime.datetime.today()) - (datetime.datetime.strptime(logDate, "%Y-%m-%d"))).days
        if lastUsedDelta < daysAllowed:
            usedBooks.append(logDetails[2])
        else:
            daysSince.append(logDetails[2]+";"+str(lastUsedDelta))
    daysSince.reverse()

    for i in range(0, len(books)): #adds data to the list booksToBeWeeded based on all books found in the database but not in the usedBooks list
        toBeWeeded = True
        bookDetails = books[i].split(",")
        for j in range(0, len(usedBooks)):
            if bookDetails[2] == usedBooks[j]:
                toBeWeeded = False
                break
        if toBeWeeded == True:
            booksToBeWeeded.append(bookDetails)

    for i in range(0, len(booksToBeWeeded)): #adds data to the the list booksToBeWeededDays of all the books recomended to be weeded plus the days since they were last used
        bookDetails = booksToBeWeeded[i]
        for j in range(0, len(daysSince)):
            daysSinceDetails = daysSince[j].split(";")
            if bookDetails[2] == daysSinceDetails[0]:
                bookDetails.append(daysSinceDetails[1])
                booksToBeWeededDays.append(bookDetails)
                break
    print("successfully collected books to be weeded")    
    return booksToBeWeededDays


def getGraphData():
    """returns a list of the data needed to plot a graph of book titles
    against days since they were last checked out"""
    weedingData = weedBooks() #gets the raw data
    sortedData = [] 
    for i in range(0, len(weedingData)): #sort weedingData into a list of just the days since use and book titles
        tempList = []
        tempList.append(weedingData[i][2])
        tempList.append(weedingData[i][6])
        sortedData.append(tempList)
    sortedData.sort(key=lambda x: x[1]) #sort the data based on the days since last used

    bookTitles = [] 
    bookDays = []
    for i in range(0, len(sortedData)): #adds data to a list of bookTitles and a list of bookDays
        bookTitles.append(sortedData[i][0])
        bookDays.append(sortedData[i][1])

    returnData = [] #creates a list of two lists with all the data needed to plot a graph
    returnData.append(bookTitles)
    returnData.append(bookDays)
    print("successfully collected graph data")
    return returnData


if __name__ == "__main__":
    #the following allows you to test the functions weedBooks and getGraphData
    print(weedBooks())
    print("\n")
    print(getGraphData())
