import json
import unittest
from app import app

class TestApp(unittest.TestCase):

    def test_check_number_low(self):
        with app.test_client() as client:
            response = client.get('/number/50')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['number'], 50)
            self.assertEqual(data['message'], 'low')

    def test_check_number_high(self):
        with app.test_client() as client:
            response = client.get('/number/150')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['number'], 150)
            self.assertEqual(data['message'], 'high')

if __name__ == '__main__':
    unittest.main()
