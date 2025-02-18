print("   *   ", "  * *  ", " *   * ", " ** ** ","  * *  ", "  * *  " ," *****  ", sep='\n')

john = 3
mary = 5
adam = 6

total_apples = john + mary + adam

print("John: " + str(john) + ", Mary: " + str(mary) + " Adam: " + str(adam));
print("Total apples: " + str(total_apples))

kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles * 1.609344
kilometers_to_miles = kilometers / 1.609344
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

x = 2
x = float(x)
y = 3*3 - 2*2 + 3*x - 1
print("y =", y)