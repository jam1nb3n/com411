def search(filename):
    print("Searching...")
    sections = []
    books = []
    with open(filename) as file:
        for line in file:
            if (line.startswith("Section:")):
                lineList = line.split(":", 1)
                sections.append(lineList[1])
            else:
                books.append(line)
        print("Done!")
    return (sections, books)

def save(filename, data):
    print("Saving...")
    sections = data[0]
    books = data[1]

    sections = [remove_break(x) for x in sections]
    books = [remove_break(x) for x in books]

    with open(filename, "w") as file:
        file.write("Sections: " + ", ".join(sections)+"\n")
        file.write("Books: " + ", ".join(books))


def remove_break(x):
    if(x.find("\n") != 0):
        return x[:-1]
    else:
        return x

def run(): 
    data = search("data/files/txt/books.txt")
    save("data/files/txt/section-books.txt", data)

run()