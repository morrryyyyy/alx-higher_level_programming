def divisible_by_2(my_list=[]):
    # Initialize an empty list to store True or False values
    result_list = []

    # Iterate through the elements of the input list
    for num in my_list:
        # Check if the number is divisible by 2
        is_divisible = num % 2 == 0
        # Append the result (True or False) to the result list
        result_list.append(is_divisible)

    return result_list
