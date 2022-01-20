import numpy as np

def search_data_start(file, identifier, encoding):
    """
    Returns the line of an identifier for the start of the data in a file.
    """
    if identifier is None:
        return 0
    search = open(file, encoding=encoding)
    i = 1
    for line in search:
        if identifier in line:
            search.close()
            return i
        i += 1

def load_data(file, identifier, delimiter, start_row=0, end_row=None, names=True, encoding=None, dtype=float):
    """
    Loads a measurement and returns the data
    moment data.
    """
    data = {}
    data = np.genfromtxt(fname=file, delimiter=delimiter, skip_header=search_data_start(file, identifier, encoding), names=names, encoding=encoding, dtype=dtype)
    first_line = [str(i) for i in data[0]]
    if all(x == 'nan' for x in first_line):
        data = data[1:]
    return data[start_row:end_row]
