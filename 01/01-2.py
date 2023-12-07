lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break


numbers_list = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

first = ''
last = ''
sums = 0


for line in lines:
    for index, character in enumerate(line):
        if character.isnumeric() and first == '':
            first = character
        elif first == '':
            for word in numbers_list:
                if word[0] == character:
                    complete_word = line[index:index+len(word)]
                    print(complete_word, word)
                    if word == complete_word:
                        first = str(numbers_list.index(word) +  1)
        elif character.isnumeric():
            last = character
        else:
            for word in numbers_list:
                if word[0] == character:
                    complete_word = line[index:index+len(word)]
                    print(complete_word, word)
                    if word == complete_word:
                        last= str(numbers_list.index(word) +  1)

    if(last == ''):
        last = first
    print(first + last)
    sums += int(first + last)
    first = ''
    last = ''

print(sums)
