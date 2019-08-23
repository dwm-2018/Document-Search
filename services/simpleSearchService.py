
class SimpleSearchService:
    def __init__(self):
        pass

    def search(self, search_term, search_files):
        search_result = []
        for search_file in search_files:
            occurrences = self.conduct_simple_string_search(search_term, search_file.fileBuffer)
            if occurrences > 0:
                search_result.append({'file_name' :search_file.fileName, 'occurences': occurrences})

        return search_result

    @staticmethod
    def conduct_simple_string_search(search_term, buffer_to_search):
        return buffer_to_search.count(search_term)
