#!/usr/bin/env python

import logging


class Model:
    def __init__(self, tasks):
        self.tasks_list = tasks
        self.tasks_dict = self._convert_tasks_list_to_dict(tasks)

    def _convert_tasks_list_to_dict(self, tasks):
        tasks_dict = {}
        for task in tasks:
            tasks_dict[task.get_name()] = task
        return tasks_dict

    def get_tasks(self):
        return self.tasks_list

    def get_task(self, task_name):
        return self.tasks_dict.get(task_name)
