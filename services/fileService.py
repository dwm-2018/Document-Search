import os

LOCATION = "resources"


class FileService:

    def __init__(self):
        pass

    @staticmethod
    def get_search_files():
        return os.listdir(LOCATION)

    @staticmethod
    def read_file(file_name):
        file_path = LOCATION + "/" + file_name
        if not os.path.exists(file_path):
            return
        file = open(file_path, "r")
        return file.read()

