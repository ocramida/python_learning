# assigning values to variables, or the assignment operator puts 
#	value into a variable, or variable gets value.
cars = 100.5
space_in_a_car = 4.2
drivers = 30.2
passengers = 90
# next set of variables are using variables above in algebraic equation below 
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# printing strings that refer to variables and in turn insert the values 
#	of those variables in the string. 
print "There are" , cars, "cars available."
print "There are only" , drivers, "drivers available."
print "There will be" , cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have" , passengers, "to carpool today."
print "We need to put about" , average_passengers_per_car, "in each car."