# eagoradb
This is a fully functional database system writen in Django 2.0, HTML/CSS and Bootstrap 4.1.
It was made during the 2018-19 academic year for the Databases course of ECE AUTH.

To install django, you need to have python3 installed and pip.
Run makefile -f install, in order to install django at your computer.
To run the database, run makefile -f runserver and connect via a browser to
localhost:8080/database/.


This is the home page of the database application. In the top bar, there are links to find stores and
products that our database provides. On the top right, you can create a client user to be able to make
an order. You can also see the details of a product, where it is sold and in what price.
You can see the details of a store and make an order. If you are not logged in, you will be redirected
to the login page. Then you will be able to make an order and keep track of them.

This is a proof of concept for a real store-product managing system. It contains several important views,
such as find products, find stores, product's details, store's details, make an order view, check orders
and account managing views.



P.S. If makefile doesn't work, open a cmd and type 'pip install Django' to install django package
and 'django manage.py runserver' in the same folder as this project in order to run the application.
