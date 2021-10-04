# Create a function named flights that receives a different number of arguments representing the information about the flights for a day:
# •	the destination of each flight
# •	the count of passengers that are boarding the plane
# •	a string "Finish"
# You need to take each argument and make a dictionary with the plane’s destination as a key and the passengers as a value of the corresponding key.
# If there are more than one flight to the same destination, you should count all the passengers that flew to the destination.
# You should modify the dictionary until the current argument is equal to "Finish".



def flights(*args, all_flights=dict()):
    if args[0] == "Finish" or not args:
        return all_flights

    if args[0] not in all_flights:
        all_flights[args[0]] = 0

    all_flights[args[0]] += args[1]
    return flights(*args[2:], all_flights=all_flights)


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))