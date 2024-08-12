#from operator import add
l1 = list(map(int,input().split(",")))
l2 = list(map(int,input().split(",")))
l1 = l1[::-1]
l2 = l2[::-1]
s1=""
s=""
for i in range(0,len(l1)):
    s+=str(l1[i])
for i in range(0,len(l2)):
    s1+=str(l2[i])
n = int(s)+int(s1)
l = [int(x) for x in str(n)]
print(l[::-1])