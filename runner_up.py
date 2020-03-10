n = int(input())
if (n>=2 and n<=10):
    arr=list(map(int, input().split(" ")[:n]))

#print(Array)

max=-999

for i in range(n):
    for j in range(i+1,n):
        if (arr[i]> arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    

max =arr[i] 
l=len(arr)
#print(l)
i=0
while (i<l):
    if (arr[i]==max):
        arr.remove(arr[i])

        l=l-1
        i=i-1
    i+=1

       


print(arr[-1])