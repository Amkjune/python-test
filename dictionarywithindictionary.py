a = {
    "firstname" : "aman",
    "lastname" : "kaur",
    "Address" : {
        "firstaddress" : "234 fjfk",
        "secondaddress" : "45fghh"
                }
}
b=1
while(b!=3):
    print(f"1: delete 2: add 3: update 4: Exit")

    b=int(input("enter your choice ::"))
    if (b == 1):
        c=input("Enter key to delete ::")
        if c in a:
            a.pop(c)  
            x= a.items()
            print(x)
        else:
            a["Address"].pop(c)
            x= a.items()
            print(x)
    elif (b == 2):
        c=input("enter key to add")
        d=input("enter value to the key")
        a[c] = d
        x= a.items()
        print(x)
    elif (b == 3):
        c=input("enter key to update")
        d=input("enter new value")
        if c in a:
            a[c] = d
            x= a.items()
            print(x)
        else:
            a["Address"][c] = d
            x= a.items()
            print(x)
    elif (b == 4):
        exit
    else:
        print("invalid number")
