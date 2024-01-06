import json
import unittest
from your_application_file import app

class TestEmployeeAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_employees(self):
        response = self.app.get('/employees')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 3)  # Assuming there are initially 3 employees

    def test_get_employee_by_id(self):
        response = self.app.get('/employees/1')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['name'], 'Ashley')

    def test_get_nonexistent_employee(self):
        response = self.app.get('/employees/100')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['error'], 'Employee does not exist')

    # Add more tests for other endpoints and edge cases as needed

if __name__ == '__main__':
    unittest.main()
