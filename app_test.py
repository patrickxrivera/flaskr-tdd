import unittest
import os
import tempfile

import app


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_db(self):
        tester = os.path.exists('flaskr.db')
        self.assertEqual(tester, True)


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        app.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    def login(self, username, password):
        credentials = dict(username=username, password=password)
        return self.app.post('/login', data=credentials, follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    # assert functions

    def test_empty_db(self):
        rv = self.app.get('/')


if __name__ == '__main__':
    unittest.main()
