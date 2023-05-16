"""Task 2 - breaking the inner loop
Your task is to write Python program (using break statement),
that prints:

in first line the numbers from 0 to 7,
in second line the numbers from 10 to 17,
and in third line the numbers from 20 to 27.
Hint: You can use nested loops!
Remember that the break statement terminates the loop containing it!

Your results could look like this:
0 1 2 3 4 5 6 7 

10 11 12 13 14 15 16 17 

20 21 22 23 24 25 26 27  """

# Solution 1
for i in range(3):  # Outer loop for three lines
    for j in range(8):  # Inner loop for numbers in each line
        num = i * 10 + j  # Calculate the number based on the line index and inner loop index
        print(num, end=' ')  # Print the number followed by a space
    print()  # Print a new line after each line of numbers
