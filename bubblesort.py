a = []
f=1
b=0
c=0
for i in range(0,5):
    v=input("Enter list of number")
    a.append(v)
print(a)
while f!=0:
    f=0
    for i in range(len(a)-1):
        b = i+1
        if a[i]>=a[b]:
            c=a[i]
            a[i]=a[b]
            a[b]=c
            f=f+1
            print(a)
        else:
            continue
    i=0
    continue
print(a)
