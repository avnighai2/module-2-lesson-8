def square(x):
    perimeter = 4*x
    print("The perimeter of a square is", perimeter )

def rectangle (l,b):
    perimeter = 2*(l+b)
    return perimeter

def circumfrence(r):
    c = 2*3.14*r
    print("The circumfrence of a circle is", c)

r = int(input("Enter the radius of a circle:"))
circumfrence(r)

x = int(input("Enter the side of a square:"))
square(x)

l = int(input("Enter the length of a rectangle:"))
b = int(input("Enter the breadth of a rectangle:"))
print(rectangle(l,b))