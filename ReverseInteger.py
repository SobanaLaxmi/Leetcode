n = int(input())
s = str(n)
s1 = ""
neg = s[0] =='-'
if neg:
    s = s[1:]
s1 = s[::-1]
s1 = s1.lstrip('0')
if neg:
    print(f"-{s1}")
else:
    print(s1)
