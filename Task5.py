"""Task 5 - only digits
Your task is to write a Python program using loop, that iterates over the entered string and counts sum of the digits in the string.
User should be prompted to enter her/his characters with the keyboard, even without looking at it.
Store the information about sum of the digits.
Program should terminate after encountering '=' character in the string (if it is present there).

Hint: use one of the string's method and try to type only letters and digits!

Your results could look like this:
Input your characters: gh1ghghg2huhjhjh3gghgv4gvgyg5ggygygyg6ygyg

Found a digit  1
Found a digit  2
Found a digit  3
Found a digit  4
Found a digit  5
Found a digit  6

Sum of digits:  21
...
Input your characters: ncuuuhuh2huhu3uhu4hhu5uhuhuhu6hh=hfd6def

Found a digit  2
Found a digit  3
Found a digit  4
Found a digit  5
Found a digit  6

Exit after finding '=' sign """

# Solution
user_input = input("Input your characters: ")  # Prompt the user to enter a string

sum_of_digits = 0  # Initialize the variable to store the sum of digits

for char in user_input:  # Iterate over each character in the user input
    if char.isdigit():  # Check if the character is a digit
        digit = int(char)  # Convert the digit character to an integer
        print("Found a digit", digit)  # Print a message indicating a digit is found
        sum_of_digits += digit  # Add the digit to the sum_of_digits variable
    if char == '=':  # Check if the character is '='
        print("Exit after finding '=' sign")  # Print a message indicating the termination condition is met
        break  # Terminate the loop if '=' is found

print("Sum of digits:", sum_of_digits)  # Print the final sum of digits
