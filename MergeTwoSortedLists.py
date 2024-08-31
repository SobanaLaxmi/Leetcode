l1 = list(map(str,input().split(",")))
l2 = list(map(str,input().split(",")))
for i in range(0,len(l2)):
    l1.append(l2[i])
print(sorted(l1))