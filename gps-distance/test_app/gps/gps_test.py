import unittest

from app.gps.gps import Gps
from app.gps.errors import *


class GpsTest(unittest.TestCase):
    def test_extract_gps_data(self):
        file = "../TEST_ROOT_FOLDER/containsGps.jpg"
        gps = Gps(file)

        try:
            geotags = gps.get_geotagging()
            self.assertIsNotNone(geotags)
            self.assertTrue(geotags)
        except BaseCustomGpsError:
            self.fail("Does not contain expected gps location metadata.")

    def test_extract_gps_data_file_does_not_exist(self):
        file = "./TEST_ROOT_FOLDER/non-existent-file.jpg"
        gps = Gps(file)

        self.assertRaises(ImageDoesNotExistError, lambda: gps.get_geotagging())

    def test_extract_gps_data_file_does_not_contain_geo_location_data(self):
        file = "../TEST_ROOT_FOLDER/noGpsData.JPG"
        gps = Gps(file)

        self.assertRaises(NoGpsLocationDataError, lambda: gps.get_geotagging())
