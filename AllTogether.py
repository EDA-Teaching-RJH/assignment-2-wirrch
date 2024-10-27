### Part Four -- your code goes here. 

import random

the_list = []

# Add 10 random ints from 1 to 100 on the end of the_list
for i in range(10):
    the_list.append(random.randint(1,100))

# print(the_list)

# Go through the_list, find how many even numbers there are
number_of_evens = 0
for the_element in the_list:
    if the_element % 2 == 0:
        number_of_evens += 1

# print(f"Number of Evens: {number_of_evens}")

# Go through the list, remove any even numbers, stop when number_of_evens = 0
i = 0
while number_of_evens != 0:
    # print(f"{i}, {the_list[i]}")
    if the_list[i] % 2 == 0:
        the_list.pop(i)
        number_of_evens -= 1
    else:
        i += 1

# Print **THE_FINAL_LIST**
print(the_list)