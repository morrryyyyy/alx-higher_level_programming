#!/usr/bin/python3
# Define the function
def divisible_by_2(my_list=[]):
    # Initialize an empty list to store the result
    result_list = []
    # Iterate through the input list
    for num in my_list:
        # Check if it is divisible by 2
        if num % 2 == 0:
            # Append true to the resulting list, otherwise append false
            result_list.append(True)
        else:
            result_list.append(False)
    # Return the result list
    return result_list
