# there are 100 cars
cars = 100
# there is 4.0 space in each car
space_in_a_car = 4.0
# there are 30 drivers
drivers = 30
# there are 90 passengers
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven



print "There are" , cars, "cars available."
print "There are only" , drivers, "drivers available."
print "There will be" , cars_not_driven, "empty cars today."
print "We can trasnport" , carpool_capacity, "people today"
print "We have" , passengers, "to carpool today."
print "We need to put about" , average_passengers_per_car, "in each car."
