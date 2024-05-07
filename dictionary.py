a = {}
b=1
while(b!=3):
    print(f"1: delete 2: add 3: Exit")

    b=int(input("enter your choice ::"))
    if (b == 1):
        c=input("Enter key to delete ::")
        a.pop(c)  
        x= a.items()
        print(x)
    elif (b == 2):
        c=input("enter key to add")
        d=input("enter value to the key")
        a[c] = d
        x= a.items()
        print(x)
    elif (b == 3):
        exit

    
