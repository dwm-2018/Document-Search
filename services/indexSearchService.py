
class IndexSearchService:
    def __init__(self):
        pass

    def search(self, search_term, search_index):
        pass

    def build_search_index(self, search_files):
        master_index = {}
        for file in search_files:
            pass

    def build_inverted_index(self, file_buffer):
        words_list = file_buffer.split()
        inverted_index = {}
        for word in words_list:
            self.add_word_to_dict(word, inverted_index)
        return inverted_index

    @staticmethod
    def add_word_to_dict(word, index_dict):
        if word in index_dict:
            index_dict[word] += 1
        else:
            index_dict[word] = 1
        return index_dict

    @staticmethod
    def add_inverted_index_to_master_index(master_index, inverted_index, file_name):
        for key, value in inverted_index.items():
            if key in master_index:
                master_index[key].append({file_name: value})
            else:
                master_index[key] = [{file_name: value}]
        return master_index
