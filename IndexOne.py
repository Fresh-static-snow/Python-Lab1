import operator
import sys
a = {'+': operator.add, '-': operator.sub,
     '*': operator.mul, '/': operator.truediv}


print(a[sys.argv[2]]((int)(sys.argv[1]),
                     (int)(sys.argv[3])))
