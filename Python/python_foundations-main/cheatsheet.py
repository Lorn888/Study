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

def superify(name):
    return f"super{name}"

dog_result = superify("dog")
print(f"Look, it's {dog_result}!")
# Should print "Look, it's superdog!"

cat_result = superify(superify(superify("cat")))
print(f"Look, it's {cat_result}!")
# Should print "Look, it's supersupersupercat!"