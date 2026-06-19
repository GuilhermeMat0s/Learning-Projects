User_number = int(input("Enter any number to get its multiplication table: "))
counter = 0
while counter <= 10:
    result = counter * User_number
    print(f"{User_number} x {counter} = {result}")
    counter += 1