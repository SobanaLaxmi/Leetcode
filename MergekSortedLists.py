l1 = list(input())
l2 = []
for i in l1:
    if i.isdigit():
        l2+=i 
print(sorted(l2))