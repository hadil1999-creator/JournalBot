import unittest
from unittest.mock import patch
from app_folder import app

class TestNLPWebApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch('app.call_github_nlp_api')  # Mock external API call
    def test_analyze_success(self, mock_nlp):
        mock_nlp.return_value = {"summary": "This is a test summary."}

        response = self.client.post('/analyze', json={
            "text": "Write a function to sort a list."
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn("summary", response.get_json())

    def test_analyze_missing_input(self):
        response = self.client.post('/analyze', json={})
        self.assertEqual(response.status_code, 400)

    @patch('app.call_github_nlp_api')
    def test_analyze_github_api_failure(self, mock_nlp):
        mock_nlp.side_effect = Exception("GitHub API failed")

        response = self.client.post('/analyze', json={
            "text": "def foo(): pass"
        })

        self.assertEqual(response.status_code, 500)
        self.assertIn("error", response.get_json())

if __name__ == '__main__':
    unittest.main()
