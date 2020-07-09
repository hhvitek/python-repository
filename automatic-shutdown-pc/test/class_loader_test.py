import unittest
import tasks
from model.class_loader import ClassLoader
from tasks.shutdown_task import ShutdownTask
from tasks.restart_task import RestartTask


class ClassLoaderTest(unittest.TestCase):
    def test_load_shutdown(self):
        loader = ClassLoader()
        modulename = "tasks.shutdown_task"
        classname = "ShutdownTask"

        shutdown_instance = loader.from_module_classname(modulename, classname)

        self.assertIsInstance(shutdown_instance, ShutdownTask)

    def test_load_restart(self):
        loader = ClassLoader()
        modulename = "tasks.restart_task"
        classname = "RestartTask"

        restart_instance = loader.from_module_classname(modulename, classname)

        self.assertIsInstance(restart_instance, RestartTask)

    def test_load_nonexistent_class(self):
        loader = ClassLoader()
        modulename = "tasks.shutdown_task"
        classname = "NonExistentTask"
        self.assertRaises(
            AttributeError, lambda: loader.from_module_classname(modulename, classname)
        )

    def test_load_nonexistent_module(self):
        loader = ClassLoader()
        modulename = "tasks.nonexistent_task"
        classname = "ShutdownTask"
        self.assertRaises(
            ModuleNotFoundError,
            lambda: loader.from_module_classname(modulename, classname),
        )

    def test_load_shutdown_from_string(self):
        loader = ClassLoader()
        modulename_classname = "tasks.shutdown_task.ShutdownTask"
        shutdown_instance = loader.from_string(modulename_classname)

        self.assertIsInstance(shutdown_instance, ShutdownTask)

    def test_get_modules_names_from_path(self):
        expected_found_tasks = 2
        modulename_endswith = "_task"

        loader = ClassLoader()
        module_path = tasks.__path__

        modules_names = loader.get_modules_names(module_path, modulename_endswith)

        self.assertEqual(expected_found_tasks, len(modules_names))


if __name__ == "__main__":
    unittest.main()
