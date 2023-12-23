# Create an empty dictionary
my_dict = {}

# Adding key-value pairs
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'

print("Initial Dictionary:")
print(my_dict)

# Updating key-value pairs
my_dict['age'] = 31  # Update the 'age' key
my_dict['country'] = 'USA'  # Add a new key-value pair

print("\nUpdated Dictionary:")
print(my_dict)

# Deleting key-value pairs
del my_dict['city']  # Delete the 'city' key
my_dict.pop('country', None)  # Delete the 'country' key using pop method (with a default value)

print("\nDictionary after Deletions:")
print(my_dict)
