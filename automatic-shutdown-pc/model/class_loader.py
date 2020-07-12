#!/usr/bin/env python

import importlib
import pkgutil
import logging


class ClassLoader:
    """
        Instantiate class using full moduleName.className
    """

    def __init__(self):
        raise NotImplementedError(
            "ClassLoader class cannot be instantiated. It contains only static methods."
        )

    # raises(AttributeError)
    # raises(ModuleNotFound)
    @classmethod
    def from_module_classname(cls, modulename, classname):
        module = importlib.import_module(modulename)
        class_ = getattr(module, classname)
        instance = class_()
        return instance

    @classmethod
    def from_string(cls, modulename_classname):
        modulename, classname = modulename_classname.rsplit(".", 1)
        return cls.from_module_classname(modulename, classname)

    @classmethod
    def from_string_on_error_none(cls, modulename_classname):
        modulename, classname = modulename_classname.rsplit(".", 1)
        try:
            return cls.from_module_classname(modulename, classname)
        except (ModuleNotFoundError, AttributeError) as ex:
            logging.error(f"Failed to found class: {modulename_classname} : {ex}")
            return None

    @classmethod
    def get_modules_names(cls, folder_package_path, module_name_suffix=""):
        modules_names = []
        for finder, name, ispkg in pkgutil.iter_modules(folder_package_path):
            if name.endswith(module_name_suffix):
                modules_names.append(name)

        return modules_names
