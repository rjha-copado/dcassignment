import xmlrpc.client
import os

def request_file(file_name, server, client_local_path):
	try:
		proxy = xmlrpc.client.ServerProxy(f"http://{server}/")
		file_content = proxy.get_file(file_name, client_local_path)
		if file_content != "File Not Found":
			print("\nFile Found")
			print("\nFile being downloaded to nearer local machine")
			proxy.update_file(file_name, file_content, client_local_path)
	except Exception as e:
		print("\nError accessing server {server}: {e}\n")
		return "\n File not found on any of the nearest servers"

if __name__ == "__main__":
	server = "localhost:8003"
	current_working_directory = os.getcwd()
	client_local_path = os.path.join(current_working_directory, 'client_files4')
	file_name = input('Enter file name: ')
	file_content = request_file(file_name, server, client_local_path)
	print(file_content)
	print("\n")