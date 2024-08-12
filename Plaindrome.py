n = int(input())
s = str(n)
s1 = s[::-1]
if(s==s1):
    print("true - palindrome")
else:
    print("false - not palindrome")
