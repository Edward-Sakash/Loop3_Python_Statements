"""Task 1 - omitting the number
Your task is to write Python program that prints in one line all the numbers from 0 to 8 except 3 and 6

Your results should look like this:
0 1 2 4 5 7 8"""

# Solution 1
# Iterate through the numbers from 0 to 8
for num in range(9):
    # Check if the number is 3 or 6
    if num == 3 or num == 6:
        continue  # Skip the current iteration
    
    # Print the number
    print(num, end=' ')  # Print with a space separator

# Print a new line after all the numbers have been printed
print()

print("____________________________________________________")

# Solution 2
num = 0  # Initialize the variable 'num' to 0

while num <= 8:  # Continue the loop until 'num' reaches 8
    if num != 3 and num != 6:  # Check if 'num' is not equal to 3 and not equal to 6
        print(num, end=' ')  # Print the value of 'num' followed by a space
    num += 1  # Increment 'num' by 1 in each iteration

print()  # Print a new line after all the numbers have been printed
