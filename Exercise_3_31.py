#(Geometry: point position) Given a directed line from point p0(x0, y0) to p1(x1, y1), you can use the following condition to decide whether a point p2(x2, y2) is on the left side of the line, on the right side of the line, or on the same line.
#Write a program that prompts the user to enter the three points for p0, p1, and p2 and displays whether p2 is on the left side of the line from p0 to p1, on the right side, or on the same line.

x0 =float(input(f"Enter the x-coordinate of Point 0: "))
y0 =float(input(f"Enter the y-coordinate of Point 0: "))
x1 =float(input(f"Enter the x-coordinate of Point 1: "))
y1 =float(input(f"Enter the y-coordinate of Point 1: "))
x2 =float(input(f"Enter the x-coordinate of Point 2: "))
y2 =float(input(f"Enter the y-coordinate of Point 2: "))

exam = (x1 - x0)*(y2 - y0) - (x2-x0)*(y1-y0)

if exam >0:
    print(f"p2 is on the left side of the line.")
elif exam <0:
    print(f"p2 is on the right side of the line.")
else: print(f"p2 is on the same line.")
