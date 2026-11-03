# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        takes the persons name and checks that the name is a string and birth is a integer
        """
        if not isinstance(name,(str)):
            raise TypeError("the name has to be letters only")
        if name.strip() == "":
            raise ValueError("the name section cant be empty ")
        if not isinstance(birth,(date)):
            raise TypeError("date of birth must be a date")
        
        self.name = name
        self.birth = birth

    def initials(self):
        """
        return the initials of the person by doing upperclasses
        """
        initial_letters = []

        for character in name:
            letter = character[0].upper()
            initial_letters.append(letter)

            result = "".join(initial_letters)
            return result
    def is_birthday(self):
        """
        returns true is its the person birthday today
        """
        today = date.today()
        return self.birth.month == today.month and self.birth.day == today.day
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
