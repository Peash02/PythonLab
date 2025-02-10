a = int(input("Enter Number1:"))
b = int(input("Enter Number2:"))
temp = a
a = b
b = temp
print(f"Number 1 is {a} and Number 2 is {b}" )
a = a + b
b = a - b
a = a - b
print("Number 1 is ", a , "and Number 2 is ", b )