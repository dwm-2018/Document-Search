import datetime
import signal
import time

from services.fileService import FileService
from services.indexSearchService import IndexSearchService
from services.regexSearchService import RegexSearchService
from services.simpleSearchService import SimpleSearchService
from services.utils import print_result

if __name__ == "__main__":
    search_files = FileService.get_search_files()

    while True:
        try:
            result = []
            search_term = input("Enter a search term or ctrl-c to quit \n>")
            search_type = input("\nSelect a search method:\n1) String Match \n2) Regular Expression \n3) Indexed \n>")

            if search_type == "1":
                start_time_ms = int(round(time.time() * 1000))
                sss = SimpleSearchService()
                result = sss.search(search_term, search_files)
                end_time_ms = int(round(time.time() * 1000))
                print_result(result)
                print("Elapsed Time: {ex_time}ms".format(ex_time=end_time_ms-start_time_ms))
            elif search_type == "2":
                start_time_ms = int(round(time.time() * 1000))
                rss = RegexSearchService()
                result = rss.search(search_term, search_files)
                end_time_ms = int(round(time.time() * 1000))
                print_result(result)
                print("Elapsed Time: {ex_time}ms".format(ex_time=end_time_ms-start_time_ms))
            elif search_type == "3":
                start_time_ms = int(round(time.time() * 1000))
                iss = IndexSearchService()
                search_index = iss.build_search_index(search_files)
                result = iss.search(search_term, search_index)
                end_time_ms = int(round(time.time() * 1000))
                print_result(result)
                print("Elapsed Time: {ex_time}ms".format(ex_time=end_time_ms-start_time_ms))
            else:
                print("Please choose 1, 2 or 3.\n")

        except KeyboardInterrupt:
            exit()

