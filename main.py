class TwoNumbersOperations:
    def __init__(self, a=0.0, b=0.0):
        """
        The class initiates the calculus between two numbers
        :param a: The first number (default 0.0)
        :param b: The second number (default 0.0)
        """

        assert isinstance(a, float), "The first number may be a float"
        assert isinstance(b, float), "The second number may be a float"
        assert b!=0, "Division requires a second non-zero number"
        self.a = a
        self.b = b

    def addition2numbers(self):
        # Calculate the sum of two numbers
        return self.a + self.b

    def substraction2numbers(self):
        # Calculate the difference between two numbers
        return self.a - self.b

    def multiplication2numbers(self):
        # Calculate the multiplication of two numbers
        return self.a * self.b

    def division2numbers(self):
        # Calculate the division of two numbers
        return self.a / self.b


if __name__ == "__main__":
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    operation = TwoNumbersOperations(a, b)
    print("Addition : ", operation.addition2numbers())
    print("Substraction : ", operation.substraction2numbers())
    print("Multiplication : ", operation.multiplication2numbers())
    print("Division : ", operation.division2numbers())