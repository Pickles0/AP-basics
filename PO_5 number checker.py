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

#main routine goes here
for item in range(0, 2):
    width = num_check("width: ")
    print(width)

print()

for item in range(0, 2):
    height = num_check("height: ")
    print(height)
    