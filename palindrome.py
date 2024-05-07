str = input(print("Enter string"))
a=[]
i=0
c=0
d=-1
r=0
for i in range(len(str)):
    a.append(str[i])
for c in range(0,len(a)):
    for d in range(len(a) - 1, 0, -1):
        if (c!=d):
            if (a[c] == a[d]):
                r=c
                break
            elif (c-r==1):
                d-1
                if (a[c] == a[d]):
                    r=c
                    continue
            else:
                print("number not palindrome")
                exit()
        else:
            print("number is palindrome")
            exit()
    continue
      

    


