import os


def cwd():
    path = os.getcwd()
    print(f"The current working folder is {path}")
    for file in os.listdir(path):
        print (file)

def run():
    print("Processing...")
    cwd()