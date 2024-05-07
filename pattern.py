a = int(input("Enter number: "))
i=1
j=1
for i in range(a):
    #print("i"+str(i),end)
    for j in range(a-i,0,-1):
        print("*",end='')
    print("")


            
    

