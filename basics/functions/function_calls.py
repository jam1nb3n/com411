def in_box(word):
    print("**"+(len(word)*"*")+"**")
    print(f"* {word} *")
    print("**"+(len(word)*"*")+"**")

def in_lowercase(word):
    print(word.lower())

def in_uppercase(word):
    print(word.upper())

def mirrored(word):
    print(word[::-1])

def repeat(word):
    i = int(input("How many times do you want to display the word: "))
    while (i != 0):
        if (i % 2 == 0):
            in_lowercase(word)
        else:
            in_uppercase(word)
        i -= 1

def run():
    wordInput = input("Please enter a word: ")
    print("""
        1) Display in a Box – display the word in an ascii art box
        2) Display Lower-case – display the word in lower-case e.g. hello
        3) Display Upper-case – display the word in upper-case e.g. HELLO
        4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
        5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.
    """)
    selectFunction = int(input("Please enter a menu number: "))
    if (selectFunction == 1):
        in_box(wordInput)
    elif (selectFunction == 2):
        in_lowercase(wordInput)
    elif (selectFunction == 3):
        in_uppercase(wordInput)
    elif (selectFunction == 4):
        mirrored(wordInput)
    elif (selectFunction == 5):
        repeat(wordInput)


run()