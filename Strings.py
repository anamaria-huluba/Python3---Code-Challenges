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

# 6. Check Name

# You are creating an app that allows users to interact and share their coding project ideas online. 
# The first step is to provide your name in the application and a greeting for other people to see 
# which contains your name. Let’s create a function that is able to check if a user’s name is located 
# within their greeting. We need a function that accepts two parameters, a string for our sentence 
# and a string for a name. The function should return True if the name exists within the string 
# (ignoring any differences in capitalization). 
# 
# Here is what we need to do:
# Define the function to accept two parameters, one string for the sentence and one string for the name
# Convert all of the strings to the same case so we don’t have to worry about differences in 
# capitalization
# Check if the name is within the sentence. If so, then return True. Otherwise, return False

# check_for_name function here:

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

print(check_for_name("My name is Jamie", "Jamie"))
# returns: print True
print(check_for_name("My name is jamie", "Jamie"))
# returns: True
print(check_for_name("My name is Samantha", "Jamie"))
# returns: False

#As you can see, this function can be created using one line. The in keyword will return True if the first provided string 
# is within the second. So in this case, we’re checking if name is in sentence. In order to ignore differences in 
# capitalization, we can use the .lower() function which converts all characters to lowercase characters.

# 7. Every Other Letter

# For this next function, we are going to create a function that extract every other letter from a string and returns the 
# resulting string. There are a few different ways you can solve this problem.
# 
# Here are the steps needed for one of the ways:
# Define the function to accept one parameter for the string
# Create a new empty string to hold every other letter from the input string
# Loop through the input string while incrementing by two every time
# Inside the loop, append the character at the current location to the new string we initialized earlier
# Return the new string
# Code Challenge

# Write your every_other_letter function here:
def every_other_letter(word):
  every_other_letter_str = ""
  for letter in range(0, len(word), 2):
    every_other_letter_str += word[letter]
  return every_other_letter_str

print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

#In order to alternate which character is added to the every_other string, we use a range of indices which starts at 
# index 0 (the beginning of our word) and ends at the end of our word. The third parameter in the range function 
# determines what value to increment by. In this case, we want to increment by 2 in order to get every other letter.

#Another way to loop through all indices of our original string, but only add the letters that correspond to an even 
# index. As a challenge, try solving this problem that way!

# 8. Reverse

# This one is similar to the last challenge. Instead of selecting every other letter, we want to reverse the entire string. T
# This can be performed in a similar manner, but we will need to modify the range we are using. 
# 
# Here is what we need to do:
# Define the function to accept one parameter for the string
# Create a new empty string to hold the reversed string
# Loop through the input string by starting at the end, and working towards the beginning
# Inside the loop, append the character at the current location to the new string we initialized earlier
# Return the result

# reverse_string function here:

def reverse_string(word):
  reversed_str = ""
  for letter in range(len(word)-1, -1, -1):
    reversed_str += word[letter]
  return reversed_str

print(reverse_string("Codecademy"))
# returns: ymedacedoC
print(reverse_string("Hello world!"))
# returns: !dlrow olleH
print(reverse_string(""))
# returns: 

#This is similar to the last solution, but our range has been modified in order to start at the last index of the string 
# (length of the string minus one) up to the first index. Since the parameter for the ending index is exclusive we need to 
# provide the index of one more iteration than what we want to stop at. We want to stop at 0, and since we are incrementing
#  by -1, we will set the ending index to -1. Finally, make sure to add the third parameter of -1. This makes us increment 
# by -1 at each step.

# 9. Make Spoonerism

# A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is made 
# when someone says “Belly Jeans” instead of “Jelly Beans”. We are going to make a function that is similar, but instead 
# of using the first syllable, we are going to switch the first character of two words. 
# 
# Here is what we need to do:
# Define the function to accept two parameters for our two words
# Get the first character of the first word and the first character of the second word
# Get the remaining characters of the first word and the remaining characters of the second word.
# Append the first character of the second word to the remaining character of the first word
# Append a space character
# Append the first character of the first word to the remaining characters of the second word.
# Return the result

# make_spoonerism function here:

def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

print(make_spoonerism("Codecademy", "Learn"))
# returns: Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# returns: wello Horld!
print(make_spoonerism("a", "b"))
# returns: b a

#We can accomplish the task in one line by appending and slicing at the same time. We can get the first index of our words 
# by using word1[0] and word2[0] which gets the letter at the first index. In order to get the remaining letters we can 
# use word1[1:] and word2[1:]. This returns all characters in the strings starting with index 1 and on. We concatenate 
# everything together to get the result.

# 10. Add Exclamation

# Let’s say we are writing a program that displays a large message on a blimp and we need to fill in any missing space if
# a short phrase is provided. Our function will accept a string and if the size is less than 20, it will fill in the 
# remaining space with exclamation marks until the size reaches 20. If the provided string already has a length greater 
# than 20, then we will simply return the original string. 
# 
# Here are the steps:
# Define the function to accept one parameter for our string
# Loop while the length of our input string is less than 20
# Inside the loop, append an exclamation mark
# Once done, return the result

# Write your add_exclamation function here:

def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

print(add_exclamation("Codecademy"))
# returns: Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# returns: Codecademy is the best place to learn

