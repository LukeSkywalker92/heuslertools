def search_data_start(file, identifier):
    """
    Returns the line of an identifier for the start of the data in a file.
    """
    if identifier is None:
        return 0
    search = open(file)
    i = 1
    for line in search:
        if identifier in line:
            search.close()
            return i + 1
        i += 1
