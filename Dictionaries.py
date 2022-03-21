1. Sum Values

For the first code challenge, we are going to look at only the values in a dictionary. This function 
should sum up all of the values from the key-value pairs in the dictionary. 

Here are the steps we need:
Define the function to accept one parameter for our dictionary
Create a variable to keep track of our sum
Loop through every value in the dictionary
Inside the loop, add each value to the sum
Return the sum

# sum_values function here:
def sum_values(my_dictionary):
  total = 0
  for value in my_dictionary.values():
    total += value
  return total

OR useing function sum()
def sum_values(my_dictionary):
  return sum(my_dictionary.values())

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# returns: 10
print(sum_values({10:1, 100:2, 1000:3}))
# returns: 6

We start by creating a variable to keep track of the total. Next, we use the values() function in our for loop in order to iterate through each of the values in the 
dictionary. Using this, we can access each value and add it to our total variable. At the end of our loop, we return the total.

2. Even Keys

Next, we are going to do something similar, but we are going to use the keys in order to retrieve the values. Additionally, we are going to only look at every even 
key within the dictionary. 

Here are the steps:
Define the function to accept one parameter for our dictionary
Create a variable to keep track of our sum
Loop through every key in the dictionary
Inside the loop, if the key is even, add the value from the even key
After the loop, return the sum

# sum_even_keys function here:

def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key%2 == 0:
      total += my_dictionary[key]
  return total

OR 
def sum_even_keys(my_dictionary):
  return sum([v for k, v in my_dictionary.items() if k%2 == 0])

OR 
def sum_even_keys(my_dictionary):
  return sum([my_dictionary[k] for k in my_dictionary.keys() if k%2 ==0])
             
print(sum_even_keys({1:5, 2:2, 3:3}))
# returns: 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# returns: 6

Similar to the previous problem, we are iterating through our dictionary, except this time we are iterating through the keys instead of the values. In order to get 
the keys we use the keys() function and to get the value of a key we can use brackets. To test if the key is even we use the modulus operator and test if the remainder
is 0 when dividing by 2.

3. Add Ten

Let’s loop through the keys again, but this time let’s modify the values within the dictionary. Our function should add 10 to every value in the dictionary and return
the modified dictionary. 

Here is what we need to do:
Define the function to accept one parameter for our dictionary
Loop through every key in the dictionary
Retrieve the value using the key and add 10 to it. Make sure to re-save the new value to the original key.
After the loop, return the modified dictionary

# add_ten function here:
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# returns: {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# returns: {10:11, 100:12, 1000:13}

We use a for loop to iterate through each key and we access the value using the key. After accessing it, we overwrite the value with the value plus 10. Finally, we 
return the modified dictionary.

4. Values That Are Keys

We are making a program that will create a family tree. Using a dictionary, we want to return a list of all the children who are also parents of other children. 
Using dictionaries we can consider those people to be values which are also keys in our dictionary of family data. 

Here is what we need to do:
Define the function to accept one parameter for our dictionary
Create an empty list to hold the values we find
Loop through every value in the dictionary
Inside the loop, test if the current value is a key in the dictionary. If it is then append it to the 
list of values we found
After the loop, return the list of values which are also keys

# values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary:
      value_keys.append(value)
  return value_keys

OR using a list comprehension
def values_that_are_keys(my_dictionary):
  return [v for k, v in my_dictionary.items() if v in my_dictionary.keys()]

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# returns: [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# returns: ["a"]

For this solution, we iterate through every value within the dictionary. In order to check if it is also a key, we can use the in keyword. This checks the value 
against all of the keys in the dictionary to see if it exists as a key as well. If it does, then we append it to our list of values which are also keys.

5. Largest Value

For the last challenge, we are going to create a function that is able to find the maximum value in the dictionary and return the associated key. This is a twist on 
the max algorithm since it is using a dictionary rather than a list. 

These are the steps:
Define the function to accept one parameter for our dictionary
Initialize the starting key to a very low number
Initialize the starting value to a very low number
Iterate through the dictionary’s key/value pairs.
Inside the loop, if the current value is larger than the current largest value, replace the largest 
key and largest value with the current ones you are looking at
Once you are done iterating through all key/value pairs, return the key which has the largest value

# max_key function here:
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

OR using function max() and lambda 
def max_key(my_dictionary):
  return max(my_dictionary, key = lambda key: my_dictionary[key])

print(max_key({1:100, 2:1, 3:4, 4:10}))
# returns: 1
print(max_key({"a":100, "b":10, "c":1000}))
# returns: "c"

In order to program the max algorithm using dictionaries, we need to keep track of the max value and the key which is used to access it. We start by using 
float("-inf") in order to initialize them to the lowest possible value. To retrieve the key and value at the same time, we use the items() function.Inside our loop,
we overwrite the current largest value and the key used to access whenever we find a larger value. We return the largest value’s key once we have iterated through the
entire dictionary.

6. Word Length Dict

Let’s start by writing a function that creates a new dictionary based on a list of strings. The keys of our dictionary will be every string in our list of strings, 
while the values will be the length of each the words in the string list. 

Here are the steps:
Define the function to accept one parameter for our list of strings
Create a new empty dictionary
Loop through every string in the list of strings
Inside the loop, add the string as a key and the length of the string as the value to the dictionary
After the loop, return the new dictionary

# word_length_dictionary function here:
def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths

OR we could do it this way:
def word_length_dictionary(words):
  return {word:len(word) for word in words}

print(word_length_dictionary(["apple", "dog", "cat"]))
# returns: {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# returns: {"a": 1, "": 0}

To create a new dictionary we set a variable equal to {}. While iterating through each string in our string list, we can add the key and value to our dictionary using
this syntax: word_lengths[word] = len(word).

7. Frequency Count

This next function is similar, but instead of counting the length of each string in the list of strings, we will be counting the frequency of each string. This 
function will also accept a list of strings as input and return a new dictionary. 

Here is what we need to do:
Define the function to accept one parameter for our list of strings
Create a new empty dictionary
Loop through every string in the list of strings
Inside the loop, if the string is not already in our dictionary, store the string as a key with a value of 0 in our dictionary. Then, increment the value by 1.
After the loop, return the new dictionary

# frequency_dictionary function here:

def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1
  return freqs

OR we cound use Counter library in Python:
from collections import Counter:
  
def frequency_dictionary(words):
  return dict(Counter(words))
  
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# returns: {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# returns: {0:5}

To create a new dictionary we set a variable equal to {}. We iterate through each of the strings in the list of strings and check if it is already in our dictionary 
using the in keyword. If it is not then we add it as a new key-value pair where the value is 0. Regardless of whether the string was already in the dictionary, 
increase the value by 1. This will make it so all new entries will have a value of 1 and all existing entries will increase their old value by 1.

8. Unique Values

Now let’s try reading a dictionary as input and finding how many values are unique. The function should return a number which is the count of all values from the 
dictionary without including duplicates. 

These are the steps:
Define the function to accept one parameter for our dictionary
Create a new empty list
Loop through every value in our dictionary
Inside the loop, if the value is not already in our list, append the value to our list
After the loop, return the length of our list

# unique_values function here:

def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

OR using Python sets:
def unique_values(my_dictionary):
  return len(set(my_dictionary.values()))

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# returns: 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# returns: 1

This function has a similar structure to the last one except that the input has been changed to a dictionary. We iterate through each of the values and whenever we 
find one we have not added to our list already, we add it to the list. After the loop, we return the length of the list since that contains all unique values from 
the dictionary.

9. Count First Letter

This function accepts a dictionary where the keys are last names and the values are lists of first names of people who have that last name. We need to calculate the
number of people who have the same first letter in their last name. 

Here are the steps we need:
Define the function to accept one parameter for our dictionary
Create a new empty dictionary called letters
Loop through every key in our names dictionary
Inside the loop, get the first letter of the last name we are looking at. If the first letter 
is not in our letter dictionary, add it as a key with a value of 0. Then, increment that key by the 
number of people that have that last name
After the loop, return the letters dictionary

# count_first_letter function here:
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

OR we can use defaultdict:
from collections import defaultdict

def count_first_letter(names):
  d = defaultdict(int)
  for name in names:
    first_name = name[0]
    d[first_name] += len(names[names])
   return dict(d)
  
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# returns: {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# returns: {"S": 7}

This function uses two dictionaries instead of one dictionary and one list. We iterate through each of the keys (which are the last names) and store the first letter 
of the last name in first_letter. We then use similar logic to what we have used before by testing if we have already seen that letter before. If we haven’t seen that 
letter before, then we add it to our dictionary with a value of 0. Next, we are going to increment the value. Since we know that some people share the last name (as 
seen by the list of first names in our names dictionary), we are going to increment the value in our letters dictionary by the length of first names that share the 
last name for our current iteration (key).



