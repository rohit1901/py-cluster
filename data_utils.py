import numpy as np

"""
Calculate the Euclidean distance between two points.

Args:
    point1 (numpy.ndarray): The first point.
    point2 (numpy.ndarray): The second point.

Returns:
    float: The Euclidean distance between the two points.
"""


def calculate_distance(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    return np.sqrt(np.sum((point1 - point2) ** 2))


"""
Load data from a text file.

Args:
    filename (str): The name of the text file containing the data.

Returns:
    list: A list of data points.
"""


def load_data(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append([float(x) for x in line.strip().split()])
    return data


def load_clustering_data(filename):
    return np.loadtxt(filename)


def get_dimensions_and_samples(data):
    """Get the number of dimensions (D) and data samples (N)."""
    D = data.shape[1]
    N = data.shape[0]
    return D, N
