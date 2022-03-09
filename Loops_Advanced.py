# Python Code Challenges: Loops (Advanced)

# 1. Larger Sum
# We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the 
# sums, afterwards we will compare the two and return which one has a greater sum. 

# Here are the steps we need:
# Define the function to accept two input parameters: lst1 and lst2
# Create two variables to record the two sums
# Loop through the first list and add up all of the numbers
# Loop through the second list and add up all of the numbers
# Compare the first and second sum and return the list with the greater sum

# Larger Sum function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else:
    return lst2

# Testing function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
# should return [1, 9, 5]

# In this solution, we manually iterate through each element in each list and calculate our sums. We then return the list with the greater sum and break 
# the tie by returning lst1. You can also try solving this problem using the sum() function in python. The body of this function could also be condensed 
# into one line of code if you want an additional challenge!

# 2. Over 9000
# We are constructing a device that is able to measure the power level of our coding abilities and according to the device, it will be impossible for our power
# levels to be over 9000. Because of this, as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater 
# than 9000. Once this happens, we should stop adding the numbers and return the value where we stopped. 

# In order to do this, we will need the following steps:
# Define the function to accept a list of numbers
# Create a variable to keep track of our sum
# Iterate through every element in our list of numbers
# Within the loop, add the current number we are looking at to our sum
# Still within the loop, check if the sum is greater than 9000. If it is, end the loop
# Return the value of the sum when we ended our loop

# Over 9000 function here
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

# Testing function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
# should return 9020

# Our solution follows a similar pattern to some of the other code challenges, except that we have a condition where we end early. In the case where we reach a sum greater 
# than 9000, we can use the break keyword to exit our loop. This will continue to execute the code outside of our loop, which in this case, returns the sum that we found.

# 3. Max Num
# Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of numbers. This can be accomplished using the max()
# function in python, but as a challenge, we are going to manually implement this function. 

# Here is what we need to do:
# Define the function to accept a list of numbers called nums
# Set our default maximum value to be the first element in the list
# Loop through every number in the list of numbers
# Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
# Return the maximum number

# Max Num function here
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

# Testing function is done
print(max_num([50, -10, 0, 75, 20]))
# should return 75

# There are a few different ways to accomplish this task, but the way we did it was to check every element in the list and see if there is one bigger than what we currently 
# think is the biggest. If there is a bigger one, then replace it. We keep replacing the number until the largest number has been found.

# 4. Same Values
# In this challenge, we need to find the indices in two equally sized lists where the numbers match. We will be iterating through both of them at the same time and 
# comparing the values, if the numbers are equal, then we record the index. 

# These are the steps we need to accomplish this:
# Define our function to accept two lists of numbers
# Create a new list to store our matching indices
# Loop through each index to the end of either of our lists
# Within the loop, check if our first list at the current index is equal to the second list at the current index. If so, append the index where they matched
# Return our list of indices

#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst 

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# should return [0, 2, 3]

# In this solution, we used a loop that iterates using the range of the len of our list. This generates the indices we need to iterate through. Note that we assume
# the lists are of equal size. We then access the element at the current index from each list using lst1[index] and lst2[index]. If they are equal we add the index to
# the new list. Finally, we return the results.

# 5. Reversed List
# For the final challenge, we are going to test two lists to see if the second list is the reverse of the first list. There are a few different ways to approach this,
# but we are going to try a method that iterates through each of the values in one direction for the first list and compares them against the values starting from the 
# other direction in the second list. 

# Here is what you need to do:
# Define a function that has two input parameters for our lists
# Loop through every index in one of the lists from beginning to end
# Within the loop, compare the element in the first list at the current index against the element at the second list’s last index minus the current index. If there was a mismatch, then the lists aren’t reversed and we can return False
# If the loop ended successfully, then we know the lists are reversed and we can return True.

# Reversed List function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

# Testing function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
# True

print(reversed_list([1, 5, 3], [3, 2, 1]))
# False

# In this code, we iterate through each of the indices for the entire length of either of the lists (since we assume the lengths are equal) and we perform a comparison 
# on each of the elements. We get the element at the current index from our first list with lst1[index] and we test it against the last index of the second list minus 
# the current index len(lst2) - 1 – index.

# That math is a little complicated — it helps to look at a concrete example. If we are given a list of 5 elements, the valid indices are 0 to 4. Because of this, the 
# last index in the second list is len(lst2) - 1, or 5 - 1 = 4. Now in order to get the inverse of the position we are at in the first list, we subtract the index we 
# are at from the end of the second list. So on the first pass, we’ll compare the element at position 0 to the element at position 5 - 1 - 0 = 4. On the next pass, 
# we’ll compare the element at position 1 to the element at position 5 - 1 - 1 = 3, and so on.

# If any of the two elements are not equal then we know that the second list is not the reverse of the first list and we return False. If we made it to the end without 
# a mismatch then we can return True since the second list is the reverse of the first. 