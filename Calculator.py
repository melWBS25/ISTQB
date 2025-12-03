class Calculator:
    """Eine einfache Taschenrechner-Klasse"""

    def addiere(self, a, b):
        """Addiert zwei Zahlen"""
        return a + b

    def subtrahiere(self, a, b):
        """subtrahiert zwei Zahlen"""
        return a - b

    def dividiere(self, a, b):
        """subtrahiert zwei Zahlen"""
        if b == 0:
            raise ValueError("Division durch Null ist nicht erlaubt")
        return a / b
