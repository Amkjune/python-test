import random
for z in range(0,a[pivot]):
    pivot=a[z]
    while(i<j):
        for i in range(0,len(a)):
            if a[i] < pivot:
                continue
            else:
                exit
        for j in range(len(a)-1, 0, -1):
            if a[i] > pivot:
                continue
            else:
                exit
        v=a[i]
        a[i]=a[j]
        a[j]=v
    i=a[i]
    a[i]=pivot
    pivot=i
    
print(a) 


n = int(input("Enter number of elements : "))
 
# Below line read inputs from user using map() function
a = list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n]
v = 0
print("\nList is - ", a)
i=0
j=len(a)-1
pivot=0



print('Sorted Array in Ascending Order:')
print(a)
    
        

