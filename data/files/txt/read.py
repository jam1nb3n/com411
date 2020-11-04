def search(filename): #define filename
    print("Searching...")
    with open(filename) as file: #open file as file while running
        for line in file:
            print(f"Looked in {line}")
        print("...Done!")

def run():
    search("data/files/txt/locations.txt")

run()