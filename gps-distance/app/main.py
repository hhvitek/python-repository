#!/usr/bin/env python

import logging
import os
import re

from app.gps.coordinates import Coords
from app.model.gps_image_model import GpsImageModel
from app.settings.app_settings import AppSettings
from app.settings.errors import ItemNotFoundError


def strip_whitespaces_list(ext_list):
    return [x.strip() for x in ext_list]


def finish_with_error(error_msg):
    if error_msg:
        logging.error(error_msg)
    logging.info("*********************Finished*********************")
    quit(1)


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s||%(message)s",
        level=logging.INFO
       # datefmt="%H:%M:%S",
    )

    logging.info("*********************Starting*********************")

    # load settings from a file
    settings = AppSettings(create_if_not_exists=True)

    try:
        ARG_EXTENSIONS = settings.get_extensions()
        ARG_ROOT_FOLDER = settings.get_root_folder()
        ARG_LAT = settings.get_latitude()
        ARG_LON = settings.get_longitude()
        ARG_DISTANCE = settings.get_max_distance_in_km()
    except ItemNotFoundError as ex:
        finish_with_error(f"Error in settings file: {ex}")

    if not os.path.isdir(ARG_ROOT_FOLDER):
        finish_with_error("Argument root folder does not exist!!!")

    extensions = re.split(",", ARG_EXTENSIONS)
    extensions = strip_whitespaces_list(extensions)

    coords = Coords(ARG_LAT, ARG_LON)

    logging.info(f"Using R: {ARG_ROOT_FOLDER}, E: {extensions}, C: {coords}, D: {ARG_DISTANCE}")

    gps_model = GpsImageModel(root_folder=ARG_ROOT_FOLDER, extensions=extensions, coords=coords, distance=ARG_DISTANCE)
    gps_model.process_all()
    processor = gps_model.get_processor()
    logging.info(f"Found {len(processor.get_images_match())}, {processor.get_images_match()}")

    logging.info("*********************Finished*********************")