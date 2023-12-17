import json

# Assuming the JSON data is stored in a file named "flight_data.json"
file_path = "pp.json"

# Read the JSON data from the file
with open(file_path, "r") as file:
    flight_data = json.load(file)

# Now you can access different parts of the JSON data
print("Flight Agency Name:", flight_data["flightAgency"]["name"])
print("Location:", flight_data["flightAgency"]["location"]["city"], ",", flight_data["flightAgency"]["location"]["country"])

# Accessing details of the first flight
first_flight = flight_data["flightAgency"]["flights"][0]
print("First Flight Number:", first_flight["flightNumber"])
print("Airline:", first_flight["airline"])
print("Departure Airport:", first_flight["departure"]["airport"])
print("Passenger Details:")
for passenger in first_flight["passengers"]:
    print("  - Name:", passenger["name"])
    print("    Seat Number:", passenger["seatNumber"])
    print("    Ticket Class:", passenger["ticketClass"])