class Coords:
    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude

    @classmethod
    def from_point(cls, point=()):
        latitude, longitude = point
        return cls(latitude, longitude)

    def to_lat_lon_tuple(self):
        return self._latitude, self._longitude

    def __repr__(self):
        return f"Coords({self._latitude} {self._longitude})"
