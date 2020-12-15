from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

from geopy.distance import geodesic
from .coordinates import Coords
import app.gps.errors as errors


class Gps:
    """
        Constructs this object from a string variable - path to a image.
        Provides a several image/exif-based helper methods to extract
        helpful gps information
    """

    NUMBER_OF_DECIMALS_TO_ROUND = 10

    def __init__(self, filepath):
        self._filepath = filepath
        self._coords = None

    def get_exif(self):
        """
        :exception ImageDoesNotExistError: If the file cannot be found.
        :exception InvalidImageFormatError: If the image cannot be opened and identified.
        """
        try:
            with Image.open(self._filepath) as image:
                return image.getexif()
        except FileNotFoundError as ex:
            raise errors.ImageDoesNotExistError(self._filepath)
        except UnidentifiedImageError as ex:
            raise errors.InvalidImageFormatError(self._filepath)

    def get_labeled_exif(self):
        """
        :exception ImageDoesNotExistError: If the file cannot be found.
        :exception InvalidImageFormatError: If the image cannot be opened and identified.
        """
        exif = self.get_exif()

        labeled_exif = {}
        for (key, value) in exif.items():
            labeled_exif[TAGS.get(key)] = value

        return labeled_exif

    def get_geotagging(self):
        """
        :exception ImageDoesNotExistError: If the file cannot be found.
        :exception InvalidImageFormatError: If the image cannot be opened and identified.

        :exception NoExifMetadataFoundError: if image does not contain exif metadata.
        :exception NoGpsLocationDataError: if image does not contain gps location based metadata

        """
        exif = self.get_exif()

        if not exif:
            raise errors.NoExifMetadataFoundError(self._filepath)

        geotagging = {}
        for (idx, tag) in TAGS.items():
            if tag == 'GPSInfo':
                if idx not in exif:
                    raise errors.NoGpsLocationDataError(self._filepath)

                for (key, val) in GPSTAGS.items():
                    if key in exif[idx]:
                        geotagging[val] = exif[idx][key]

        return geotagging

    def get_coordinates(self):
        """
        :exception ImageDoesNotExistError: If the file cannot be found.
        :exception InvalidImageFormatError: If the image cannot be opened and identified.

        :exception NoExifMetadataFoundError: if image does not contain exif metadata.
        :exception NoGpsLocationDataError: if image does not contain gps location based metadata

        :exception InvalidExifGpsMetadataError: if Gps metadata does not contain expected
        Latitude and Longitude information.
        """
        geotagging = self.get_geotagging()

        try:
            lat = self._get_decimal_from_dms(geotagging['GPSLatitude'], geotagging['GPSLatitudeRef'])
            lon = self._get_decimal_from_dms(geotagging['GPSLongitude'], geotagging['GPSLongitudeRef'])
            return Coords(lat, lon)
        except KeyError as ex:
            raise errors.InvalidExifGpsMetadataError(self._filepath, geotagging)

    @classmethod
    def _get_decimal_from_dms(cls, dms, ref):
        degrees = dms[0]
        minutes = dms[1] / 60.0
        seconds = dms[2] / 3600.0

        if ref in ['S', 'W']:
            degrees = -degrees
            minutes = -minutes
            seconds = -seconds

        return round(degrees + minutes + seconds, cls.NUMBER_OF_DECIMALS_TO_ROUND)

    def calculate_distance_to_another_coords(self, calculate_to_coords):
        """
        :exception ImageDoesNotExistError: If the file cannot be found.
        :exception InvalidImageFormatError: If the image cannot be opened and identified.

        :exception NoExifMetadataFoundError: if image does not contain exif metadata.
        :exception NoGpsLocationDataError: if image does not contain gps location based metadata

        :exception InvalidExifGpsMetadataError: if Gps metadata does not contain expected
         Latitude and Longitude information.
        """
        if self._coords is None:
            self._coords = self.get_coordinates()

        return self.calculate_distance_between_two_points_coords(self._coords, calculate_to_coords)

    @classmethod
    def calculate_distance_between_two_points_coords(cls, coords_x, coords_y):
        point_x = coords_x.to_lat_lon_tuple()
        point_y = coords_y.to_lat_lon_tuple()
        return geodesic(point_x, point_y).kilometers

    @classmethod
    def calculate_distance_between_two_points(cls, lat_x, lon_x, lat_y, lon_y):
        point_x = (lat_x, lon_x)
        point_y = (lat_y, lon_y)

        return cls.calculate_distance_between_two_points_coords(point_x, point_y)