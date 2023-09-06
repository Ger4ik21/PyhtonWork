sequence = input("Input sequence: ")

sequenceNew = ""


for i in sequence:
    if i.isdigit() == False:
        sequenceNew += i

print("New sequence without digits: ", sequenceNew)