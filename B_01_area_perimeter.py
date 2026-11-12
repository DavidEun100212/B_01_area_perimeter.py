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


keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    height = num_check("height: ")

    # calculate the area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
