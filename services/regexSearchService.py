import re


class RegexSearchService:
    def __init__(self):
        pass

    def search(self, search_term, search_files):
        search_result = []
        for search_file in search_files:
            occurrences = self.conduct_regular_expression_search(search_term, search_file.fileBuffer)
            if occurrences > 0:
                search_result.append({search_file.fileName: occurrences})

        return search_result

    @staticmethod
    def conduct_regular_expression_search(search_term, buffer_to_search):
        return len(re.findall(search_term, buffer_to_search))
