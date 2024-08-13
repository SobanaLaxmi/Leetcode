
n = list(map(int,input().split(",")))
n1 = list(map(int,input().split(",")))
n2 = n+n1
leng = len(sorted(n2))
print(sorted(n2))
if(leng % 2 == 0):
    med = (n2[int(leng/2)]+n2[int(leng/2)-1])/2;
    print(med)
else:
    print(n2[int(leng/2)-1])