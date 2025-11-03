arr=[10,20,20,10,10,30,50,10,20]
n=len(arr)

#finding total number of matching pairs of socks

def sokcets(arr,n):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                count+=1    
        return count

print(sokcets(arr,n))            