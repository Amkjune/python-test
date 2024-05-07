a=[]
b=0
c=0
d=0
v=0
for i in range(0,5):
    v=input("enter number")
    a.append(v)
print(a)
for j in range(0,len(a)):
    for k in range(0,len(a)):
        if a[j]>a[k]:
            c=a[j]
            a[j]=a[k]
            a[k]=c
        else:
            continue
    continue
print(a)        
        