from app.gps.gps import Gps
from app.gps.errors import *


class GpsImageFileProcessor:
    def __init__(self, coords, distance):
        self._total = 0
        self._matches = []
        self._not_matches = []
        self._no_gps_metadata = []
        self._invalid_exif = []
        self._invalid = []
        self._others = []

        self._coords = coords
        self._distance = distance

    def process_file(self, file):
        try:
            gps = Gps(file)
            distance_km = gps.calculate_distance_to_another_coords(self._coords)
            if distance_km < self._distance:
                self._matches.append(file)
            else:
                self._not_matches.append(file)
        except ImageDoesNotExistError:
            self._invalid.append(file)
        except InvalidImageFormatError:
            self._others.append(file)
        except (NoExifMetadataFoundError, NoGpsLocationDataError):
            self._no_gps_metadata.append(file)
        except InvalidExifGpsMetadataError:
            self._invalid_exif.append(file)
        finally:
            self._total += 1

    def get_file_processed_total(self):
        return self._total

    def get_images_match(self):
        return self._matches

    def get_images_not_match(self):
        return self._not_matches

    def get_images_no_gps_metadata(self):
        return self._no_gps_metadata

    def get_images_invalid(self):
        return self._invalid

    def get_images_invalid_exif(self):
        return self._invalid_exif

    def get_file_others(self):
        return self._others