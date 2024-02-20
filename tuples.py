# Create a tuple with the values (1, 7, 2)
# Print the largest and smallest elements using the MAX and MIN function

tuple_1 = (1, 7, 2)

print("Higher: ", max(tuple_1))
print("Lowest: ", min(tuple_1))

# Create a script that receives two values from the user and stores them in two variables A and B, creates a tuple with the values A and B, and prints A*B

a = int(input("Write a value to A: "))
b = int(input("Write a value to B: "))

tuple_2 = (a, b)

print("tuple[0] * tuple[1] = ", a * b)

# Print the last 3 values of the tuple using the slice operator

tuple_3 = (2, 3, 5, 7, 11, 13)
print("The last three values are: ", tuple_3[-3:])

# Using the FOR loop, print all the even values from the tuple
tuple_4 = (2,5,9,6,12,44,48,45,47,100)

for i in tuple_4:
    if i % 2 == 0:
        print(i)