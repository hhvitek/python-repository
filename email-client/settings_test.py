import unittest

from settings import Settings


class SettingsTest(unittest.TestCase):
    def setUp(self):
        self.settings = Settings("./settings_test.ini")

    def test_default_values(self):
        self.assertEqual("test_username", self.settings.get_username())
        self.assertEqual("test_password", self.settings.get_password())

    def test_get_login_values_ok(self):

        self.settings.set_value("LOGIN", "PASSWORD", "passwd")
        self.settings.set_value("LOGIN", "USERNAME", "user")

        self.assertEqual("passwd", self.settings.get_password())
        self.assertEqual("user", self.settings.get_username())

    def test_get_nonexistent_values_returns_none(self):

        self.settings.set_value("LOGIN", "PASSWORD", "passwd")
        self.settings.set_value("LOGIN", "USERNAME", "user")

        non_existent_value = self.settings.get_value(
            "NON_EXISTENT_SECTION", "NON_EXISTENT_VALUE"
        )

        self.assertIsNone(non_existent_value)


if __name__ == "__main__":
    unittest.main()
