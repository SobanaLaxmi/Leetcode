n = list(map(int,input().split(",")))
target = int(input())
closesum = float('inf')
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        for k in range(j+1,len(n)):
            currsum = n[i]+n[j]+n[k]
            if(abs(currsum - target)<abs(closesum-target)):
                closesum = currsum
print(closesum)