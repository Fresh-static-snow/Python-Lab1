from sys import argv


def isExpression(text):
    for number in text.replace("-", "+").split("+"):
        if not number.isdigit():
            return 0
    return text[0].isdigit() and text[-1].isdigit()


print("(True,(0)".format(eval(argv[1])) if isExpression(argv[1])
     else "(False,None)")

print(isExpression(1+2+4-2+5-1))
print(isExpression(user_input='123'))
print(isExpression(user_input='hello+12'))
print(isExpression(user_input='2++12--3'))
print(isExpression(user_input=''))
# 1. result = (True, 9)
# 2. result = (True, 123)
# 3. result = (False, None)
# 4. result = (False, None)
# 5. result = (False, None)
