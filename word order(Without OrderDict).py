n=int(input())
arr=[]
for i in range(n):
    arr.append(input())

count=[]
cnt=1

i=0
while(i<len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            cnt+=1
            count.append(cnt)
            element=arr[j]
            arr.remove(arr[i])
            
            arr.remove(element)
            break
    else:
        count.append(cnt)   
            
            
    
    cnt=1
    i+=1
count.append("1")  
    
print(len(count))
string= ' '.join(map(str, count))
print(string)




