###menu.py
import sys
sys.path.append('databasefunctions')
sys.path.append('databasefunctions/functions')
import databasefunctions.booksearch as bs
import databasefunctions.bookreturn as br
import databasefunctions.bookcheckout as bc
import databasefunctions.bookweed as bw

from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



###--------------------------###
###-----Search Functions-----###
###--------------------------###

def bookSearch():
    """loads the book search page"""
    for widget in taskFrame.winfo_children(): 
        widget.destroy() #clears the page of any widgets left on the screen from previous pages

    inputSearchFrame = LabelFrame(taskFrame, text="Search for Books", padx=8, pady=8, bd=0)
    inputSearchFrame.grid(row=0) #draws a frame for all widgets the user interacts with 
    
    global outputSearchFrame #frame is global so updateSearch() can access it
    outputSearchFrame = LabelFrame(taskFrame, padx=8, pady=8, bd=0)
    outputSearchFrame.grid(row=1) #draws a frame for all widgets that display the search results

    criteriaLabel = Label(inputSearchFrame, text="Choose Search Criteria", padx=8)
    criteriaLabel.grid(row=1,column=0)

    global v #creates a global variable v so that updateSearch() can access it
    v = IntVar()
    v.set(1)
    rad1 = Radiobutton(inputSearchFrame, text="Book ID", indicatoron=0, variable=v, value=1, padx=0)
    rad2 = Radiobutton(inputSearchFrame, text="Book ISBN", indicatoron=0, variable=v, value=2, padx=0)
    rad3 = Radiobutton(inputSearchFrame, text="Book Title", indicatoron=0, variable=v, value=3, padx=0)
    rad4 = Radiobutton(inputSearchFrame, text="Book Author", indicatoron=0, variable=v, value=4, padx=0)
    rad5 = Radiobutton(inputSearchFrame, text="Purchase Date", indicatoron=0, variable=v, value=5, padx=0)
    rad6 = Radiobutton(inputSearchFrame, text="Loaned To", indicatoron=0, variable=v, value=6, padx=0)
    rad1.grid(row=1,column=1)
    rad2.grid(row=1,column=2)
    rad3.grid(row=1,column=3)
    rad4.grid(row=1,column=4)
    rad5.grid(row=1,column=5)
    rad6.grid(row=1,column=6)

    global bookCriteria #cretes a global variable bookCriteria so updateSearch() can access it
    bookCriteria = Entry(inputSearchFrame)
    bookCriteria.grid(row=2,column=0)
    confirmButton = Button(inputSearchFrame, text="Search", command=updateSearch)
    confirmButton.grid(row=2, column=1)


def updateSearch():
    """loads search results"""
    for widget in outputSearchFrame.winfo_children(): #removes any old search results
        widget.destroy()

    if v.get() == 1:
        matchingBooks = bs.searchForID(bookCriteria.get())
    elif v.get() == 2:
        matchingBooks = bs.searchForISBN(bookCriteria.get())
    elif v.get() == 3:
        matchingBooks = bs.searchForTitle(bookCriteria.get())
    elif v.get() == 4:
        matchingBooks = bs.searchForAuthor(bookCriteria.get())
    elif v.get() == 5:
        matchingBooks = bs.searchForPurchasedate(bookCriteria.get())
    elif v.get() == 6:
        matchingBooks = bs.searchForLoanedTo(bookCriteria.get())

    if(matchingBooks == []):
        noBooks = Label(outputSearchFrame, text="No books found")
        noBooks.grid(row=0, column=0)
    else: #creates headings for all the book details
        bookidLabel = Label(outputSearchFrame, text="Book ID:", padx=2)
        bookidLabel.grid(row=0, column=0)
        bookisbnLabel = Label(outputSearchFrame, text="Book ISBN:", padx=2)
        bookisbnLabel.grid(row=0, column=1)
        booktitleLabel = Label(outputSearchFrame, text="Book Title:", padx=2)
        booktitleLabel.grid(row=0, column=2)
        bookauthorLabel = Label(outputSearchFrame, text="Book Author:", padx=2)
        bookauthorLabel.grid(row=0, column=3)
        bookpurchasedateLabel = Label(outputSearchFrame, text="Date of Purchase:", padx=2)
        bookpurchasedateLabel.grid(row=0, column=4)
        bookloanedtoLabel = Label(outputSearchFrame, text="Loaned To:", padx=2)
        bookloanedtoLabel.grid(row=0, column=5)
        for i in range(0,len(matchingBooks)): #outputs all the books details that match the search
            bookid = Label(outputSearchFrame, text=matchingBooks[i][0])
            bookid.grid(row=((i*1)+1), column=0)
            bookisbn = Label(outputSearchFrame, text=matchingBooks[i][1])
            bookisbn.grid(row=((i*1)+1), column=1)
            booktitle = Label(outputSearchFrame, text=matchingBooks[i][2])
            booktitle.grid(row=((i*1)+1), column=2)
            bookauthor = Label(outputSearchFrame, text=matchingBooks[i][3])
            bookauthor.grid(row=((i*1)+1), column=3)
            purchasedate = Label(outputSearchFrame, text=matchingBooks[i][4])
            purchasedate.grid(row=((i*1)+1), column=4)
            loanedto = Label(outputSearchFrame, text=matchingBooks[i][5])
            loanedto.grid(row=((i*1)+1), column=5)



###----------------------------###
###-----Checkout Functions-----###
###----------------------------###

def bookCheckout():
    """loads the book checkout page"""
    for widget in taskFrame.winfo_children():
       widget.destroy() #clears the page of any widgets left on the screen from previous pages

    inputCheckoutFrame = LabelFrame(taskFrame, text="Checkout Books", padx=8, pady=8, bd=0)
    inputCheckoutFrame.grid(row=0) #draws a frame for all widgets the user interacts with to enter their member id

    global validateCheckoutFrame #frame is global so that validateCheckout() can acess it
    validateCheckoutFrame = LabelFrame(taskFrame, padx=8, pady=8, bd=0)
    validateCheckoutFrame.grid(row=1) #draws a frame for all the widgets that respond to the members book id

    global resultsCheckoutFrame #frame is global so that doCheckout() can access it
    resultsCheckoutFrame = LabelFrame(taskFrame, padx=8, pady=8, bd=0)
    resultsCheckoutFrame.grid(row=2) #draws a frame for all the widgets that display the success of the book checkout

    memberidLabel = Label(inputCheckoutFrame, text="Enter Member ID") 
    memberidLabel.grid(row=0, column=0)
    global memberidInput #creates a global variable memberidInput so that validateCheckout() can access it
    memberidInput = Entry(inputCheckoutFrame) 
    memberidInput.grid(row=0, column=1)
    continueButton = Button(inputCheckoutFrame, text="Continue", command=validateCheckout) 
    continueButton.grid(row=0, column=2)


def validateCheckout():
    """loads the widgetss in response of a memberid being entered"""
    for widget in validateCheckoutFrame.winfo_children():
        widget.destroy() #removes any old checkout data
    for widget in resultsCheckoutFrame.winfo_children():
        widget.destroy() #removes any old checkout data

    if(bc.validMember(memberidInput.get())): #check if member id is valid, if so allow for a bookid to be entered
        bookToWithdrawLabel = Label(validateCheckoutFrame, text="Enter Book ID")
        bookToWithdrawLabel.grid(row=0, column=0)
        global bookToWithdrawInput # creates a global variable bookToWithdrawInput so that doCheckout() can access it
        bookToWithdrawInput = Entry(validateCheckoutFrame)
        bookToWithdrawInput.grid(row=0, column=1)
        continueButton = Button(validateCheckoutFrame, text="Continue", command=doCheckout) 
        continueButton.grid(row=0, column=3)
    else: #if member id is not valid, ask for a valid id to be entered
        bookToWithdrawLabel = Label(validateCheckoutFrame, text="Not Valid\nPlease Enter a Valid Member ID")
        bookToWithdrawLabel.grid(row=0, column=0)    


def doCheckout():
    """loads the widgets in response of an attempted book checkout"""
    for widget in resultsCheckoutFrame.winfo_children():
        widget.destroy() #removes any old checkout data

    checkoutStatus = bc.checkoutBooks(bookToWithdrawInput.get(), memberidInput.get()) #attempt to checkout a book
    if checkoutStatus == 0: #display relevant message based on success of checkout
        checkoutStatusLabel = Label(resultsCheckoutFrame, text="Book Successfully Checked Out")
        checkoutStatusLabel.grid(row=1,columnspan=3)
    elif checkoutStatus == 1:
        checkoutStatusLabel = Label(resultsCheckoutFrame, text="Checkout Failed\nBook Already On Loan")
        checkoutStatusLabel.grid(row=1,columnspan=3)
    elif checkoutStatus == 2:
        checkoutStatusLabel = Label(resultsCheckoutFrame, text="Checkout Failed\nBook Not Found")
        checkoutStatusLabel.grid(row=1,columnspan=3)



###--------------------------###
###-----Return Functions-----###
###--------------------------###

def bookReturn():
    """loads the book return page"""
    for widget in taskFrame.winfo_children():
       widget.destroy() #clears the page of any widgets left on the screen from previous pages

    inputReturnFrame = LabelFrame(taskFrame, text="Return Books", padx=8, pady=8, bd=0)
    inputReturnFrame.grid(row=0) #draws a frame for all the widgets the user interacts with to return the book

    global outputReturnFrame #frame is global so that doReturn() can access it
    outputReturnFrame = LabelFrame(taskFrame, padx=8, pady=8, bd=0)
    outputReturnFrame.grid(row=1) #draws a frame for all the widgets that display the success of the book return

    bookidLabel = Label(inputReturnFrame, text="Enter Book ID") 
    bookidLabel.grid(row=0, column=0)
    global bookToReturnInput #creates a global variable bookToReturnInput so that doReturn() can access it
    bookToReturnInput = Entry(inputReturnFrame) 
    bookToReturnInput.grid(row=0, column=1)
    continueButton = Button(inputReturnFrame, text="Continue", command=doReturn) 
    continueButton.grid(row=0, column=2)


def doReturn():
    """loads widgets in response to an attempted book return"""
    for widget in outputReturnFrame.winfo_children():
        widget.destroy() #removes any old return results
    
    returnStatus = br.returnBooks(bookToReturnInput.get()) #attempt to return a book
    if returnStatus == 0: #display relevant message based on success of book return
        returnStatusLabel = Label(outputReturnFrame, text="Book Successfully Returned")
        returnStatusLabel.grid(row=1,columnspan=3)
    elif returnStatus == 1:
        returnStatusLabel = Label(outputReturnFrame, text="Return Failed\nBook Already Returned")
        returnStatusLabel.grid(row=1,columnspan=3)
    elif returnStatus == 2:
        returnStatusLabel = Label(outputReturnFrame, text="Return Failed\nBook Not Found")
        returnStatusLabel.grid(row=1,columnspan=3)



###---------------------------###
###-----Weeding Functions-----###
###---------------------------###

def bookWeed():
    """loads the book weed page"""
    for widget in taskFrame.winfo_children():
       widget.destroy() #clears the page of any widgets left on the screen from previous pages

    weedFrame = LabelFrame(taskFrame, text="Weed Books", padx=8, pady=8, bd=0)
    weedFrame.grid(row=0, column=0) #draws a frame for the widgets the user interacts with

    global weedOutputFrame #frame is global so that doWeeding() can access it
    weedOutputFrame = LabelFrame(weedFrame, padx=8, pady=8, bd=0)
    weedOutputFrame.grid(row=2, column=0) #draws a frame for the widgets that show the weeding data

    bookweedButton = Button(weedFrame, text="Weed Books", command=doWeeding)
    bookweedButton.grid(row=0, column=0)

    global drawGraphFrame #frame is global so that drawGraph() can access it
    drawGraphFrame = LabelFrame(weedFrame, padx=8, pady=8, bd=0)
    drawGraphFrame.grid(row=2, column=1)

    drawGraphButton = Button(weedFrame, text="Draw Graph",command=drawGraph)
    drawGraphButton.grid(row=1, column=0)


def doWeeding():
    """loads all the widgets that display the result of a book weed"""
    for widget in weedOutputFrame.winfo_children():
        widget.destroy() #removes any old weeeding results

    bookisbnLabel = Label(weedOutputFrame, text="Book ISBN:", padx=2)
    bookisbnLabel.grid(row=0, column=0)
    booktitleLabel = Label(weedOutputFrame, text="Book Title:", padx=2)
    booktitleLabel.grid(row=0, column=1)
    bookauthorLabel = Label(weedOutputFrame, text="Book Author:", padx=2)
    bookauthorLabel.grid(row=0, column=2) 
    dayssinceLabel = Label(weedOutputFrame, text="Days Since Last Use:",padx=2)
    dayssinceLabel.grid(row=0, column=3)

    booksToBeWeeded = bw.weedBooks()
    for i in range(0,len(booksToBeWeeded)): #outputs all the books that need to be weeded
        bookisbn = Label(weedOutputFrame, text=booksToBeWeeded[i][1])
        bookisbn.grid(row=((i*1)+1), column=0)
        booktitle = Label(weedOutputFrame, text=booksToBeWeeded[i][2])
        booktitle.grid(row=((i*1)+1), column=1)
        bookauthor = Label(weedOutputFrame, text=booksToBeWeeded[i][3])
        bookauthor.grid(row=((i*1)+1), column=2)
        dayssince = Label(weedOutputFrame, text=booksToBeWeeded[i][6])
        dayssince.grid(row=((i*1)+1), column=3)
    

def drawGraph():
    """draws a bar chart based on data from bookweed"""
    graphData = bw.getGraphData() #get data
    bookTitles = graphData[0]
    bookDays = graphData[1]

    f = Figure(figsize=(20,10), dpi=60) #creates a figure to contain the barchart
    ax = f.add_subplot(111) 
    ax.barh(bookTitles,bookDays, height=0.4)
    ax.xaxis.label.set_fontsize(12)
    ax.yaxis.label.set_fontsize(12)
    for label in (ax.get_xticklabels()):
        label.set_fontsize(11)
    for label in (ax.get_yticklabels()):
        label.set_fontsize(7)
    ax.set_ylabel("Book Title")
    ax.set_xlabel("Days Since Last Used")
    ax.set_title("Books To Be Weeded", fontsize=16)
    canvas = FigureCanvasTkAgg(f, master=drawGraphFrame) #creates a canvas containing the figure f in the drawGraphFrame frame 
    canvas.get_tk_widget().grid(row=0, column=0) #draws the canvas



###-----------------------------------###
###-----Stuff Drawn on Menu Start-----###
###-----------------------------------###
    
root = Tk()
root.title("Library Management System")

taskFrame = LabelFrame(root, padx=20, pady=20, bd=4)
taskFrame.grid(row=0, column=1, columnspan=7, rowspan=5) #draws a frame which holds all the frames for the different pages

msg = Label(taskFrame, text="Welcome to the library management system\nUse the buttons to the left to navigate\nhelp about how to use in readme.txt, e.g. search formats")
msg.grid(row=0, column=0) #draws an introduction message

optionFrame = LabelFrame(root, padx=8, pady=8, bd=4)
optionFrame.grid(row=0, column=0, columnspan=1) #draws a frame containing all the buttons to navigate the different pages
bookSearchButton = Button(optionFrame, text="Search for Books", command = bookSearch)
bookSearchButton.grid(row=0, column=0, ipadx=30, ipady=25)
bookCheckoutButton = Button(optionFrame, text="Checkout Books", command = bookCheckout)
bookCheckoutButton.grid(row=1, column=0, ipadx=31, ipady=25)
bookReturnButton = Button(optionFrame, text="Return Books", command = bookReturn)
bookReturnButton.grid(row=2, column=0, ipadx=39, ipady=25)
bookWeedButton = Button(optionFrame, text="Weed Books", command = bookWeed)
bookWeedButton.grid(row=3, column=0, ipadx=41, ipady=25)
quitButton = Button(optionFrame, text="Quit", command = root.destroy)
quitButton.grid(row=4, column=0, ipadx=62, ipady=25)

#all functions have been tested and are working
root.mainloop()
