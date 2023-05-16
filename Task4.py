"""Task 4 - dividor game
Your task is to write Python program (using continue and break statements), that reads (prompts) two integers.

First integer must be bigger than 100 and must be odd!
Second integer must be must be odd!

If first number is divisible by second number, then you'll get one "point" (some variable increases by 1) and you can continue typing numbers. Use continue statement!

If first number is not divisible by second number, then you'll quit the game. Use break statement!

Print out information about points!

Note: You can treat this exercise as a practice in dividing numbers in your head 😃

Your results could look like this:
First number: 123
Second number: 3
You earned a point!

First number: 245
Second number: 5
You earned a point!

First number: 347
Second number: 7
You've made a mistake!

You gathered  2 point(s)!"""

# Solution 
points = 0  # Initialize the points variable to 0

while True:
    first_number = int(input("First number: "))
    second_number = int(input("Second number: "))

    # Check if the first number is odd and greater than 100
    if first_number % 2 != 0 and first_number > 100:
        # Check if the first number is divisible by the second number
        if first_number % second_number == 0:
            print("You earned a point!")
            points += 1  # Increase the points by 1
            continue  # Continue to the next iteration of the loop

        else:
            print("You've made a mistake!")
            break  # Terminate the loop

    else:
        print("Invalid input. First number must be odd and greater than 100.")
        continue  # Continue to the next iteration of the loop

print("You gathered", points, "point(s)!")
