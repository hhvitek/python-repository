#!/usr/bin/env python3

import configparser
import logging
import os


class Settings:
    DEFAULT_CONFIG_PATH = f"{os.getcwd()}/settings.ini"

    def __init__(self, path=DEFAULT_CONFIG_PATH):
        self._config_path = path
        self._config_parser = self._get_default_config_parser()

        if not self._load_config_from_file(path):
            logging.info(
                f'Configuration file "{path}" not found. Initializing with default values.'
            )

    def _get_default_config_parser(self):
        # allow_no_value=True ... allows comments
        config_parser = configparser.ConfigParser(
            allow_no_value=True, interpolation=None
        )
        # case sensitive
        config_parser.optionxform = lambda option: option

        config_parser["LOGIN"] = {
            "; [USERNAME/PASSWORD]": None,
            "USERNAME": "",
            "PASSWORD": "",
        }

        config_parser["IMAP"] = {"SERVER": ""}

        return config_parser

    def _load_config_from_file(self, path=DEFAULT_CONFIG_PATH):
        if not self._config_parser.read(path):
            logging.warning("Cannot load/read configuration file: " + path)
            return False
        else:
            logging.info("Success reading configuration file: " + path)
            return True

    def create_default_configfile(self, path=None):
        if path is None:
            path = self._config_path

        default_config_parser = self._get_default_config()

        with open(path, "w") as configfile:
            default_config_parser.write(configfile)
            logging.info(f"Succesfully created default configuration file: {path}")

    def get_value(self, section_name, value_name):
        if self.exists_value(section_name, value_name):
            return self._config_parser.get(section_name, value_name)
        else:
            return None

    def exists_value(self, section_name, value_name):
        return self._config_parser.has_option(section_name, value_name)

    def set_value(self, section_name, value_name, value):
        self._config_parser[section_name][value_name] = value

    def get_username(self):
        return self.get_value("LOGIN", "USERNAME")

    def get_password(self):
        return self.get_value("LOGIN", "PASSWORD")

    def get_server(self):
        return self.get_value("IMAP", "SERVER")
