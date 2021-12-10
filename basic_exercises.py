# Write a loop that uses while instead of the built-in looping structure
total_records = 101
counter = 0

while counter <= total_records:
    counter += 10
    print(f"total count: {counter}")

# Write a loop that loop over the keys in a dictionary and prints the values
my_dict = {"first dog": "Frida", "new puppy": "Winston"}

for key, val in my_dict.items():
    print(f"{val} is my {key}.")

# Write the functions is_odd and is_even that are shown in the lecture
def is_odd(integer):
    """return a boolean to answer whether the integer is odd"""

    if isinstance(integer, int):
        return integer % 2 == 1
    else:
        raise ValueError(f"expecting argument type of `int`. got {type(integer)} instead. Pass an integer!")


def is_even(integer):
    """return a boolean to answer whether the integer is event"""
    
    return not is_odd(integer)

# Loop over my_first_list and square the value if the value is a number, 
# and print the calories of the fruit if it’s a fruit (hint: use the dictionary to look up the calories)
my_first_list = ['apple', 1, 'banana', 2, 'pineapple']
cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

for item in my_first_list:
    if isinstance(item, int) or isinstance(item, float):
        print(item**2)
    elif isinstance(item, str):
        cal_lookup.get(item, f"{item} does not exist as a fruit in cal_lookup")

# write a function that takes a dictionary as an argument, loops over the keys in the dictionary, prints the square of the value in the value
def square_dict_values(dictionary):
    """given a dictionary of keys that contain numerical values, 
    print the square of each value
    """
    if isinstance(dictionary, dict):
        try:
            print([val**2 for val in dictionary.values()])
        except TypeError:
            print("Ruh'Roh! a dictionary value may not be square-able. Check that values are int or float types")
    else:
        print("Ruh'Roh! The function requires a dictionary")

r_values_dict = {"model1": 0.754, "model2": 0.84}
square_dict_values(r_values_dict)