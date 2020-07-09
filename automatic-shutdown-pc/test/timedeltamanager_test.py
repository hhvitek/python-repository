import unittest

from view.timedelta_manager import TimedeltaManager
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
        self.assertEqual(afterdelta, remaining)


if __name__ == "__main__":
    unittest.main()
