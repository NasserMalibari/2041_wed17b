#!/usr/bin/env python3

from collections import Counter

my_list = [1,2,2,2,2,3,3,3]
my_counter = Counter(my_list)

my_counter[5] += 5
print(my_counter)