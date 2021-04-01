To run server, navigate to /danjowildcard/ and type the command (OS dependent)
**py manage.py runserver 80**

Current configuration:
  /login - login page
  /calculator - calculator page

This is a very sparse html website that calculates wildcard masks and addresses

Code for calculations are located in calculator.py

HTML is in /templates/

Pretty much it

Changelog 2021-04-01
-Added a login page. The login page is a simple POST form that returns an HTTPResponse either successful or unsuccessful for the login.
