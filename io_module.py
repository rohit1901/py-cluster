#Function to read multi-dimension data from a file

def read_multi_dim_data(filename):
    """
    Reads a multi-dimensional data from a file.
    """
    dataset = []
    with open(filename, 'r') as f:
        for line in f:
            data = line.split()
            dataset.append([float(x) for x in data])
    print(dataset)
    return dataset



