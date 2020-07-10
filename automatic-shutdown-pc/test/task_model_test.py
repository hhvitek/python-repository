import unittest

from model.task_model import TaskModel
from tasks.task_exception import TaskError


class TaskModelTest(unittest.TestCase):
    def setUp(self):
        tasks_active = [
            "tasks.shutdown_task.ShutdownTask",
            "tasks.restart_task.RestartTask",
        ]
        self.task_model = TaskModel(tasks_active)

    def test_execute_shutdown_ok(self):

        task_name = "Shutdown"
        result = self.task_model.execute_task(task_name)
        self.assertEqual(result, "OK")

    def test_execute_unknown_raise(self):
        task_name = "Unknown"
        self.assertRaises(ValueError, lambda: self.task_model.execute_task(task_name))

    def test_execute_restart_raise(self):
        task_name = "Restart"
        self.assertRaises(TaskError, lambda: self.task_model.execute_task(task_name))


if __name__ == "__main__":
    unittest.main()
