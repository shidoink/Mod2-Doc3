def areaCalc():
    length= input("How long is the house?")
    width=input("How wide is the house?")
    area= int(length)* int(width)
    print(f"The house has an area of {area}")

def circumCalc():
    radius= float(input("What is the radius?"))
    circumference= radius * 2.0 * 3.1415
    print(f"This circle has a circumference of {circumference}")