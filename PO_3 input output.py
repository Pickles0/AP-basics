# ask the user for their name
username = input("What is your name?")
# ask the user for their favourite number (integer)
fav_num = int(input("What is your favourite number?"))
# double half and square the users favourite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num
# greet user
print()
print(f"Hi {username} your favourite number is {fav_num} ")
# output the results of doubling halving and
# squaring the users favourite integer
print(f"Double {fav_num} is {double}")
print(f"half of {fav_num} is {halve}")
print(f"{fav_num} squared is {square}")
print()
print("Have a nice day.")