## Algorithm for file updates in Python 
## SCENARIO...
## You are a security professional working at a health care company. As part of your job, 
## you're required to regularly update a file that identifies the employees who can access restricted content. 
## The contents of the file are based on who is working with personal patient records. 
## Employees are restricted access based on their IP address. There is an allow list for IP addresses permitted to sign into the restricted subnetwork. 
## There's also a remove list that identifies which employees you must remove from this allow list.
## Your task is to create an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list. 
## If so, you should remove those IP addresses from the file containing the allow list.


# Assign the name of the "import_file" to the name of the file 

import_file = "allow_list.txt"

with open(import_file, "r") as file:
    
# use read() to read the imported file and store it in a variable named "ip_addresses"
    ip_addresses = file.read()

# covert ip_addresses from a string to a list
ip_addresses = ip_addresses.split()


# Created a for loop to loop through "remove list"
for item in remove_list:
    if item in ip_addresses:
        ip_addresses.remove(item)

#Covert ip_addresses back into a string
ip_addresses = "\n".join(ip_addresses)

# "With" statement to rewrite the original file 
with open(import_file, "w") as file:
    file.write(ip_addresses)