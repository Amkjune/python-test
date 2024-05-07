
a = int(input("enter number"))
for i in range(2,a+1):
    if a == i:
        print("prime number")
        break
    if a%i == 0:
        print("number is not prime")
        break
    else:
        continue

