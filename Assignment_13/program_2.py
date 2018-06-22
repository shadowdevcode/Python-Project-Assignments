"""
Create a user-defined exception AgeTooSmallError()
that warns the user when they have entered age less than 18.
The code must keep taking input till the user enters the appropriate age number(less than 18).
"""


class AgeTooSmallError(ValueError):

    pass


while True:
    try:
        age = int(input("Enter age: "))
        if age > 18:
            raise AgeTooSmallError
        break
    except ValueError:
        print("Oops! You entered wrong age.Enter appropriate age number which is less than 18")
print("Congratulations! You guessed it right")
