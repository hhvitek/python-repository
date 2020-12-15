import os
from app.gps.coordinates import Coords
from .gps_image_file_processor import GpsImageFileProcessor


class GpsImageModel:
    DEFAULT_ROOT_FOLDER = f"{os.getcwd()}"
    DEFAULT_DISTANCE = 10.0
    DEFAULT_COORDS = Coords(0.0, 0.0)
    DEFAULT_EXTENSIONS = [".jpg", ".jpeg"]

    def __init__(self,
                 root_folder=DEFAULT_ROOT_FOLDER,
                 extensions=DEFAULT_EXTENSIONS,
                 coords=DEFAULT_COORDS,
                 distance=DEFAULT_DISTANCE):
        self._extensions = extensions
        self._root_folder = root_folder
        self._coords = coords
        self._distance = distance
        self._processor = GpsImageFileProcessor(self._coords, self._distance)

    def set_extensions(self, extensions):
        self._extensions = extensions

    def set_root_folder(self, root_folder):
        self._root_folder = root_folder

    def set_coords(self, coords):
        self._coords = coords

    def set_distance(self, distance):
        self._distance = distance

    def find_all(self):
        found_files = []

        for rootdirpath, dirnames, filenames in os.walk(self._root_folder):
            for filename in filenames:
                filepath = os.path.abspath(os.path.join(rootdirpath, filename))

                if self._has_extension_in(filepath):  # it's image
                    found_files.append(filepath)
                else:
                    pass  # file has different extension

        return found_files

    def _has_extension_in(self, filename):
        for extension in self._extensions:
            if self._has_extension(filename, extension):
                return True
        return False

    def _has_extension(self, filename, extension):
        root, ext = os.path.splitext(filename)
        return extension.lower() == ext.lower()

    def process_all(self):
        self._processor = GpsImageFileProcessor(self._coords, self._distance)

        found_files = self.find_all()

        for file in found_files:
            self._process_image(file)

    def _process_image(self, file):
        self._processor.process_file(file)

    def get_processor(self):
        return self._processor