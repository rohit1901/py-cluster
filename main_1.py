import os
import datetime

from data_utils import load_data
from classify_unknown_samples import classify_unknown_samples

# This function loads the data from the files
# the filesnames depend on the number of dimensions passed to the function
def get_data(dimensions):
    unknown_data = load_data(f"datasets/unknown_{dimensions}d.txt")
    red_data = load_data(f"datasets/red_{dimensions}d.txt")
    blue_data = load_data(f"datasets/blue_{dimensions}d.txt")
    return unknown_data, red_data, blue_data

# This function classifies the unknown samples and outputs the results to a file
# The file name is generated using the current timestamp and the number of dimensions
# example: unknown_samples_2d_20210301123456.txt
def get_dimensions_and_samples(dimensions, unknown_data, red_data, blue_data):
    # Classify unknown samples
    class_labels = classify_unknown_samples(unknown_data, red_data, blue_data)

    # Define the output folder
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    # Generate a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Create the output file
    output_file = os.path.join(output_folder, f"unknown_samples_{dimensions}d_{timestamp}.txt")

    # Output unknown samples and their class labels to the file
    with open(output_file, "w") as file:
        for i, (unknown_sample, label) in enumerate(class_labels):
            file.write(f"Unknown Sample {i + 1}: {unknown_sample}, Class: {label}\n")

    print(f"Output saved to {output_file}")


def main():
    # Load data
    # NOTE: the number of dimensions can be changed here: 2 or 4 or 8
    unknown_data, red_data, blue_data = get_data(2)
    # Get dimensions and samples
    get_dimensions_and_samples(2, unknown_data, red_data, blue_data)


if __name__ == "__main__":
    main()
