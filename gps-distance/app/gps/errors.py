class BaseCustomGpsError(Exception):
    pass


class ImageDoesNotExistError(BaseCustomGpsError):
    def __init__(self, image_path):
        super().__init__(f"File does not exist: {image_path}.")


class InvalidImageFormatError(BaseCustomGpsError):
    def __init__(self, image_path):
        super().__init__(f"Image has invalid format: {image_path}.")


class NoGpsLocationDataError(BaseCustomGpsError):
    def __init__(self, image_path):
        super().__init__(f"File does not contain gps location metadata: {image_path}.")


class NoExifMetadataFoundError(BaseCustomGpsError):
    def __init__(self, image_path):
        super(NoExifMetadataFoundError, self).__init__(f"No exif metadata found. {image_path}")


class InvalidExifGpsMetadataError(BaseCustomGpsError):
    def __init__(self, image_path, tags):
        super(InvalidExifGpsMetadataError, self).__init__(f"Invalid exif metadata. {image_path} -> {tags}")
