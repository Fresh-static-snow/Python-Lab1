import operator
import sys
a = {"add": operator.add, "sub": operator.sub,
     "mul": operator.mul, "truediv": operator.truediv}
print(a[sys.argv[1]]((int)(sys.argv[2]), (int)(sys.argv[3])))
