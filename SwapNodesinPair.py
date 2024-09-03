l1 = list(map(str,input().split(',')))
l2,l3 = [],[]
for i in range(0,len(l1)):
    if l1[i].isdigit():
        l2 += l1[i]
for i in range(0,len(l2),2):
    l3.append(l2[i+1])
    l3.append(l2[i])
print(l3)