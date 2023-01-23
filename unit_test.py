import unittest
from pass_api import app

class TestPasswordGeneration(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_generate_password(self):
        response = self.client.get('/generate/10')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'password', response.data)
        self.assertEqual(len(response.json['password']), 10)
        
    def test_generate_password_custom(self):
        response = self.client.get('/generate-custom/15?animals=true')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'password', response.data)
        self.assertEqual(len(response.json['password']), 15)

if __name__ == '__main__': 
  unittest.main()
