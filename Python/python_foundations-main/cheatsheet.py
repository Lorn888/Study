# # # # def add_two_numbers(num1,num2):
# # # #     print(num1 + num2)

# # # # add_two_numbers(2,5)

# # # # def add_three_numbers(num1, num2, num3):
# # # #     print(num1+num2+num3)

# # # # add_three_numbers(1,7,6)

# # # # def friend_names(name1, name2):
# # # #     return f"My mate {name1} and {name2}"

# # # # print(friend_names("Marcin", "Hasan"))

# # # # def seconds_in_a_week(weeks):
# # # #     return 60*60*24*7*weeks

# # # # print(seconds_in_a_week(4))

# # # # def superify(name):
# # # #     return f"super{name}"

# # # # dog_result = superify("dog")
# # # # print(f"Look, it's {dog_result}!")
# # # # # Should print "Look, it's superdog!"

# # # # cat_result = superify(superify(superify("cat")))
# # # # print(f"Look, it's {cat_result}!")
# # # # # Should print "Look, it's supersupersupercat!"

# # # # def swap_the_case_of_a_string(string):
# # # #     # your code goes here (delete the pass below)
# # # #     new = ""
# # # #     for x in string:
# # # #         if x == x.lower():
# # # #             new += x.upper()
# # # #         else:
# # # #             new += x.lower()
# # # #     return new

# # # # print(swap_the_case_of_a_string("sMe string"))

# # # def is_integer_odd(integer):
# # #     # your code goes here (delete the pass below)
# # #     if integer % 2 == 0:
# # #         print(True)
# # #     else:
# # #         print(False)

# # # is_integer_odd(1)

# # # def starts_with_the_letter_a(string):
# # #     # your code goes here (delete the pass below)
# # #     for letters in string:
# # #         if letters[0].lower() == "a":
# # #             return True
# # #         else:
# # #             return False

# # def ends_with_the_letter_a(string):
# #     # your code goes here (delete the pass below)
# #         return string[-1]

# def remove_x(string):
#     # your code goes here (delete the pass below)
#     x = string.replace("x","")
#     y = x.replace("X","")
#     return y

def first_half(string):
    # your code goes here (delete the pass below)
    x = int(len(string)/2)
    return string(range(0, x))
