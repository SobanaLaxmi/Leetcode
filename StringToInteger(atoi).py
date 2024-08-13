import re
s = input()
if s[0] not in '-0123456789':
    print(0)
else:
    neg = s[0] == '-'
    pos = s[0] == '+'
    if neg or pos:
        s = s[1:]
    s = s.lstrip('0')
    n = re.findall(r'\d+', s)
    if n:
        if neg:
            print(f"-{n[0]}")
        else:
            print(n[0])
    else:
        print(0)
