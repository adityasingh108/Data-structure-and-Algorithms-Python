    # Write a program to ask user to enter the day they
    # want to calculate the average temperature of the asked day 
    # and also show in which day the temperature is over the average
from array import *


input_day = int(input("Enter the day you want to calculate the average temperature:"))
array_temp = array( 'i',[]) 
for i in range(1,input_day+1):
    user_temp = int(input(f"Enter {i} Day temperature "))
    array_temp.append(user_temp)
average = sum(array_temp) / len(array_temp)
print(f"The average temperature of {input_day} days is {average}")
above = 0 
for i in array_temp:
    if i > average:
        above +=1
print(f'{above}days is over the average temperature')