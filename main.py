#greet user
print("welcome today you will guess the area of a rectangle based on its length and width.")

#get length
length = int(input("Enter length of rectangle (cm): "))

#get width
width = int(input("Enter width of rectangle (cm): "))

#calculate area
area = width * length

#ask user for guess
guess = int(input("What is the area of the rectangle (cm^2): "))

#determine if guess is correct
if area == guess:
  print("Correct, the area of the rectangle is " + str(area) + "cm^2")
else:
  print("Incorrect, the area of the rectangle is " + str(area) + "cm^2")