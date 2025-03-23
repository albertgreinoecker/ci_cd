import unittest
from ex_04_test_flask_server import app

class TestFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Wird einmal vor allen Tests ausgeführt."""
        cls.client = app.test_client()

    def test_hello_route(self):
        """Testet die /api/hello Route"""
        response = self.client.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hallo, Welt!"})

if __name__ == '__main__':
    unittest.main()