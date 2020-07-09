import unittest

from model.model import Model
from tasks.restart_task import RestartTask
from tasks.shutdown_task import ShutdownTask
from view.window_creator import WindowCreator


class WindowCreatorTest(unittest.TestCase):
    def setUp(self):
        tasks = [ShutdownTask(), RestartTask()]
        model = Model(tasks)
        self.creator = WindowCreator(model)

    def test_generator_sequence(self):
        step_in_minutes = 30
        sequence = self.creator._generate_time_sequence(step_in_minutes)
        self.assertEqual(24, len(sequence))
        self.assertEqual("00:00", sequence[0])
        self.assertEqual("11:30", sequence[-1])


if __name__ == "__main__":
    unittest.main()
