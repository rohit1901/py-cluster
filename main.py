import os
import datetime

from data_utils import load_data
from classify_unknown_samples import classify_unknown_samples


def main():
    # Load data
    unknown_data = load_data("datasets/unknown_2d.txt")
    red_data = load_data("datasets/red_2d.txt")
    blue_data = load_data("datasets/blue_2d.txt")

    # Classify unknown samples
    class_labels = classify_unknown_samples(unknown_data, red_data, blue_data)

    # Define the output folder
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    # Generate a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Create the output file
    output_file = os.path.join(output_folder, f"unknown_samples_{timestamp}.txt")

    # Output unknown samples and their class labels to the file
    with open(output_file, "w") as file:
        for i, (unknown_sample, label) in enumerate(class_labels):
            file.write(f"Unknown Sample {i + 1}: {unknown_sample}, Class: {label}\n")

    print(f"Output saved to {output_file}")


if __name__ == "__main__":
    main()
