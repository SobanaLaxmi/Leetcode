head = list(map(int,input().split(",")))
n = int(input())
rev_head = head[::-1]
new_head=[]
for i in range(0,len(rev_head)):
    if i == (n-1):
        pass
    else:
        new_head.append(rev_head[i])
print(new_head[::-1])