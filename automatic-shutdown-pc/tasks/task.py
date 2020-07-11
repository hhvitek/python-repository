#!/usr/bin/env python

from abc import ABC, abstractmethod
from .task_exception import TaskError


class Task(ABC):
    """Define an abstract task that can be scheduled by user"""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    # toString method
    def __str__(self):
        return f"Task: {self.name}"

    # unique representation of this object
    def __repr__(self):
        return str(self)

    @abstractmethod
    def execute(self):
        """
            Returns string message

            on error raises TaskError exception
        """
        raise TaskError("Execute method is not overriden!")
