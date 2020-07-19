#!/usr/bin/env python

import logging
from .class_loader import ClassLoader


class TaskModel:
    """
    Represents interface to tasks(operations) supported by application.
    It's static data and task's behaviour
    """

    def __init__(self, tasks_module_names):
        """
        It's possible to initialize app with only subset of requires tasks (tasks_module_names parameter)
        """
        self.tasks = self._get_tasks_from_tasks_modules(tasks_module_names)
        self.tasks_dict = self._convert_tasks_list_to_dict(self.tasks)

    def _get_tasks_from_tasks_modules(self, tasks_module_names):
        tasks = []
        for task_module in tasks_module_names:
            task = ClassLoader.from_string(task_module)
            tasks.append(task)
        return tasks

    def _convert_tasks_list_to_dict(self, tasks):
        tasks_dict = {}
        for task in tasks:
            tasks_dict[task.get_name()] = task
        return tasks_dict

    def get_tasks_names(self):
        tasks_names = []
        for task in self.tasks:
            tasks_names.append(task.get_name())
        return tasks_names

    def get_tasks(self):
        return self.tasks

    def get_task(self, task_name):
        return self.tasks_dict.get(task_name)

    def execute_task(self, task_name, parameter=None):
        if task_name not in self.tasks_dict:
            error_message = f"Neznámá akce: <{task_name}>. Neprovedena žádná akce."
            logging.error(error_message)
            raise ValueError(error_message)
        else:
            task = self.tasks_dict[task_name]
            result_message = task.execute(parameter)
            logging.info("Task <{task_name}> executed. Parameter <{parameter}>")
            return result_message
