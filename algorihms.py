#1.	Algorithm FindMaximum(List)
 #   3max ← List[0]
    #for each number in List do
     #   if number > max then
    #        max ← number
   #     end if
  #  end for
 #   return max
#End Algorithm

# Implementation of the FindMaximum algorithm in Python
"""""
def FindMaximum(list):
    max=list[0]
    for num in list:
        if num>max:
            max=num
    return max
"""""

#2.
#      2.	Algorithm Factorial(n)
    #result ← 1
    #for i ← 1 to n do
   #     result ← result * i
  #  end for
 #   return result
#End Algorithm
#


# Implementation of the Factorial algorithm in Python
"""""
def Factorial(n):
    result = 1
    for i in range(1, n+1):
        result *=i
    return result
    """
#3. 3.	Algorithm BubbleSort(List)
   # n ← length(List)
    #for i ← 0 to n - 1 do
     #   for j ← 0 to n - i - 2 do
      #      if List[j] > List[j + 1] then
       #         swap List[j] and List[j + 1]
        #    end if
        #end for
  #  end for
   # return List
#End Algorithm
"""""
def Bubble(list):
    n=len(list)
    for i in range(n):
        for j in range(0, n-i-1):
              if list[j]>list[j+1]:
                    list[j], list[j+1]=list[j+1], list[j]
    return list
"""""
        
        