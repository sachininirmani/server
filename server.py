import socket
import os
import urllib.parse

import gzip
import zlib


# Set the port to 2728
PORT = 2728

# Define the document root directory
DOCUMENT_ROOT = "htdocs"


def handle_client(client_socket):
    # Receive the client's request
    request_data = client_socket.recv(4096).decode("utf-8")
    

    print(f"\n\nrequest_data {request_data}")

    # Extract the requested file path
    request_lines = request_data.split("\r\n")
    print(f"\n\n\nrequest_lines -   {request_lines}")
    request_line = request_lines[0]
    print(f"\n\n\nrequest_line -   {request_line}")

    path = request_line.split(" ")[1]
    request_type = request_line.split(" ")[0]

    print(f"path -   {path}")
    print(f"request_type - {request_type}")

    # Map '/' to the index.php file
    if path == "/":
        path = "/index.php"

    # Get the file extension
    file_extension = os.path.splitext(path)[1].split("?")[0]
    print(f"file extention  - {file_extension}")
     # Get the file location 
    file_location = f"{DOCUMENT_ROOT}{path.split('?')[0]}"
    print(f"file location  - {file_location}")

    


    try:
        if file_extension == ".php":
            print("this is a php file")
            # Extract query parameters from the URL
            query_params = urllib.parse.parse_qs(urllib.parse.urlparse(path).query)
            print(f"query_params - {query_params}")
            num1 = query_params.get('num1', [''])[0]
            print(num1)
            num2 = query_params.get('num2', [''])[0]
            print(num2)

            try:
                if request_type == "GET" and len(path.split("?")) == 1:
                    # Construct the command to execute the PHP script with parameters
                    php_command = f"php -f {DOCUMENT_ROOT}{path} "

                    #php_command = f"php -f {DOCUMENT_ROOT}{path}" - this doesn't work -
                    # https://www.igorkromin.net/index.php/2017/12/07/how-to-pass-parameters-to-your-php-script-via-the-command-line/

                    print(php_command)
                    print("run")

                    # Run the PHP script and capture its output
                    php_output = os.popen(php_command).read()



                if request_type == "GET" and len(path.split("?")) > 1:

                    #check if there are params    params = ["num1=5", "num2=3"]
                    params = path.split("?")[1].split("&")  

                    print(params)
                    if len(params) > 1:         # create a PHP Associative Array
                        get_or_post_arr = f'$_GET_or_POST = array("{params[0].split("=")[0]}" => {params[0].split("=")[1]}, "{params[1].split("=")[0]}" => {params[1].split("=")[1]});'
                        print(get_or_post_arr)
                    else:
                        print("error - Two numbers are needed")


                    php_text = "<?php " + get_or_post_arr + "\n $_GET = $_GET_or_POST; ?> "

                    print(php_text)
                    
                    file_location = f"{DOCUMENT_ROOT}{path.split('?')[0]}"
                    with open(file_location, 'r') as php_file:
                        php_code = php_file.read()
                        print(php_code)
                    
                    temp_php = f"{DOCUMENT_ROOT}/temp/temp.php"

                    with open(temp_php, 'w') as php_file:
                            php_file.write(php_text + php_code)

                    php_command = f"php -f {temp_php}"
                    php_output = os.popen(php_command).read()

                    print("php output")
                    print(php_output)

                

                if request_type == "POST":
                    print("go")
                    
        
                    params = request_lines[request_lines.index('')+1].split("&")   ####

                    if len(params) > 1:         # create a PHP Associative Array
                        get_or_post_arr = f'$_GET_or_POST = array("{params[0].split("=")[0]}" => {params[0].split("=")[1]}, "{params[1].split("=")[0]}" => {params[1].split("=")[1]});'
                        print(get_or_post_arr)
                    else:
                        print("error - Two numbers are needed")

                    php_text = "<?php " + get_or_post_arr + "\n $_POST = $_GET_or_POST; ?> "
                    
                    print(php_text)
                    
                    file_location = f"{DOCUMENT_ROOT}{path.split('?')[0]}"
                    with open(file_location, 'r') as php_file:
                        php_code = php_file.read()
                        print(php_code)
                    
                    temp_php = f"{DOCUMENT_ROOT}/temp/temp.php"

                    with open(temp_php, 'w') as php_file:
                            php_file.write(php_text + php_code)

                    php_command = f"php -f {temp_php}"
                    php_output = os.popen(php_command).read()

                    print("php output")
                    print(php_output)
 
            
            
            except:
                # Construct the command to execute the PHP script with parameters
                php_command = f"php -f {DOCUMENT_ROOT}{path.split('?')[0]} {num1} {num2}"

                #php_command = f"php -f {DOCUMENT_ROOT}{path}" - this doesn't work -
                # https://www.igorkromin.net/index.php/2017/12/07/how-to-pass-parameters-to-your-php-script-via-the-command-line/

                print(php_command)
                print("run")

                # Run the PHP script and capture its output
                php_output = os.popen(php_command).read()

            
            
            response_headers = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
            response_content = php_output.encode("utf-8")
        else:
            # Open and read the requested file   - htdocs/add_numbers_form.html
            with open(f'{DOCUMENT_ROOT}{path}', "rb") as file:
                # this calls http://localhost:2728/htdocs/add_numbers_form.html in browser
                response_content = file.read()
                #print(response_content)
                response_headers = f"HTTP/1.1 200 OK\nContent-Type: text/html \nContent-Length: {len(response_content)}\n\n"
    except FileNotFoundError:
        # Handle 404 Not Found error
        response_content = b"Not Found"
        response_headers = "HTTP/1.1 404 Not Found\nContent-Type: text/plain\nContent-Length: 9\n\n"
    
    # Send the response to the client
    client_socket.send(response_headers.encode("utf-8"))
    client_socket.send(response_content)
    
    # Close the client socket
    client_socket.close()

def main():
    # Create a socket to listen on the specified port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", PORT))
    server_socket.listen(10)
    print(os.path)

    print(f"Server is running on port {PORT}")

    while True:
        # Accept incoming client connections
        try:
            client_socket, _ = server_socket.accept()

        # Handle each client request in a separate thread or process if needed
            handle_client(client_socket)
        except:
            continue

if __name__ == "__main__":
    main()
