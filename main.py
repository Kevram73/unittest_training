class TwoNumbersOperations:
    def __init__(self, a=0.0, b=0.0):
        """
        The class initiates the calculus between two numbers
        :param a: The first number (default 0.0)
        :param b: The second number (default 0.0)
        """

        assert isinstance(a, float), "Le premier nombre doit être un décimal"
        assert isinstance(b, float), "Le deuxième nombre doit être un décimal"
        assert b!=0, "La division requiert un second nombre non nul"
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
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le second nombre : "))
    operation = TwoNumbersOperations(a, b)
    print("Addition : ", operation.addition2numbers())
    print("Soustraction : ", operation.substraction2numbers())
    print("Multiplication : ", operation.multiplication2numbers())
    print("Division : ", operation.division2numbers())