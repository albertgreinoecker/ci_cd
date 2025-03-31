import unittest

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def add(self, money):
        if self.currency != money.currency:
            raise ValueError("Currency mismatch")
        return Money(self.amount + money.amount, self.currency)

    def __str__(self):
        return f"{self.amount} {self.currency}"

class MoneyTest(unittest.TestCase):
    def setUp(self):
        """Vorbereitung vor jedem Test"""
        self.money1 = Money(100, "EUR")
        self.money2 = Money(50, "USD")
    # Run tests

    def test_add_same_currency(self):
        result = self.money1.add(self.money1)
        self.assertEqual(result.amount, 200)
        self.assertEqual(result.currency, "EUR")

    def test_add_different_currency(self):
        with self.assertRaises(ValueError):
            self.money1.add(self.money2)


if __name__ == '__main__':
    unittest.main()
