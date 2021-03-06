Python Code Challenges: Functions

1. Tenth Power
Let’s create some functions which can help us solve math problems! For this first function, we are going to take the tenth power of a number. 
In order to do this we need to do three things:

Set up the function header for tenth_power which accepts one parameter
Take the tenth power of the input value
Return the result

# Tenth Power function here:
def tenth_power(num):
  return num**10

# Testing tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1

# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0

print(tenth_power(2))
# 2 to the 10th power is 1024

This is one way to solve this problem using two lines of code.
The first line is the function header which uses def to define the function followed by the function name. Within the parentheses we include num which is our formal parameter.
Because of this, num is the variable name for the value we pass into this function.
On our next line, we use return to show that this function is going to return a value when it is called. Next to the return keyword, we define what value is going to be 
returned.
Since we need the tenth power of our input value, we can use the power operator in python which is **. Using this knowledge, in order to get the tenth power of our input 
value, we use num ** 10.

2. Square Root
Another useful function for solving math problems is the square root function. We can create this using similar steps from the last problem. The code will look very similar. 

We need to:
Set up the function header for square_root which accepts one parameter
Take the square root of the input value
Return the result

# Square Root function here:
def square_root(num):
  return num ** 0.5

# Testing square_root function:
print(square_root(16))
# should print 4

print(square_root(100))
# should print 10

As you can see, this solution is very similar to the last problem. In this case, the only changes we need are the function name and changing the power value to 0.5. 
We define the function called square_root with one parameter. We then take the one half power of the input value which is mathematically the same as taking the square 
root and return it.

3. Win Percentage
Next, we will create a function which calculates the percentage of games won. In order to do this, we will need to know how many total games there were and divide the
number of wins by the total number of games. For this function, there will be two input parameters, the number of wins and the number of losses. We also need to make
sure that we return the result as a percentage (in the range of 0 to 100). 

In order to create this method we need the following steps:
Define the function header with two parameters, wins and losses
Calculate the total number of games using the number of wins and losses
Get the ratio of winning using the number of wins out of the total number of games.
Convert the ratio to a percentage
Return the percentage

# Win percentage function, the simpler way:
def win_percentage(wins, losses):
  return wins / (wins + losses) * 100
  
# Win percentage function, using variables:
 def win_percentage(wins, losses):
  total_games = wins + losses
  ratio_won = wins / total_games
  return ratio_won * 100 

# Testing function win_percentage function:
print(win_percentage(5, 5))
# should print 50

print(win_percentage(10, 0))
# should print 100

First, we defined our function with two parameters, one for games won and one for games lost. Next, we calculated the total number of games using the number of 
wins + losses. After that, we use calculate the ratio of wins out of the total number of games by dividing wins by our total_games variable. Since this gives us 
a ratio and we want it in percentage form, we multiply the answer by 100 and return it.

4. Average
Let’s create a function which takes the average of two numbers. These two numbers will be the input of the function and the output will be the average of the two. In order 
to do this, we need to do a few steps:

Define the function with two input parameters, num1 and num2
Calculate the sum of the two numbers
Divide the sum by the number of inputs to the function
Return the answer

# Average function here:
def average(num1, num2):
  return (num1 + num2) / 2
  
# Testing average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5

print(average(1, -1))
# The average of 1 and -1 is 0

In this solution, we defined the function with two parameters one line and returned the average on the next line. When returning the value, we used parentheses around 
the addition to cause the two numbers to be added together first before dividing by two.

5. Remainder
For the final challenge in this group, we are going to take the remainder of two numbers while performing other mathematical operations on them. We are going to multiply 
the numerator by 2 and divide the denominator by 2. After the two values have been modified, we will divide them and return the remainder. 

In order to do this we will need to:
Define the function to accept two parameters
Multiply the first input value by 2
Divide the second input value by 2
Calculate the remainder of the modified first input value divided by the modified second input value (using modulus)
Return the answer
  
 # Remainder function here:
def remainder(num1, num2):
  return (num1 * 2) % (num2 / 2)

# Testing remainder function:
print(remainder(15, 14))
# should print 2

print(remainder(9, 6))
# should print 0

Our solution is shortened to use only two lines of code. The first line defines the function with two input parameters. The second line performs the two mathematical 
operations on either side of the modulus within parenthesis. This causes the two calculations to be performed before taking the remainder of the left side divided by 
the right side.
