from operator import add, sub, mul, truediv
from sys import argv

if len(argv) == 4:
    dictionary = {'add': add, 'sub': sub, 'mul': mul, 'truevid': truediv}
    try:
        print(dictionary[argv[2]](int(argv[1]), int(argv[3])))
    except:
        print("error")
else:
    print("not enough arguments")