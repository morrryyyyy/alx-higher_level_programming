#!/usr/bin/python3
# Define the function
def delete_at(my_list=[], idx=0):
    # Handle invalid index
    if idx < 0 or idx > len(my_list):
        return my_list
    # Delete item at index
    del my_list[idx]
    return my_list
