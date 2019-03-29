import identidock
import unittest

class TestCase(unittest.TestCase):
    def setUp(self):
        identidock.app.config["TESTING"] = True
        self.app = identidock.app.test_client()

    def test_get_main_page(self):
        page = self.app.post("/", data=dict(name="Moby Dock"))
        self.assertEqual(page.status_code, 200)
        self.assertIn("Moby Dock", str(page.data))

    def test_html_escaping(self):
        page = self.app.post("/", data=dict(name="><h1>Beware</h1><!--"))
        self.assertNotIn(">Beware", str(page.data))

# TODO add test to get monster image, mock api
# https://realpython.com/testing-third-party-apis-with-mock-servers/


if __name__ == "__main__":
    unittest.main()
