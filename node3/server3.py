from xmlrpc.server import SimpleXMLRPCServer
import os
import sys
import xmlrpc
 
NEAREST_SERVER = ['localhost:8002']
 
# Function to check if file exists in server's file system
def file_exists(file_path):
   return os.path.isfile(file_path)
 
# Function to retrieve file content
def get_file_content(file_path):
   with open(file_path, 'r') as file:
       content = file.read()
   return content
 
# RPC Server class
class FileServerRPC:
   def __init__(self, server_id, file_directory):
       self.server_id = server_id
       self.file_directory = file_directory
  
   def get_file(self, file_name, client_local_path):
       file_path = os.path.join(self.file_directory, file_name)
       if file_exists(file_path):
           print(f"\nFile {file_name} is found in server {self.server_id}:{port}")
           file_content = get_file_content(file_path) + "\nServer - " + self.server_id + ":" + str(port)
       else:
           print(f"\nFile {file_name} not found in server {self.server_id}:{port}")
           print(f"Forwarding request to nearest server {NEAREST_SERVER[0]}")
           client = xmlrpc.client.ServerProxy(f'http://{NEAREST_SERVER[0]}')
           file_content = client.get_file(file_name, client_local_path)
           if file_content != "File not found":
               self.update_file(file_name, file_content, self.file_directory)
       return file_content
 
   def update_file(self, file_name, content, pathname):
       file_path = os.path.join(pathname, file_name)
       with open(file_path, 'w') as file:
           file.write(content)
       return "File updated successfully"
 
 
# Start RPC Server
def start_rpc_server(server_id, port, file_directory):
    server = SimpleXMLRPCServer((address, port))
    server.register_instance(FileServerRPC(server_id, file_directory))
    print(f"Server {server_id} listening on port {port}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)
 
if __name__ == "__main__":
   address = 'localhost'
   port = 8003
   current_working_directory = os.getcwd()
   server_local_path = os.path.join(current_working_directory, 'server_files3')
   start_rpc_server(address, port, server_local_path)