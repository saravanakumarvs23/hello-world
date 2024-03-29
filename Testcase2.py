''' An if statement can be used to conditionally execute code, depending on whether the "if" statement's condition is True or False.
An elif (that is, "else if") statement can follow an if statement. Its block executes if its condition is True and all the previous conditions have been False.
An else statement comes at the end. Its block is executed if all of the previous conditions have been False.
The values 0 (integer), 0.0 (float), and ‘‘ (the empty string) are considered to be "falsey" values. When used in conditions they are considered False. You can always see for yourself which values are truthy or falsey by passing them to the bool() function.'''

password ='saravana'
if password == 'saravana':
    print("Access Granted.....")
    print("Done...")
else:
    print("Access Denied")

=================================================

print("Enter you name:")
name = input()
if name != '':
    print("Thank you for entering a name...")
else:
    print("You did not enter a name...")