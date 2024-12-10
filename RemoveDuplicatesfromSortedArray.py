nums = list(map(int,input().split(',')))
s = sorted(nums)
l1=[]
l = []
c=0
for i in s:
    if i not in l:
        l.append(i)
    elif i not in l1:
        l1.append(i)
le = len(l1)
leng = len(l)
l += ['_']*le
print(leng,", nums = ",l)
