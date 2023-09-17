# classify_unknown_samples.py
from data_utils import calculate_distance


def classify_unknown_samples(unknown_data, red_data, blue_data):
    """
    Classify unknown samples based on their distances to red and blue samples.

    Args:
        unknown_data (list): List of unknown data points.
        red_data (list): List of red data points.
        blue_data (list): List of blue data points.

    Returns:
        list: A list of tuples containing the unknown sample and its class label.
    """
    class_labels = []

    for unknown_sample in unknown_data:
        min_distance_to_red = float("inf")
        min_distance_to_blue = float("inf")

        for red_sample in red_data:
            distance = calculate_distance(unknown_sample, red_sample)
            if distance < min_distance_to_red:
                min_distance_to_red = distance

        for blue_sample in blue_data:
            distance = calculate_distance(unknown_sample, blue_sample)
            if distance < min_distance_to_blue:
                min_distance_to_blue = distance

        if min_distance_to_red < min_distance_to_blue:
            class_labels.append((unknown_sample, "red"))
        else:
            class_labels.append((unknown_sample, "blue"))

    return class_labels
