n = int(input("Enter number of elements : "))
 
# Below line read inputs from user using map() function
a = list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n]
 
print("\nList is - ", a)
v=0
for min in range(0,len(a)):
    print(min)
    for i in range(min,len(a)):
        if a[min]< a[i]:
            continue
        else:
            v=a[min]
            a[min]=a[i]
            a[i]=v
            continue
    print(a)
    continue
