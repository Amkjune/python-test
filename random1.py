import random
print(random.randrange(1,10))

a="aman preet"
print(a[4])
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

x = ["hi welcome", "aman", "azad"]
print(x[:1])

y = "hi"
print(y[1])

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# print("my name is john, and i am "+ age) wrong

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 

