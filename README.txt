Corben Sayer Introduction to Programming Coursework
Library Management System

Inside the package folders databasefunctions and functions you will see additional database.txt s and logfile.txt s.
These files are only edited when you directly run the python files in their respective packages to allow you to test
the functions inside this packages individually. The actual database.txt and logfile.txt that are used when main.py 
is run are the ones inside this folder which contains main.py and this README.txt.

When using the library management system the window can resize to only display what is needed at any given moment.
You may find that if you are using a smaller screen sometimes the window will expand and you might not be seeing 
everything that is meant to be show. To fix this just fullscreen the window and you should be able to see everything.

When you have the library management system open pressing one of the menu buttons on the side will change to that
page which you are currently viewing. If you click a button corresponding to a page you are already on the page
will refresh to how it looked when you first clicked on it before you started interacting with it.

How Searching Should be Formatted to return what you want:
ID: a number e.g. 4
ISBN: a 13 digit number  e.g. 9780552773898
Title: a string, not caps sensitive but character sensitive e.g. F. Scott Fitzgerald but not F Scott Fitzgerald
Author: a string, not caps sensitive but character sensitive e.g. j.r.r. tolkien but not jrr tolkien
Purchase Date: a string in the format yyyy-mm-dd e.g. 2019-06-11
Loaned To: either a four digit member id e.g. 1234 or a 0
