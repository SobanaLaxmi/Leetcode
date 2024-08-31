l1 = input()
alpha,digit = [],[]
for i in l1:
    if i.isalpha():
        alpha.append(i)
    elif i.isascii():
        digit.append(i)
    else:
        pass
for i in range(0,len(digit)):
    s = alpha[i]
    d = digit[i]
    print(s*int(d),end="")