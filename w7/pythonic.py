#!/usr/bin/env python3


    # for (i, value) in enumerate(seq):
    #     if value == target:
    #         break
    # else:
    #     return -1
    # return i



# Looping over a collection 

# colors = ['red', 'green', 'blue', 'yellow']
# range(5) == [0, 1, 2, 3, 4]

# for i in range(len(colors)):
#     print(colors[i])

# for color in colors:
#     print(color)


# ####################


# Looping backwards

colors = ['red', 'green', 'blue', 'yellow']

# for i in range(len(colors)-1, -1, -1):
#     # print(i)
#     print(colors[i])

# for color in reversed(colors):
#     print(color)


#######################33

# colors = ['red', 'green', 'blue', 'yellow']
# # for i in range(len(colors)):
# #     print(f"{i} --> {colors[i]}")
# for index, color in enumerate(colors):
#     print(f"{index} --> {color}")


# names =  ['raymond', 'rachel', 'matthew']
# colors = ['red',     'green' , 'blue'    , 'yellow']


# for name, color in zip(names, colors):
#     print(f"{name} --> {color}")
# n = min(len(names), len(colors))
# for i in range(n):
#     print (names[i], '--->', colors[i])


colors = ['red', 'green', 'blue', 'yellow']

# Forward sorted order
# for color in sorted(colors):
#     print(color)

# Backwards sorted order
# for color in sorted(colors, reverse=True):
#     print(colors)



# Multiple exit points in a loop

def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

# list1 = [1, 3, 5]
# target = 6
# print(find(list1, target))



###### DICTIONARIES ##############################

d = {'a': 1, 'b':2, 'c': 3}

# for k in d:
#     print (f"{k} --> {d[k]}")

# for k in d.keys():
#     print (f"{k} --> {d[k]}")

# for key, val in d.items():
#     print (f"{key} --> {val}")


# construct from pairs
names = ['raymond', 'rachel', 'matthew']
colors = ['red',    'green' , 'blue']

pair_dic = dict(zip(names, colors))
# print(pair_dic)

# COUNTING WITH DICTIONARIES
# from collections import default_dict, Counter
# d = default_dict(int), 

my_list = ['a', 'b', 'c', 'a', 'c', 'a']
# result: {'a': 3, 'b': 1, 'c': 2}

count_dict = {}
for letter in my_list:

    # if (letter not in count_dict.keys()):
    #     count_dict[letter] = 0

    # count_dict[letter] = count_dict[letter] + 1

    count_dict[letter] = count_dict.get(letter, 0) + 1

print(count_dict)