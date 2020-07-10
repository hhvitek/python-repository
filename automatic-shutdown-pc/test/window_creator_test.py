import unittest

from model.task_model import TaskModel
from view.window_creator import WindowCreator


class WindowCreatorTest(unittest.TestCase):
    def setUp(self):
        tasks_active = [
            "tasks.shutdown_task.ShutdownTask",
            "tasks.restart_task.RestartTask",
        ]
        self.task_model = TaskModel(tasks_active)
        tasks = self.task_model.get_tasks()

        self.creator = WindowCreator(tasks)

    def test_generator_sequence(self):
        step_in_minutes = 30
        sequence = self.creator._generate_time_sequence(step_in_minutes)
        self.assertEqual(24, len(sequence))
        self.assertEqual("00:00", sequence[0])
        self.assertEqual("11:30", sequence[-1])


if __name__ == "__main__":
    unittest.main()
