# - Create a distance converter converting Km to milessd

# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

# Get user input for name and distance in kilometers
name = input("Please enter your first name: ")
distance_km = float(input("Please enter the distance in kilometers: "))

# Convert kilometers to miles
distance_miles = distance_km / 1.609

# Print the greeting and the distance in both kilometers and miles
print("Hi " + name.capitalize() + "" + " distance in miles: " +str(distance_miles))

name.re