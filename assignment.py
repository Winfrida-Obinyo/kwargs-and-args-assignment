#  Write a function that takes an unknown number of arguments and returns their sum.
def sum_all(*args):
    return sum(args)

result = sum_all(1, 2, 3, 4, 5) 
print (result)


# // Write a function that takes two arguments, the first being a string and the second being an unknown number of integers. The function should return a new string where the integers have been added to the original str
# // ing.
def add_numbers(s, *args):
    for num in args:
        s += str(num)
    return s
original_string = "The total is: "
new_string = add_numbers(original_string, 10, 20, 30)
print(new_string)

# // Write a function that takes an unknown number of keyword arguments and returns a dictionary where the keys are the argument names and the values are the argument values.
def keyword_args(**kwargs):
    return kwargs
result = keyword_args(name='Alice', age=30, city='New York')
print(result)

# // Write a function that takes a function and an unknown number of arguments, and returns the result of calling the function with the arguments.
def call_function_with_args(func, *args):
    return func(*args)
def add_numbers(x, y):
    return x + y

result = call_function_with_args(add_numbers, 5, 7)
print(result)

# // Write a function that takes an unknown number of keyword arguments, each with a string value. The function should concatenate all the strings and return the resulting string.
def concatenate_strings(**kwargs):
    return ''.join(kwargs.values())
result = concatenate_strings(name='Alice', age='30', city='New York')
print(result)     



