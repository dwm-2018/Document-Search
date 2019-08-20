import os

from models.searchFile import SearchFile

LOCATION = "resources"


class FileService:

    def __init__(self):
        pass

    @staticmethod
    def get_search_files():
        search_files = []
        file_names = FileService.get_search_file_names()
        for file_name in file_names:
            search_file = SearchFile()
            search_file.fileName = file_name
            search_file.fileBuffer = FileService.read_file(file_name)
            search_files.append(search_file)

        return search_files

    @staticmethod
    def get_search_file_names():
        return os.listdir(LOCATION)

    @staticmethod
    def read_file(file_name):
        file_path = LOCATION + "/" + file_name
        if not os.path.exists(file_path):
            return
        file = open(file_path, "r")
        file_buffer = file.read()
        file.close()
        return file_buffer

