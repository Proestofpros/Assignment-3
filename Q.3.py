my_list = eval(input('Enter the list: '))
my_result = [(val, pow(val, 2)) for val in my_list]
print(my_result)
