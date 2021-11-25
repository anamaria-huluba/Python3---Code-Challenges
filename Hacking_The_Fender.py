#Hacking The Fender

# The Fender, a notorious computer hacker and general villain of the people, has compromised several 
# top-secret passwords including your own. Your mission, should you choose to accept it, is threefold. 
# You must acquire access to The Fender‘s systems, you must update his "passwords.txt" file to scramble 
# the secret data. The last thing you need to do is add the signature of Slash Null, a different hacker
#  whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as 
# a threat.

# 1. Are you there? We’ve opened up a communications link to The Fender‘s secret computer. 
# We need you to write a program that will read in the compromised usernames and passwords that are 
# stored in a file called "passwords.csv".

# First import the CSV module, since we’ll be needing it to parse the data.

import csv

compromised_users = []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    print(password_row['Username']) 




