question - 
Program a simple web server according to the following criteria.

1. You can use Python, Java, or C programming language.

2. If you are using Python you cannot use the built-in HTTPServer module.

3. The server should listen to port 2728.

4. Your server should be able to serve PHP files.

5. You need to comment the program clearly.

6. You should upload a  zip file named with your index number. The zip file should contain the following items.

      a sever source code.

      b htdocs folder which contains the following items.

               - index.php file (this is the default web page the browser displays when typed http://localhost:2728/

              - folders that contain web pages

      c) read-me file that contains instructions to execute the web server

________________________________________________________________________________________________________________________


 open the file folder in vs code

start the local server - command -       python .\server.py
(python <path to the server.py>)


     How this server works?

URL - http://localhost:2728/index.php can be used to access this website. -  index.php file 
(this is the default web page the browser displays when typed http://localhost:2728/)

when you type http://localhost:2728/ ,
server converts it as http://localhost:2728/index.php.



to add two numbers type url - http://localhost:2728/add_numbers_form.html in the browser.

this would take you to a html page where you can submit two numbers to add.

clicking add would take you to http://localhost:2728/add_numbers.php with the given two parameters.

or you can directly access said php file (http://localhost:2728/add_numbers.php) with two params for num1 and num2.

The URL should look like http://localhost:2728/add_numbers.php?num1=4&num2=3 if the given two numbers are 4 and 3.

this would show the results of addition.
________________________________________________________________________________________________________________________

                                                       
                                                       W.A.N.Umasha - 21002029 -assignment
                                                       ----------------------