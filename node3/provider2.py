import xmlrpc.client
import os
import socket
 
# Function to update file on server
def update_file(file_name, content, server, port):
   try:
       proxy = xmlrpc.client.ServerProxy(f"http://{server}:{port}/")
       # Update file on server
       proxy.update_file(file_name, content, server_path)
       print(f"File created successfully")
   except Exception as e:
       print(f"Error updating file on server {server}: {e}")

if __name__ == "__main__":
   server = 'localhost'
   port = '8003'
   current_working_directory = os.getcwd()
   server_path = os.path.join(current_working_directory, 'server_files3')
   file_name = input("Enter file name: ")
   file_content = input("Enter file content: ")
   update_file(file_name, file_content, server, port)