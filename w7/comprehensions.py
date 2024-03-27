#!/usr/bin/env python3

# map
my_list = [1, 3, 6, 10]
new_list = []
for num in my_list:
    new_list.append(func(num))

# # 

# print(new_list)




# my_list = [1, 3, 6, 10]
# new_list = [ num**2 for num in my_list ]
# print(new_list)


new_list = [ num for num in my_list if num % 2 == 0 ]
# print(new_list)

# map, filter