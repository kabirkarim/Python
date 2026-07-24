import os
directory = "/"  # Replace with your desired directory path
contents = os.listdir(directory) #List all files and directories in the specified directory
for item in contents: #print each item in the directory
    print(item) 