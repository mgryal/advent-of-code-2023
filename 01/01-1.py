lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

first = None
last = None
total = 0
for line in lines:
    for character in line:
        if character.isnumeric() and first == None:
            first = character
        elif character.isnumeric():
            last = character
    if last == None:
        last = first
    total += int(first + last)
    first = None
    last = None

print(total)