import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20"""
        prod_1 = Product('Test Product')
        self.assertEqual(prod_1.weight, 20)

    def test_default_product_weight(self):
        """Test default product flammability being 0.5"""
        prod_3 = Product('Test Product')
        self.assertEqual(prod_3.flammability, 0.5)

    def test_stealibility(self):
        """Test stealibility"""
        prod_2 = Product('Test Product')
        self.assertTrue "Kinda stealable" in prod_2.stealability

class AcmeReportTests(unittest.TestCase):
    """Making sure reports are working"""
    
    def test_default_num_products(self):
        """Test defualt number being 30"""
        x = generate_products()
        self.assertEqual(len(names), 30)

    def test_legal_names(self):
        """Check if the names are generated from Adj and nouns lists"""
        self.assertIn(ADJECTIVES, names)
        self.assertIn(NOUNS, names)

if __name__ == '__main__':
    unittest.main()