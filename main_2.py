def get_dimensions_and_samples(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        if not lines:
            print(f"The file {filename} is empty.")
            return None, None

        # Assuming the data is in tabular format with space-separated values
        # Count the number of dimensions (D) by looking at the number of columns in the first row
        first_row = lines[0].strip().split()
        D = len(first_row)

        # Count the number of data samples (N) by counting the total lines in the file
        N = len(lines)

        return D, N
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred while processing {filename}: {str(e)}")
        return None, None


def main():
    # List of data file names
    data_files = ["datasets/data_2c_2d.txt", "datasets/data_2c_4d.txt", "datasets/data_4c_2d.txt",
                  "datasets/data_4c_4d.txt"]

    # Iterate through each data file and get dimensions and samples
    for filename in data_files:
        D, N = get_dimensions_and_samples(filename)
        if D is not None and N is not None:
            print(f"File: {filename}, D: {D}, N: {N}")


if __name__ == "__main__":
    main()
