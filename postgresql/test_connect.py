import unittest
import postgresql
import os

class TestConnect(unittest.TestCase):

    def test_connect(self):
        url = os.environ.get("TEST_POSTGRESQL_URL", None)
        if url is None:
            self.skipTest("No TEST_POSTGRESQL_URL")
            return

        db = postgresql.open(url)
        test_statement = db.prepare("SELECT NOW()")
        print(test_statement())

