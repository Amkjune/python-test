a = int(input("Enter number: "))
i=1
j=1
k=1
for i in range(a):
    for j in range(a-i,0,-1):
        print(" ",end='')
    for k in range(i):
        print("* ",end='')
    print("")
