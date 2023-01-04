
#Project 13- Creating a Random Generator

#**EC2 Random Name Generator**

#Instructions
#You need to ensure that the EC2s are properly named and are unique so that owners of EC2 instances are known. 
#Use Python to create your unique EC2 names that the users can then attach to the instances. 
# My Python script should contain the below: 

# 1. Allow  the user to input how many EC2 instances they want names for and output the same amount of unique names.
# 2. Allow the user to input the name of their department that is used in the unique name.
# 3. Generate random characters and numbers that will be included in the unique name.

import random 
import string 
import sys

# Define Variables:
# department - Define Department names
# number- How many EC2 instances are needed


def string_generator(size=6, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))


department = input("Enter Department: Marketing, Accounting, FinOps: ")  
    
for _ in department:
    
    if department == "Marketing" or department.lower() == "marketing" :
        print("Proceed to next entry")
        # hint "Marketing" should print
        break
    
    elif department == "Accounting" or department.lower() == "accounting" :
        print("Proceed to next entry")
        # hint "Accounting" should print
        break
    
    elif department == "FinOps" or department.lower() == "finops" :
        print("Proceed to next entry")
        #hint "FinOps should print"
        break
    
    else:
        print("Error: You can not use this generator, enter an appropriate department name.")
        raise SystemExit
        sys.exit()  

        
number = int(input("Enter the number of EC2 instances you need: "))


    
if number < 0:
    print("Please enter a positive number: ")
 
elif number > 0:
    print("See information below regarding your instances")
    
   
        

print()
print("--------------------------------")
print("EC2 Instance Names")
print("--------------------------------")
print()

for _ in range(1, number + 1):
    unique_name = department
    EC2_unique_name = unique_name + "-" + string_generator()
    print("Your EC2 Instance's Unique Name is : ", EC2_unique_name)
    