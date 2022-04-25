import unittest

from mal import User


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User("xinil")

    def test_user(self):
        self.assertEqual(self.user.user_id, 1)


if __name__ == "__main__":
    unittest.main()
