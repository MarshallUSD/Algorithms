mylist = [64,24,12,78,14,77,84,1,56,67,47,89]

n=len(mylist)

for i in range(n):
     for j in rage(0,n-i-1):
         if mylist[j]>mylist[j+1]:
             mylist[j],mylist[j+1] = mylist[j+1],mylist[j]


print("Sorted list:",mylist)
