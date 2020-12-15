from .settings import Settings
import configparser


class AppSettings(Settings):
    def __init__(self, path=None, create_if_not_exists=None):
        super(AppSettings, self).__init__(path=path, create_if_not_exists=create_if_not_exists)

    def _get_default_config_parser(self):
        # allow_no_value=True ... allows comments
        config_parser = configparser.ConfigParser(
            allow_no_value=True, interpolation=None
        )
        # case sensitive
        config_parser.optionxform = lambda option: option

        config_parser["ARGUMENTS"] = {
            "EXTENSIONS": ".jpg, .jpeg",
            "ROOT_FOLDER": "",
            "LATITUDE": 50.4188400,
            "LONGITUDE": 16.1616603,
            "MAX_DISTANCE_IN_KM": 10
        }

        return config_parser

    def get_extensions(self):
        return self.get_value_raise("ARGUMENTS", "EXTENSIONS")

    def get_root_folder(self):
        return self.get_value_raise("ARGUMENTS", "ROOT_FOLDER")

    def get_latitude(self):
        return float(self.get_value_raise("ARGUMENTS", "LATITUDE"))

    def get_longitude(self):
        return float(self.get_value_raise("ARGUMENTS", "LONGITUDE"))

    def get_max_distance_in_km(self):
        return float(self.get_value_raise("ARGUMENTS", "MAX_DISTANCE_IN_KM"))
