#!/usr/bin/env python

from abc import ABC, abstractmethod
from .task_exception import TaskError


class Task(ABC):
    """Define an abstract task that can be scheduled by user"""

    def __init__(self, name, description, accept_parameter=False):
        self.name = name
        self.description = description

        self.accept_parameter = accept_parameter

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def accept_parameter(self):
        return self.accept_parameter

    # toString method
    def __str__(self):
        return f"Task: {self.name}"

    # unique representation of this object
    def __repr__(self):
        return str(self)

    @abstractmethod
    def execute(self, parameter=None):
        """
            Returns string message

            on error raises TaskError exception
        """
        raise TaskError("Execute method is not overriden!")