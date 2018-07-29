letter_dict = {}

string = input("Enter a string: ")
letter_list = []

for letter in string:
    if letter.isupper():
        letter = letter.lower()
    if letter.isalpha():
        letter_list.append(letter)

letter_list.sort()

for letter in letter_list:
    if letter in letter_dict:
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1
for letter in letter_dict:
    print(letter, letter_dict[letter])
