"""test"""

class Addition:
    """Cette classe représente une opération d'addition."""
    def __init__(self, a, b):
        """Initialise une instance de l'opération d'addition avec deux nombres."""
        self.a = a
        self.b = b

    def calculate(self):
        """Effectue l'opération d'addition et retourne le résultat."""
        return self.a + self.b


class Soustraction:
    """Cette classe représente une opération de soustraction."""
    def __init__(self, a, b):
        """Initialise une instance de l'opération de soustraction avec deux nombres."""
        self.a = a
        self.b = b

    def calculate(self):
        """Effectue l'opération de soustraction et retourne le résultat."""
        return self.a - self.b

class Division:
    """Cette classe représente une opération de division."""
    def __init__(self, a, b):
        """Initialise une instance de l'opération de division avec deux nombres."""
        self.a = a
        self.b = b

    def calculate(self):
        """Effectue l'opération de division et retourne le résultat."""
        if self.b != 0:
            return self.a / self.b
        return "Impossible de diviser par zéro"
