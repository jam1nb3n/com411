import csv

def search(filename):
    print("Searching...")
    data = {}
    sectionList= []
    with open(filename) as file:
        for line in file:
            if (line.startswith("Section:")):
                lineList = line.split(":", 1)
                section = lineList[1]
                sectionList = []
                if (section.find("\n") != -1):
                    section = section[:-1]
            else:
                if (line.find("\n") != -1):
                    line = line[:-1]
                sectionList.append(line)
                data[section] = sectionList
    print("Done!")
    return data

def run():
    data = search("data/files/txt/books.txt")
    with open("data/files/txt/generated.csv", "w") as f:
        for key in data.keys():
            for x in data[key]:
                f.write(f"{key},{x}\n")



print(search("data/files/txt/books.txt"))
run()