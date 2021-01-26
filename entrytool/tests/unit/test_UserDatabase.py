from unittest import TestCase

from entrytool.auth.UserDatabase import UserDatabase


class TestUserDatabase(TestCase):

    def setUp(self):
        self.user_db = UserDatabase("postgres", "3erm3TMBSj2wDtOh", "localhost", "5444", "OHDSI")

    def test_get_hashed_user_password(self):
        hashed_user_password = self.user_db.get_hashed_user_password("pmoorth1@its.jnj.com")
        print(hashed_user_password)
        self.assertIsNotNone(hashed_user_password)

    def test_check_password(self):
        check_ok = self.user_db.check_password("pmoorth1@its.jnj.com", "test")
        self.assertTrue(check_ok)
        check_ok = self.user_db.check_password("pmoorth1@its.jnj.com", "test1")
        self.assertFalse(check_ok)


