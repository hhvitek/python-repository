#!/usr/bin/env python

import importlib
import pkgutil


class ClassLoader:
    def __init__(self):
        pass

    # raises(AttributeError)
    # raises(ModuleNotFound)
    def from_module_classname(self, modulename, classname):
        module = importlib.import_module(modulename)
        class_ = getattr(module, classname)
        instance = class_()
        return instance

    def from_string(self, modulename_classname):
        modulename, classname = modulename_classname.rsplit(".", 1)
        return self.from_module_classname(modulename, classname)

    def get_modules_names(self, folder_package_path, module_name_suffix=""):
        modules_names = []
        for finder, name, ispkg in pkgutil.iter_modules(folder_package_path):
            if name.endswith(module_name_suffix):
                modules_names.append(name)

        return modules_names
