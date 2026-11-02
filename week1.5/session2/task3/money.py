# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated
        if not isinstance(pounds,(int,float)):
            raise TypeError("The pounds amount must be a number")
        if not isinstance(pounds,(pounds>=0)):
            raise ValueError("The amount must be a positive number")
        if not isinstance(pence,(int, float)):
            raise TypeError("The penny amount must be a number")
        if not isinstance(pence,(0<=pence<=99)):
            raise ValueError("The amount must be a positive number")

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')
        return f"£{self.pounds:.2f}.{self.pence:.2f}"

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        # Add code here to check that parameter 'other' is a Money object,
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
        total_pounds = self.pounds + other.pounds
        total_pence = self.pence + other.pence
        added_pounds = total_pence // 100
        remaining_pence = total_pence % 100
        final_pounds = total_pounds + added_pounds
        return Money(final_pounds, remaining_pence)
        
    def __str__(self):
        return f"£{self.pounds}.{self.pence:02d}"
