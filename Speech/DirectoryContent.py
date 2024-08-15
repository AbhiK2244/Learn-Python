import os

directory_path = "C:/Users/KIIT/OneDrive/Desktop/Python/Tutorial"

contents = os.listdir(directory_path)

for item in contents:
    print(item)