import unittest
from project import create_app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_upload_video(self):
        with open('tests/test_video.mp4', 'rb') as video:
            response = self.client.post('/upload', data={'file': video})
            self.assertEqual(response.status_code, 201)
            self.assertIn('File successfully uploaded', response.json['message'])

    def test_search_video(self):
        with open('tests/test_video.mp4', 'rb') as video:
            self.client.post('/upload', data={'file': video})
        
        response = self.client.get('/search', query_string={'filename': 'test_video.mp4'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('filename', response.json)

if __name__ == '__main__':
    unittest.main()
