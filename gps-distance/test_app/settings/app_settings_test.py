import unittest

import os
from app.settings.errors import ItemNotFoundError
from app.settings.app_settings import AppSettings


class SettingsTest(unittest.TestCase):

    def test_settings_file_doesnt_exist(self):
        settings_file = "./settings-does-not-exists-test.ini"

        self.assertFalse(os.path.exists(settings_file))
        settings = AppSettings(settings_file)
        self.assertTrue(os.path.exists(settings_file))

        if os.path.exists(settings_file):
            os.remove(settings_file)

    def test_settings_file_doesnt_exist_do_not_create_flag(self):
        settings_file = "./settings-does-not-exists-test.ini"

        self.assertFalse(os.path.exists(settings_file))
        settings = AppSettings(path=settings_file, create_if_not_exists=False)
        self.assertFalse(os.path.exists(settings_file))

        if os.path.exists(settings_file):
            os.remove(settings_file)

    def test_get_default_value(self):
        settings = AppSettings(path="./not-existent-file", create_if_not_exists=False)
        distance = settings.get_value("ARGUMENTS", "MAX_DISTANCE_IN_KM")

        self.assertEqual(distance, "10")

    def test_get_default_value_raise(self):
        settings = AppSettings(path="./not-existent-file", create_if_not_exists=False)

        distance = settings.get_value_raise("ARGUMENTS", "MAX_DISTANCE_IN_KM")
        self.assertEqual(distance, "10")

        self.assertRaises(ItemNotFoundError, lambda: settings.get_value_raise("Non-existent-section", "key"))

    def test_get_predefined_values_ok(self):
        settings = AppSettings(path="./settings_test.ini", create_if_not_exists=False)

        distance = settings.get_max_distance_in_km()

        self.assertEqual(distance, 5)

    def test_set_than_get(self):
        settings = AppSettings(path="./settings_test.ini", create_if_not_exists=False)

        settings.set_value("NEW-SECTION", "NEW-KEY", "VALUE")
        value = settings.get_value("NEW-SECTION", "NEW-KEY")

        self.assertEqual(value, "VALUE")

    def test_to_string(self):
        settings = AppSettings(path="./settings_test.ini", create_if_not_exists=False)

        str_repre = str(settings)

        print(str_repre)

        self.assertTrue("ARGUMENT" in str_repre)


if __name__ == "__main__":
    unittest.main()
