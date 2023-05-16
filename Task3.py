"""Task 3 - break or continue
Your task is to write Python program (using continue and break statements), that reads (prompts) two integers.

If first number is smaller than second number, then find all numbers between them that are divisible by 3 and print them out. Use continue statement!

If first number is bigger than second number, then find first number between them that is divisible by 5 and print it out. Start iterating from bigger number and use break statement!

If numbers are equal only print that information!

Your results could look like this:
First number: 1
Second number: 11

3  is divisible by 3.
6  is divisible by 3.
9  is divisible by 3.

Finished iterating from 1  to 11

...

First number: 11
Second number: 1

10  is divisible by 5.

...

First number: 3
Second number: 3

Nothing to do, both numbers are equal!"""

# Solution 
# Prompt the user for the first and second numbers
first_number = int(input("First number: "))
second_number = int(input("Second number: "))

# Check if the first number is smaller than the second number
if first_number < second_number:
    print("First number:", first_number)
    print("Second number:", second_number)

    # Iterate from first_number+1 to second_number-1
    for num in range(first_number + 1, second_number):
        # Check if the number is divisible by 3
        if num % 3 == 0:
            print(num, "is divisible by 3.")

    # Print a message if there are no divisible numbers
    if first_number + 1 >= second_number:
        print("No numbers between them are divisible by 3.")

    print("Finished iterating from", first_number, "to", second_number)
    print()

# Check if the first number is bigger than the second number
elif first_number > second_number:
    print("First number:", first_number)
    print("Second number:", second_number)

    # Iterate from first_number to second_number+1 in reverse order
    for num in range(first_number, second_number - 1, -1):
        # Check if the number is divisible by 5
        if num % 5 == 0:
            print(num, "is divisible by 5.")
            break  # Terminate the loop

    print("Finished iterating from", first_number, "to", second_number)
    print()

# Check if the numbers are equal
else:
    print("First number:", first_number)
    print("Second number:", second_number)
    print("Nothing to do, both numbers are equal!")
    print()

