from django.shortcuts import render, redirect
import mysql.connector as sql  # Import MySQL connector to interact with the MySQL database
from django.http import HttpResponseRedirect  # Import for redirecting to different views
from django.contrib import messages  # Import for displaying messages to the user
# Global variables to store user credentials (not recommended for production)
id = ''
pwd = ''
# View function to handle user login
def Login_View(request):
    global id, pwd
    # Check if the request is a POST (form submission)
    if request.method == "POST":
        # Establish a connection to the MySQL database
        m = sql.connect(host='localhost', user='root', passwd='Krrish1234', database='file_management')
        cursor = m.cursor()

        # Retrieve data from the POST request
        d = request.POST
        for key, value in d.items():
            if key == "ID":
                id = value  # Store the user ID
            if key == "password":
                pwd = value  # Store the password
               
        # SQL query to check if the user credentials match any record in the Officers table
        ce = "select * from Officers where Officers_ID='{}' and Password='{}'".format(id, pwd)
        cursor.execute(ce)
        t = tuple(cursor.fetchall())  # Fetch the results and convert to a tuple
        # If the user is a department officer (ID starts with 'T')
        if (id[1] == "T"):
            if t == ():  # If no matching records are found
                messages.info(request, 'Either Id or Password is invalid !')  # Display an error message
            else:
                # Redirect to the department dashboard with the officer ID and department code
                return HttpResponseRedirect('/depart/{}/DT{}'.format(id, id[2]))
        else:
            if t == ():  # If no matching records are found
                messages.info(request, 'Either Id or Password is invalid !')  # Display an error message
            else:
                # Redirect to the super dashboard with the officer ID
                return HttpResponseRedirect('/super/{}'.format(id))    
    # Render the login page template if the request is not POST
    return render(request, 'Login_View.html')
