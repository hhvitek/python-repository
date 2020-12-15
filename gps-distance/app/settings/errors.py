class ItemNotFoundError(Exception):
    def __init__(self, section, value):
        super().__init__(f"Requested item {section}.{value} not found.")
