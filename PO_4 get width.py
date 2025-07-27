# ask user for width and loop until they
# enter a number that is larger than zero

error = "Please enter a number that is more than zero"

while True :

    try:
        # ask user for a number
        width = float(input("width: "))
        #check number is more than zero
        if width > 0:
            break
        else:
            print(error)
    except ValueError:
        print(error)