Python Code Challenges: Functions (Advanced)

1. First Three Multiples
Let’s start by creating a function which both prints and returns values. For this function, we are going to print out the first three multiples of a number and return 
the third multiple. This means that we are going to print 1, 2, and 3 times the input number and then return the value of 3 times the input number. 

For this, we are going to need a few steps:
Define the function header to accept one input parameter called num
Print out 1 times num
Print out 2 times num
Print out 3 times num
Return the value of 3 times num

# First three multiples function here
def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

# Testing first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30

first_three_multiples(0)
# should print 0, 0, 0, and return 0

In this solution, we start by defining the function header with an input. We then use the next three lines to print the result of multiplying the input value by one, two, and 
three. Finally, we return the result of multiplying the input value by 3.

2. Tip
Let’s say we are going to a restaurant and we decide to leave a tip. We can create a function to easily calculate the amount to tip based on the total cost of the food
and a percentage. This function will accept both of those values as inputs and return the amount of money to tip. 

In order to do this, we will need a few steps:
Define the function to accept the total cost of the food called total and the percentage to tip as percentage
Calculate the tip amount by multiplying the total and percentage and dividing by 100
Return the tip amount

# Tip function here:
def tip(total, percentage):
  tip_amount = (total * percentage) / 100
  return tip_amount

# Testing tip function:
print(tip(10, 25))
# should print 2.5

print(tip(0, 100))
# should print 0.0

In this solution, we defined the function with two parameters and then used them to calculate the tip amount. We multiplied the input values together and divided by 100 
since the second input is in percentage form and we want a monetary amount. Lastly, we returned the calculated tip value.

3. Bond, James Bond
It’s time to re-create a famous movie scene through code. Our function is going to concatenate strings together in order to replace James Bond’s name with whatever name 
we want. The input to our function will be two strings, one for a first name and another for a last name. The function will return a string consisting of the famous 
phrase but replaced with our inputs. 

To accomplish this, we need to:
Define the function to accept two parameters, first_name and last_name
Concatenate the string ', ' on to the last_name
Concatenate the first_name on to the result of the previous step
Concatenate a space on to the result
Concatenate the last_name again to the result
Return the final string

# Write your introduction function here:
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

# Testing Introduction function:
print(introduction("Anamaria", "Huluba"))
# should print Huluba, Anamaria Huluba

print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

First, we defined the method to accept the first and last names. On the next line, we performed all of the concatenations at once by adding the comma, spaces, and names 
in the correct order. We also returned the result on the same line.

4. Dog Years
Let’s create a function which calculates a dog’s age in dog years! This function will accept the name of the dog and the age in human years. It will calculate the age of 
the dog in dog years and return a string describing the dog’s age. 

This will require a few steps:
Define the function called dog_years to accept two parameters: name and age
Calculate the age of the dog in dog years
Concatenate the string with the dog’s name and age in dog years
Return the resulting string

# Dog Years function here:
def dog_years(name, age):
  return name + ", you are " + str(age * 7) +" years old in dog years!"

# Testing dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"

print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

In this solution we used two lines of code to accomplish this task. The first line defines the function with the two inputs and the second line concatenates the string 
while also performing the calculation. We used str(age * 7) to convert the number to a string, and since that function call returns a string, we can concatenate it 
in-line with the rest of the string.

5. All Operations
For the final code challenge, we are going to perform multiple mathematical operations on multiple inputs to the function. We will begin with adding the first two inputs,
then we will subtract the third and fourth inputs. After that, we will multiply the first result and the second result. In the end, we will return the remainder of the 
previous result divided by the first input. We will also print each of the steps. 

The steps needed to complete this are:
Define the function to accept four inputs: a, b, c, and d
Print and store the result of a + b
Print and store the result of c - d
Print and store the first result times the second result
Return the previous result modulo a

# Lots Of Math function here:
def lots_of_math(a, b, c, d):
  first = a + b
  second = c - d
  third = first * second
  print(first)
  print(second)
  print(third)
  return third % a

# Testing lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0

print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

After defining the function, we store each result into its own variable for first and second. We then use these two variables in the calculation for third and we use the 
value of third to get fourth. Afterwards, we print the first three variables and return the fourth one.
