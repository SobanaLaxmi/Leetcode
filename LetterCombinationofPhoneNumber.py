from itertools import *
digits = input()
val = {"2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqr",
    "8":"stu",
    "9":"vwz",
}
s1 = [val[i] for i in digits if i in val.keys()]
combin = [''.join(j) for j in product(*s1)]
print(combin)
    