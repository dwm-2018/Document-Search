import re

from services.utils import has_non_alphanumeric, remove_non_alphanumeric


class IndexSearchService:
    def __init__(self):
        pass

    def search(self, search_term, search_index):
        return search_index.get(search_term, [])

    def build_search_index(self, search_files):
        master_index = {}
        for file in search_files:
            self.add_inverted_index_to_master_index(master_index, self.build_inverted_index(file.fileBuffer), file.fileName)

        return master_index

    def build_inverted_index(self, file_buffer):
        words_list = file_buffer.split()
        inverted_index = {}
        for word in words_list:
            self.add_word_to_dict(word, inverted_index)
            if has_non_alphanumeric(word):
                self.add_word_to_dict(remove_non_alphanumeric(word), inverted_index)
        return inverted_index

    @staticmethod
    def add_word_to_dict(word, index_dict):
        if not word:
            return index_dict

        if word in index_dict:
            index_dict[word] += 1
        else:
            index_dict[word] = 1
        return index_dict

    @staticmethod
    def add_inverted_index_to_master_index(master_index, inverted_index, file_name):
        for key, value in inverted_index.items():
            if key in master_index:
                master_index[key].append({'file_name': file_name, 'occurences': value})
            else:
                master_index[key] = [{'file_name': file_name, 'occurences': value}]
        return master_index

