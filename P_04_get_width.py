# Ask user for width and loop until they
# enter a nuber that is more then zero

error = "Please enter a number tht is more than zaro\n"
    while True:

        try:
            # ask the user for a number
            width = float(input("Width: "))

            #check that the number is more then zero
            if width > 0:
                break
            else:
                print(error)

        except ValueError:
            print(error)
