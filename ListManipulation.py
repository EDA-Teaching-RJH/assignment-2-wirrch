### Part Three -- your code goes here. 

the_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
additional_list = [7, 8]

# Just sorts it from lowest - highest ig
the_list.sort()
# print(f"SORTED: {the_list}")

# Get the amount of 1s in the list (assuming they're already sorted, so the 1s are at the front) remove that many from the front of the list
for i in range(the_list.count(1)):
    the_list.pop(0)

# Merge the_list and additional_list together (with additional_list at the end)
the_list.extend(additional_list)

# Print the list lol
print(the_list)