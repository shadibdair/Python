print("After Sorting: ")
arr=[3,1,5,2,9,8,10]
print(arr)

for i in range(len(arr)):
    minimum = i

    for j in range(i+1,len(arr)):
        # Select the smallest value:
        if arr[j]<arr[minimum]:
            minimum= j
        
    # place it at the front of the sorted end of the array.
    arr[minimum],arr[i]=arr[i],arr[minimum]

print("Before Sorting: ")
print(arr)















"""
print("After Sorting")
x=[7,1,5,2,8,10]
print(x)

for i in range(1,len(x)):
    for j in range(i,len(x)):
        if x[j-1]>x[j]:
                temp=x[j-1]
                x[j-1]=x[j]
                x[j]=temp

print("Before Sorting")
print(x)
"""

    

