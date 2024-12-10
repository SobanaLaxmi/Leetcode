nums = list(map(int,input().split(',')))
val = int(input("val = "))
s = sorted(nums)
l = []
c=0
for i in s:
    if i == val:
        c+=1
    else:
        l.append(i)
le = len(l)
l += ['_']*c
print(le,", nums = ",l)
