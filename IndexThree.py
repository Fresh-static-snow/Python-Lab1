formul = input("input = ")
formul = formul.replace(" ", "")
length = len(formul) - 1

if formul == "":
    print("error! found no expression")
    exit(1)

elif formul[0].isdigit() and formul[length].isdigit():
    while length >= 0:
        if formul[length].isdigit():
            length -= 1
        elif formul[length] == '+' or formul[length] == '-':
            if formul[length + 1] == '+' or formul[length + 1] == '-':
                print("error in expression!")
                exit(1)
            length -= 1
else:
    print("error in expression!")
    exit(1)

result = eval(formul)
print(result)