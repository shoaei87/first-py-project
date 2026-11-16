#project 1 (if):

age=int(input("enter your age:"))
if age >= 18:
    print("you are adult.")
else:
    print("you are under 18.")

#project 2 (for):
length=int(input("enter a number for length:"))
width=int(input("enter a number for width:"))

for i in range(width):
    for j in range(length):
        print("*",end=" ")
    print()
#project 3 (while):
while True:
    number=(int(input("enter number:")))
    if number ==0:
        break
    print(number)
    