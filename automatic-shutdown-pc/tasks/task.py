#!/usr/bin/env python

from abc import ABC, abstractmethod


class Task(ABC):
    """Define an abstract task that can be scheduled by user"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.parameters = {}

    @staticmethod
    def get_all_tasks(tasks):
        pass

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_parameter(self, name, value):
        self.parameters[name] = value

    # returns parameter or None if it does not exist
    def get_parameter(self, name):
        return self.parameters.get(name)

    def get_parameters(self):
        return self.parameters

    # toString method
    def __str__(self):
        return f"Task: {self.name}"

    # unique representation of this object
    def __repr__(self):
        return str(self)

    @abstractmethod
    def execute(self):
        pass

    def is_auto_plannable(self):
        return False

    def plan_execution(self, seconds):
        pass

    def unplan_execution(self):
        pass
