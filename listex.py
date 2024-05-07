thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #will not print Kiwi

print(thislist[2:5]) #will print from cherry to Kiwi

print(thislist[2:])  #will print from cherry to end

print(thislist[-4:-1]) #will print from orange till mango but not including mango

if "apple" in thislist:
    print("yes, Apple is in the list")

thislist[1] = "blackcurrent"
print(thislist)

thislist.insert(2, "watermelon")
print(thislist)                   #at the second place add watermelon

thislist.append("orange")
print(thislist)                   #add orange at the last place




thislist = ["apple", "banana", "cherry"]     #to consolidate two lists, tuples, sets, dictionaries
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)

thislist.remove("banana")                    #to remove from the list
print(thislist)

thislist.pop()                               #remove the last item from the list
print(thislist)

del thislist[0]                             #del removes the value and the idex as well
print(thislist)

thislist.clear()                            #list remains without content
print(thislist)