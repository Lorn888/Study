# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==


def are_special_characters_present(password):
    if (("!") in password or ("@") in password or ("$") in password or ("%") in password or ("&") in password):
        return True
    else:
        return False

def sufficient_length(password):
    return len(password) > 7
        
def is_valid(password):
    if are_special_characters_present(password) and sufficient_length(password):
        return True
    else:
        return False