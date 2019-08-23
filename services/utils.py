
def print_result(result):
    print("\nSearch Results:")
    if len(result) == 0:
        print('Search term was not found. \n')

    result = sorted(result, key=lambda i: i['occurences'], reverse=True)
    for entry in result:
        print("{file_name} - {occurences}".format(file_name=entry['file_name'], occurences=entry['occurences']))
    print("\n")
