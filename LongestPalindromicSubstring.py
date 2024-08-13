s = input()
longsub = ""
for i in range(len(s)):
    for j in range(i,len(s)):
        substr = s[i:j+1]
        if(substr == substr[::-1] and len(substr) > len(longsub)):
            longsub = substr
print(longsub)