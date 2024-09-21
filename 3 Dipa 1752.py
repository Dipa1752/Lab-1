
# Initial list of customer names
customers = ["Alice", "Bob", "Charlie", "David", "Eve"]

# a. Access the third customer in the list and print their name
# The third customer is at position 2 (because lists start at 0)
third_customer = customers[2]
print("The third customer is:", third_customer)

# b. Change the name of the second customer to "Ben"
# The second customer is at position 1
customers[1] = "Ben"
print("Customer list after changing the second customer:", customers)

# c. Add a new customer named "Frank" to the end of the list
# Using append() to add "Frank" at the end
customers.append("Frank")
print("Customer list after adding Frank:", customers)

# d. Remove the customer "David" from the list
# Using remove() to delete "David" from the list
customers.remove("David")
print("Customer list after removing David:", customers)

# e. Sort the customer names alphabetically and print the final list
# Using sort() to sort the list alphabetically
customers.sort()
print("Final sorted customer list:", customers)
