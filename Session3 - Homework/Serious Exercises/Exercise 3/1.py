from random import choice

keywords = ["key","dog","plane","car","ship","sheep"]

end = False
while not end:
    keyword = list(choice(keywords))
    for i in range(len(keyword)):
        letter = choice(keyword)
        print(letter)
        keyword.remove(letter,end = " ")
    answer = input("Your answer, enter X to stop? ")
    if answer == keyword:
        print("Hura")
    elif (answer == "x" or answer == "X"):
        end = True
