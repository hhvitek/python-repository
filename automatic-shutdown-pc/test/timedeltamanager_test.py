import unittest

from model.timedelta_manager import TimedeltaManager
from datetime import datetime, timedelta


class TimedeltaManagerTest(unittest.TestCase):
    def setUp(self):
        self.manager = TimedeltaManager()

    def test_setting_when_elapsed_using_afterdelay(self):

        afterdelta = "02:15"
        self.manager.set_when_elapsed_using_afterdelta(afterdelta)

        expected_when_elapsed = datetime.now() + timedelta(hours=2.0, minutes=15.0)

        self.assertEqual(
            expected_when_elapsed.strftime("%H:%M"), self.manager.get_when_elapsed()
        )

    def test_get_remaining(self):
        afterdelta = "02:15"
        self.manager.set_when_elapsed_using_afterdelta(afterdelta)

        remaining = self.manager.get_remaining()
        self.assertEqual(afterdelta + ":00", remaining)

    def test_create_instance_from_incorrect_string(self):
        correct_string = "05:30"
        incorrect_string = "incorrect_string"
        self.manager.set_when_elapsed_using_afterdelta(incorrect_string)

        self.assertTrue(self.manager.has_elapsed())
        self.assertEqual("00:00:00", self.manager.get_remaining())

    def test_create_instance_from_slightly_incorrect_string(self):
        correct_string = "05:30"
        incorrect_string = "05:XX"
        self.manager.set_when_elapsed_using_afterdelta(incorrect_string)

        self.assertTrue(self.manager.has_elapsed())
        self.assertEqual("00:00:00", self.manager.get_remaining())

    def test_is_valid_afterdelta_correct_and_incorrect(self):
        correct_string = "05:30"
        incorrect_string = "05:XX"

        self.assertTrue(TimedeltaManager.is_valid_str_afterdelta(correct_string))
        self.assertFalse(TimedeltaManager.is_valid_str_afterdelta(incorrect_string))


if __name__ == "__main__":
    unittest.main()
