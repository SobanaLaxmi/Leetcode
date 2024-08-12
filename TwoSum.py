nums = list(map(int,input().split(",")))
target = int(input())
l = len(nums);
for i in range(0,l):
    for j in range(0,i):
        if(nums[j]+nums[i]==target):
            print(j,i)