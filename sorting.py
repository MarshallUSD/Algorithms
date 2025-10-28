#Selection sprting
"""""

def selection(arr):
    n=len(arr)
    for i in range(n):
        mid_index=i
        for j in range(i+1,n):
            if arr[j]<arr[mid_index]:
                mid_index=j
        arr[i],arr[mid_index]=arr[mid_index],arr[i]
    return arr

list1=[64,25,12,22,11]
print("Selection sorting: ",selection(list1))    
"""""
#Buble sorting

def buble(arr):
    n=len(arr)
    for i in  range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            
            

    return arr

list1=[64,25,12,22,11]
print("Buble sorting: ",buble(list1))

