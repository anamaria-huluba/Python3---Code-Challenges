Python Code Challenges: Lists (Advanced)

1. Every Three Numbers
Let’s start our challenging problems with a function that creates a list of numbers up to 100 in increments of 3 starting from a number that is passed to the 
function as an input parameter. 

Here is what we need to do: 
Define the function to accept one parameter for our starting number
Calculate the numbers between the starting number and 100 while incrementing by 3
Store the numbers in a list
Return the list
Code Challenge

# Every Three Numbers function here:
def every_three_nums(start):
  return list(range(start, 101, 3))
 
# Testing function is done
print(every_three_nums(91))
# should return [91, 94, 97, 100]

We can write the body of this function in one line by nesting the range() function inside of the list() function. 
The range function accepts the starting number, the ending number (exclusive), and the amount to increment by.

2. Remove Middle
Our next function will remove all elements from a list with an index within a certain range. The function will accept a list, a starting index, 
and an ending index. All elements with an index between the starting and ending index should be removed from the list. 

Here are the steps:
Define the function to accept three parameters: the list, the starting index, and the ending index
Get all elements before the starting index
Get all elements after the ending index
Combine the two partial lists into the result
Return the result

# Remove Middle function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

# Testing function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
# should return [4, 23, 42]

This can be solved using one line of code if you combine and slice the lists at the same time. Slicing allows us to get the segments of the list before and 
after the index range and the operation + allows us to combine them together.

3. More Frequent Item

Let’s go back to our factory example. We have a conveyor belt of items where each item is represented by a different number. We want to know, out of two items, which one shows up more on our belt. To solve this, we can use a function with three parameters. One parameter for the list of items, another for the first item we are comparing, and another for the second item. Here are the steps:

Define the function to accept three parameters: the list, the first item, and the second item
Count the number of times item1 shows up in our list
Count the number of times item2 shows up in our list
If item1 shows up more, return item1. Otherwise, return item2

# More Frequent Item function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2

# Testing function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
# should return 3

We use the count() function to find the number of occurrences for each item. We then compare the counts against each other to 
find the item which appears the most in the list. The item with the most appearances is returned by the function.

4. Double Index
Our next function will double a value at a given position. We will provide a list and an index to double. This will create a new list by replacing the value at the index provided with double the original value. If the index is invalid then we should return the original list. Here is what we need to do:

Define the function to accept two parameters, one for the list and another for the index of the value we are going to double
Test if the index is invalid. If its invalid then return the original list
If the list is valid then get all values up to the index and store it as a new list
Append the value at the index times 2 to the new list
Add the rest of the list from the index onto the new list
Return the new list

# Double Index function here
def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list 
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst
  
# Testing function is done
print(double_index([3, 8, -10, 12], 2))
#should return [3, 8, -20, 12]

print(double_index([3, 8, -10, 12], 5))
# should return original list as the list has an index of 4: [3, 8, -10, 12]

5. Middle Item
For the final code challenge, we are going to create a function that finds the middle item from a list of values. 
This will be different depending on whether there are an odd or even number of values. In the case of an odd number of elements, 
we want this function to return the exact middle value. If there is an even number of elements, it returns the average of the middle two elements. 

Here is what we need to do:
Define the function to accept one parameter for our list of numbers
Determine if the length of the list is even or odd
If the length is even, then return the average of the middle two numbers
If the length is odd, then return the middle number

# Middle Item function here
def middle_element(lst):
# if even
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
 # if odd
  else:
    return lst[int(len(lst)/2)]

# Testing function is done
print(middle_element([5, 2, -10, -4, 4, 5])) 
# returns 7

We used modulus to determine if the list had an even or odd number of elements. After determining this, for an odd number of elements, we calculate the middle 
index and return the middle element from the list. For an even number of elements, we calculate the index of the element close to the middle and the other 
element close to the middle (by subtracting 1 from the middle calculation). We get the values at those indices and calculate the average.

Note that the math to find the middle index is a bit tricky. In some cases, when we divide by 2, we would get a double. For example, if our list had 3 items in it, 
then 3/2 would give us 1.5. The middle index should be 1, so in order to go from 1.5 to 1, we cast 1.5 as an int. In total, this is int(len(lst)/2).
