#Password Checker

# need a class
# init - password to be passed through on object creation. 
# 1 method to return strength of self.password:
# returns a string:
# very weak - weak- medium - strong - very strong
# length, !alphanumeric, capitals
# check against a small list of known passwords. - return very weak by default.  
# avoid dependancies (core logic)

class Password:
    def _init_(self, length, special, numbers):
        self.length = length
        self.special = special
        self.numbers = numbers


def check_password():
    user_input = input("Please enter a password: ")
    common_passwords = ["password", "password1", "favesport", "birthday"]
    special_characters = ("!, @, #, $, %, ^, &, *, (, ), (), _, +, -, =, {,}, {}, |, \\, :, ;, , ', <, >, ?, /, ., *, -, $, €, £, ¥, ~, `, <<, >>,")
    contains_digit = any(char.isdigit() for char in user_input)
    length = len(user_input)


    if user_input in common_passwords:
        print (f"Use a safer password.'{user_input}' is very weak.")

    elif length <= 6:
        print ("Your password is very weak, as it is too short.")

    elif not contains_digit:
        print ("Your password is weak. Please add numbers.")

    elif length <=6 and (not contains_digit or any(special_characters for char in user_input)):
        print("Your password is VERY weak.")

    elif length >=6 and (contains_digit or any(special_characters for char in user_input)):
        print("Your password is strong.")

    elif length >=6 and contains_digit and any(special_characters for char in user_input):
        print("Your passwors is very strong!")   

check_password()    