print("Let's form a triangle.")
print()
side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the triangle: "))

if side1 < side2 + side3 or side2 < side1 + side3 or side3 < side2 + side1:
    print("It's a triangle.")
    if side1 == side2 == side3:
        print()
        print("It is an equilateral triangle.")
    
    elif side1 == side2 or  side2 == side3 or side1 == side3:
     print()
     print("It is an isosceles triangle.")

    else:
       print("It is a scalene triangle.")

    if side1 > side2 and side3:
        hip = side1**2
        cateto = side2**2 + side3**3
        print(hip)
        print(cateto)
        if hip == cateto:
           print("It is a right-angled triangle.")
    
    if side2 > side1 and side3:
        hip = side2**2
        cateto = side1**2 + side3**3
        print(hip)
        print(cateto)
        if hip == cateto:
           print("It is a right-angled triangle.")

    if side3 > side1 and side2:
        hip = side3**2
        cateto = side1**2 + side2**3
        print(hip)
        print(cateto)
        if hip == cateto:
           print("It is a right-angled triangle.")
           