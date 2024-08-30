def validparan():
    paran = {
        "(":")",
        "{":"}",
        "[":"]"
    }
    stk=[]
    for char in s:
        if char in paran:
            stk.append(char)
        elif char in paran.values():
            if not stk or paran[stk.pop()]!=char:
                return False
    return len(stk) == 0
s = input()
res = validparan()
print(res)