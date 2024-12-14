import unittest

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        from shopping_cart import ShoppingCart, Item
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Apple", 2.50, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].name, "Apple")

    def test_remove_item(self):
        self.cart.add_item("Apple", 2.50, 3)
        self.cart.add_item("Banana", 1.00, 2)
        self.cart.remove_item("Apple")
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].name, "Banana")

    def test_total_cost(self):
        self.cart.add_item("Apple", 2.50, 3)  # Total: 7.50
        self.cart.add_item("Banana", 1.00, 2)  # Total: 2.00
        self.assertEqual(self.cart.total_cost(), 9.50)








