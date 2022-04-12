def perimeter_of_square(s):
     perimeter = 4 * s
     if not isinstance(s, int):
         raise ValueError("Input must be numeric")
     return perimeter

def merge_and_sort_two_lists(list1, list2):
    list3 = list1 + list2
    return sorted(list3)

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

def sum_of_numbers_in_string(str):
    sum_numbers = 0
    for i in str:
        if i.isdigit() == True:
            digit = int(i)
            sum_numbers = sum_numbers + digit
    return sum_numbers


