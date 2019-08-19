import os

LOCATION = "resources"


class FileService:

    def __init__(self):
        pass

    @staticmethod
    def get_search_files():
        return os.listdir(LOCATION)
