# ask user for width and loop until they
# enter a number that is larger than zero
def num_check(question):

    error = "Please enter a number that is more than zero"

    while True :

        try:
            # ask user for a number
            response = float(input(question))
            #check number is more than zero
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

# main routine starts here...

keep_going = ""
while keep_going == "":
    # get width and height
    width = num_check("width: ")
    height = num_check("height: ")
    # calculate area/perimeter
    area = width * height
    perimeter = 2 * (width + height)
    # Display output
    print()
    print(f"perimeter: {perimeter} units")
    print(f"area: {area} square units")
    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()
    print("Thank you for using the area perimeter calculator")
