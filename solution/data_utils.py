# data_utils.py

import numpy as np


def calculate_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points.

    Args:
        point1 (numpy.ndarray): The first point.
        point2 (numpy.ndarray): The second point.

    Returns:
        float: The Euclidean distance between the two points.
    """
    point1 = np.array(point1)
    point2 = np.array(point2)
    return np.sqrt(np.sum((point1 - point2) ** 2))


def load_data(filename):
    absolute_filename = f"datasets/{filename}"
    """
    Load data from a text file.

    Args:
        filename (str): The name of the text file containing the data.

    Returns:
        list: A list of data points.
    """
    data = []
    with open(absolute_filename, "r") as file:
        for line in file:
            data.append([float(x) for x in line.strip().split()])
    return data
