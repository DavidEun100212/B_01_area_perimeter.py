# Ask user for width and loop until they
# enter a nuber that is more then zero
def num_check(question):

    error = "Please enter a number tht is more than zaro\n"
    while True:

        try:
            # ask the user for a number
            response = float(input("Width: "))

            #check that the number is more then zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine Goes Here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

print()

for item in range(0, 2):
    height = num_check("Height: ")
    print(height)
