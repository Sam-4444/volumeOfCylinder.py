# volume of cylinder

height=float(input("enter the height of cylinder and press enter ! "))
radius=float(input("enter the radios of cylinder and press enter ! "))
print("height of cylinder is : "+str(float(height)))
print("radius of cylinder is "+str(float(radius)))
pi=3.14
volume=pi*radius*radius*height
print("volume is "+str(volume))
print("surface area is : "+str(float((2*3.14*height*radius)+(2*(3.14*(radius**2))))))