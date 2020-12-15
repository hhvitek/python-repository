#!/usr/bin/env python3

from abc import ABC, abstractmethod
import logging
import os
from .errors import ItemNotFoundError


class Settings(ABC):
    DEFAULT_CONFIG_PATH = f"{os.getcwd()}/settings.ini"
    DEFAULT_ROOT_FOLDER = f"{os.getcwd()}"

    def __init__(self, path=DEFAULT_CONFIG_PATH, create_if_not_exists=True):
        if path is None:
            path = self.DEFAULT_CONFIG_PATH
        if create_if_not_exists is None:
            create_if_not_exists = True

        self._config_path = path
        self._config_parser = self._get_default_config_parser()

        if create_if_not_exists and not os.path.isfile(path):
            self.create_default_configfile()

        if not self._load_config_from_file(path):
            logging.error(f'Configuration file "{path}" failed to load. Initializing with default values.')

    @abstractmethod
    def _get_default_config_parser(self):
        pass

    def create_default_configfile(self, path=None):
        if path is None:
            path = self._config_path

        default_config_parser = self._get_default_config_parser()

        with open(path, "w") as configfile:
            default_config_parser.write(configfile)
            logging.info(f"Successfully created default configuration file: {path}")

    def save_to_file(self, path=None):
        if path is None:
            path = self._config_path

        with open(path, "w") as configfile:
            self._config_parser.write(configfile)
            logging.info(f"Successfully saved configuration file: {path}")

    def _load_config_from_file(self, path=DEFAULT_CONFIG_PATH):
        if not self._config_parser.read(path):
            logging.warning("Cannot load/read configuration file: " + path)
            return False
        else:
            logging.info("Success reading configuration file: " + path)
            return True

    def get_value(self, section_name, value_name):
        if self.exists_value(section_name, value_name):
            return self._config_parser.get(section_name, value_name)
        else:
            return None

    def exists_value(self, section_name, value_name):
        return self._config_parser.has_option(section_name, value_name)

    def get_value_raise(self, section_name, value_name):
        if self.exists_value(section_name, value_name):
            return self._config_parser.get(section_name, value_name)
        else:
            raise ItemNotFoundError(section_name, value_name)

    def set_value(self, section_name, value_name, value):
        if not self._config_parser.has_section(section_name):
            self._config_parser.add_section(section_name)

        self._config_parser.set(section_name, value_name, value)

    def __repr__(self):
        return str({section: dict(self._config_parser[section]) for section in self._config_parser.sections()})
