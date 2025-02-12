"""Story
Your friend recently started an e-commerce business where people can buy little animals like reptilians, snakes, and snails. You have created a basic webshop for the startup.

Before any purchase the customers need to create an account. Unfortunately, 10% of the users give invalid email addresses on the form, and they cannot be reached again. It's your jo
 to fix this problem, and write a basic email validator for the registration page.

*"A valid email address looks like this: username@do.ma.in. The first part is called username, the second part (after the '@') is the domain. A valid address must follow these rules:

There is exactly one '@' character in it. Neither the username nor the domain can be empty or start with a . character. There is at least one . character in the domain, and the top-level domain (the last part of it) must be at least two characters long."*

Tasks
1. At least one '@'
The validator should give an error when there are no '@' characters in the email address.

Writing the email hello.worldcom, the program prints An email address has to contain a '@' character!.
2. Only one '@'
The validator should give an error when there are more then one '@' characters are in the email address.

Writing the email he@@llo@@worldcom, the program prints An email address cannot contain more than one '@' characters!"
3. Username is not empty
The validator should give an error when the username is empty.

Writing the email @@world.com, the program prints The username before the '@' character cannot be empty!
4. Domain is not empty
The validator should give an error when the domain is empty.

Writing the email hello@, the program prints The domain after the '@' character cannot be empty!
5. At least one '.'
The validator should give an error when there are no . characters in the email address.

Writing the email hello@@worldcom, the program prints An email address has to contain at least one '.' character!
6. At least one '.' in domain
The validator should give an error when there are no . characters in the domain.

Writing the email hell.o@@worldcom, the program prints The domain has to contain at least one '.' character!
7. Top-level domain is not empty
The validator should give an error when the domain ends with a . character.

Writing the email hello@@worldcom., the program prints The top-level domain cannot be empty!
8. TLD is at least two characters long
The validator should give an error when the last part of the domain is less than two characters long.

Writing the email hello@@worldco.m, the program prints The top-level domain has to be at least two characters long!
9. Valid username
The validator should give an error when the username starts with a . character.

Writing the email .hello@@world.com, the program prints The username cannot start with a '.' character!
10. Valid server name
The validator should give an error when the first part of the domain is empty.

Writing the email he.llo@.world.com, the program prints The domain cannot start with a '.' character!
11. Valid email address
The validator should recognize a valid email address.

Writing the email hello@world.com, the program prints Valid email address :)
Hints
Use the given count and position values to create the error conditions. You won't need any other values for the solution.

You won't need it here as the values are given, but in other situations you would have to search the internet for expressions like python count number of characters in a string or python find last occurrence in a string, and adapt the found code snippets to your needs.

The position of the last character is length_of_email - 1.

The positions of neighboring characters differ by 1.

Be sure to structure your conditions in a logical way (e.g. do not check for a valid server name before confirming that there is at least a `` and a . present).

Background materials
Conditional Statements in Python:
https://realpython.com/python-conditional-statements/

Strings:
https://www.w3schools.com/python/python_strings.asp
"""

email = input("Your email address: ")

# "hello.worldcom"    => An email address has to contain a '@' character!
# "he@llo@world.com"  => An email address cannot contain more than one '@' characters!
# "@world.com"        => The username before the '@' character cannot be empty!
# "hello@"            => The domain after the '@' character cannot be empty!
# "hello@worldcom"    => An email address has to contain at least one '.' character!
# "hell.o@worldcom"   => The domain has to contain at least one '.' character!
# "he.llo@worldcom."  => The top-level domain cannot be empty!
# "he.llo@worldco.m"  => The top-level domain has to be at least two characters long!
# ".hello@world.com"  => The username cannot start with a '.' character!
# "he.llo@.world.com" => The domain cannot start with a '.' character!
# "hello@world.com"   => Valid email address :)


length_of_email = len(email)
number_of_at_characters = email.count("@")
number_of_dot_characters = email.count(".")
position_of_at = email.find("@")

position_of_first_dot = email.find(".")
position_of_last_dot = email.rfind(".")
position_of_first_dot_after_the_at = email.find(".", position_of_at)


error_message_no_at = "An email address has to contain a '@' character!"
error_message_too_many_at = "An email address cannot contain more than one '@' characters!"
error_message_no_dot = "An email address has to contain at least one '.' character!"
error_message_no_username = "The username before the '@' character cannot be empty!"
error_message_no_dot_in_domain = "The domain has to contain at least one '.' character!"
error_message_no_server_name = "The domain cannot start with a '.' character!"
error_message_no_tld = "The top-level domain cannot be empty!"
error_message_short_tld = "The top-level domain has to be at least two characters long!"
error_message_no_domain = "The domain after the '@' character cannot be empty!"
error_message_invalid_username = "The username cannot start with a '.' character!"

if '@' not in email:
    print("An email address has to contain a '@' character!")
    is_valid = False
else:
    ok_message = "Valid email address :)"
    is_valid = True

    if email.count("@") > 1 :
        print(error_message_too_many_at)
        is_valid = False

    username, domain = email.split('@')
    if email.count(".") < 1 :
        username, domain = email.split('@')
        print(error_message_no_dot)

    if len(username) == 0:
        is_valid = False
        print(error_message_no_username)

    if domain.count(".") < 1:
        print(error_message_no_dot_in_domain)
        is_valid = False

    elif username[0] == '.':
        print(error_message_no_server_name)
        is_valid = False

    if len(domain) == 0:
        print(error_message_no_tld)
        is_valid = False

    if len(domain) < 2:
        print(error_message_short_tld)
        is_valid = False
    
    if len(domain) < 1:
        print(error_message_no_domain)
        is_valid = False

if is_valid:
    print("Valid email address ")
    
