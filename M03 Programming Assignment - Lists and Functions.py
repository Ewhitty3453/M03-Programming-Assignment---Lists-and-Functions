#!/usr/bin/env python
# coding: utf-8

# In[ ]:


things = ["mozzarella", "Cinderella", "salmonella"]

things[0] = things[0].upper()

print(things)


# In[ ]:


def good():
    return ['Harry', 'Ron', 'Hermione']

# Call the function and store the result in a variable
result_list = good()

# Print the result
print(result_list)


# In[ ]:


def get_odds():
    for number in range(1, 10, 2):
        yield number

# Use a for loop to find and print the third value returned
count = 0
for value in get_odds():
    count += 1
    if count == 3:
        print("Third odd value:", value)
        break

