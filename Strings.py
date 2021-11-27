# 1. Count Letters
# For the first code challenge, we are going to count the number of unique letters in a string. 
# This means that when we are looking at the word, any new letters should be counted and any duplicates 
# should not be counted. There are a few ways to solve this, but we can use the provided alphabet 
# string to ensure that duplicates are not counted. 

# Here is what we need to do:
# Define the function to accept one parameter — the word whose letters we are counting
# Create a counter to keep track of unique letters
# Loop through every letter in our alphabet string. If the current letter was found in our word, increase our count
# Return the count after looping through all letters.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# unique_english_letters function here:

def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

print(unique_english_letters("mississippi"))
# returns: 4
print(unique_english_letters("Apple"))
# returns: 4

#Since the provided alphabet string includes a single instance of all uppercase and lowercase letters 
# in the English alphabet, we can iterate through that string and see if our input strings contains the 
# current letter we are looking at. This can be accomplished using the keyword in. 
# For every letter in the possible letters, we see if that letter is in our string!

# 2. Count X

# This time we are going to count the number of occurrences of a certain letter within a string. 
# Our function will accept a parameter for a string and another for the character which we are going 
# to count. For example, providing the word "mississippi" and the character 's' would result in an 
# answer of 4. 
# 
# These are the steps we need to take:
# Define the function to accept two parameters. word for the input string and x for the single character
# Create a counter to keep track of the occurrences
# Loop through every letter in the string. If the current letter is equal to the input letter, increase our counter
# Return the counter after looping through the entire string.

# count_char_x function here:

def count_char_x(word, x):
  count = 0
  for letter in word:
    if letter == x:
       count += 1
  return count

print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# This solution is similar to the last solution. In this case, we are looping through the input 
# string and comparing it against the input character. If they are the same, then we increase the 
# counter.

# 3. Count Multi X

# Now let’s change our function to compare against an entire string instead of a single character. 
# This function should accept a string and a substring to compare against. 
# The number of occurrences of the second parameter within the first parameter string are returned. 
# What this means is that we are checking the number of occurrences of the shorter string 
# (second parameter) within the longer string (first parameter). One way to accomplish this is using 
# the split function. 
# 
# Here is how to do that:
# Define the function to accept two parameters. word for the input string and x for the second string we are searching for
# Split the string into substrings based on the second input parameter
# Count the number of instances the substring appeared in the first input string based on the split string
# Return the result

# count_multi_char_x function here:

def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

print(count_multi_char_x("mississippi", "iss"))
# returns: print 2
print(count_multi_char_x("apple", "pp"))
# returns: 1

# In our function, we split the first input string using the second input string. What this does is cut 
# the first string into an array of smaller substrings containing the parts not equal to our second 
# parameter x. For example, when splitting "mississippi" with the string "iss", the resulting array
#  will be [“m”, “”, “ippi”]. This includes the characters before "iss" was found, the empty space 
#  between the two instances of "iss" and the characters after the last"iss". Be careful! In order 
#  to get the correct result we need to return one less then the total number of split sections — in 
#  this example, "iss" was in the string twice, resulting in 3 sections. So we should return 3 - 1.

# 4. Substring Between

# Here is a challenging problem. We need a function that is able to extract a portion of a string 
# between two characters. The function will take three parameters where the first parameter is the 
# string we are going to extract the substring from, the second input is the starting character of 
# our substring and the third character is the ending character of our substring. 
# 
# Here are the steps we can use:
# Define the function to accept three parameters, one string and two characters
# find the starting index of our substring using the second input parameter
# find the ending index of our substring using the third input parameter
# If neither of the indices are -1, return the portion of the first input parameter string between the 
# starting and ending indices (not including the starting and ending index)
# If either of the indices are -1, that means the start or end of the substring didn’t exist in our 
# string. Return the original string in this case.

# substring_between_letters function here:

def substring_between_letters(word, start, end):
  start_letter = word.find(start)
  end_letter = word.find(end)
  if start_letter > -1 and end_letter > -1:
    return(word[start_letter+1:end_letter])
  return word

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

#In this solution, we use the find function to get the starting and ending indices of our substring 
# using our starting and ending characters. After getting those, we check to make sure neither of 
# them are -1. In order to extract the portion of the string within those indices, we use slicing. 
# We provide the starting index plus one in order to not include the starting character. We do not
#  need to provide the end index plus one, since the value on the right of the colon is excluded. 
# This causes our slicing to look like: word[start_ind+1:end_ind]).

# 5. X Length

# Let’s use the split method in a different way. We need a new function that is able to accept two 
# inputs: one for a sentence and another for a number. The function returns True if every single word
#  in the sentence has a length greater than or equal to the number provided. 
# 
# These are the steps:
# Define the function to accept two parameters, one string, and one number
# Split up the sentence into an array of words
# Loop through the words. If the length of any of the words is less than the provided number return False
# If we made it through the loop without returning False then return True

# x_length_words function here:

def x_length_words(sentence, x):
  words = sentence.split(" ")
  for word in words:
    if len(word) < x:
      return False
  return True

print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

#We can use the split function with the space character provided in order to get an array of all of 
# the words in the sentence. Next, we use the in keyword in order to loop through every element in our 
# array of words. We check the length of each word and compare it against x to see if it is shorter. 
# If any of the words in the array are shorter then we immediately return False and end the function. 
# If we make through all of the words without returning False, we know we should return True since all 
# of the word’s lengths were longer than x.

