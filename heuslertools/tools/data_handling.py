import numpy as np

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
            return i
        i += 1

def load_data(file, identifier, delimiter):
    """
    Loads a measurement and returns the data
    moment data.
    """
    data = {}
    data = np.genfromtxt(fname=file, delimiter=delimiter, skip_header=search_data_start(file, identifier), names=True)
    first_line = [str(i) for i in data[0]]
    if all(x == 'nan' for x in first_line):
        data = data[1:]
    return data
