a = 4

def myfun():
    global a 
    a = 2
    print(a)

myfun()
print(a)