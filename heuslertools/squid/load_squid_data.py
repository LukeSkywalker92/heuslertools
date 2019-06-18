import numpy as np

def search_data_start(file, identifier):
    search = open(file)
    i = 1
    for line in search:
        if identifier in line:
            search.close()
            return i + 1
        i += 1

def load_squid_data(file):
    data = {}
    data["field"], data["temperature"], data["long_moment"] = np.loadtxt(fname=file, skiprows=search_data_start(file, "[Data]"), delimiter=",", usecols = (2,3,4), unpack=True)
    return data
