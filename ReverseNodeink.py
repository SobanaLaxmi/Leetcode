l1 = list(map(str,input().split(',')))
k = int(input())
l2,l3,l4 = [],[],[]
for i in range(0,len(l1)):
    if l1[i].isdigit():
        l2 += l1[i]
for i in range(0,len(l2)):
    l3+=l2[i]
    if (len(l3) == k):
        l4+=l3[::-1]
        l3=[]
print(l4+l3)