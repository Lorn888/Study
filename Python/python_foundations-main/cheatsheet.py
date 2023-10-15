def add_two_numbers(num1,num2):
    print(num1 + num2)

add_two_numbers(2,5)

def add_three_numbers(num1, num2, num3):
    print(num1+num2+num3)

add_three_numbers(1,7,6)

def friend_names(name1, name2):
    return f"My mate {name1} and {name2}"

print(friend_names("Marcin", "Hasan"))

def seconds_in_a_week(weeks):
    return 60*60*24*7*weeks

print(seconds_in_a_week(4))