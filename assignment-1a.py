#########################################################################################
#																						#
# 								PROGRAMMING IN DATA SCIENCE		                        #
#								ASSIGNMENT-1 a									        #
#								STUDENT ID:											    #
#								STUDENT NAME										    #
#								DATE OF SUBMISSION:                                     #
#								UNDER GRADUATE OR POST GRADUATE                         #
#																						#
##########################################################################################

### Importing read file and utilty method ##
import io_module as io
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
import numpy as np

### Defining the dataset.
### *_2d.txt has 2 coordinate
### *_3d.txt has 3 coordinate
### *_4d.txt has 4 coordinate

def read_dataset(dimension: int):
    red_data = ["datasets/red_2d.txt", "datasets/red_4d.txt", "datasets/red_6d.txt"]
    blue_data = ["datasets/blue_2d.txt", "datasets/blue_4d.txt", "datasets/blue_6d.txt"]
    unknown_data = ["datasets/unknown_2d.txt", "datasets/unknown_4d.txt", "datasets/unknown_6d.txt"]
    try:
        if dimension == 2:
            red_dataset = io.read_multi_dim_data(red_data[0])
            blue_dataset = io.read_multi_dim_data(blue_data[0])
            unknown_dataset = io.read_multi_dim_data(unknown_data[0])
            return red_dataset, blue_dataset, unknown_dataset
        elif dimension == 4:
            red_dataset = io.read_multi_dim_data(red_data[1])
            blue_dataset = io.read_multi_dim_data(blue_data[1])
            unknown_dataset = io.read_multi_dim_data(unknown_data[1])
            return red_dataset, blue_dataset, unknown_dataset
        elif dimension == 8:
            red_dataset = io.read_multi_dim_data(red_data[2])
            blue_dataset = io.read_multi_dim_data(blue_data[2])
            unknown_dataset = io.read_multi_dim_data(unknown_data[2])
            return red_dataset, blue_dataset, unknown_dataset
        else:
            raise ValueError
    except ValueError:
        print("Please enter a valid number")


if __name__ == '__main__':
    select_dimension = int(input("Select the Dimension for the Red and blue dataset (2,4,8):"))
    red_dataset, blue_dataset, unknown_dataset = read_dataset(select_dimension)
    kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(red_dataset)

### Write a code to find whether the unknow_point is red or blue
# Calculate distances from the unknown sample to all red data samples


# The output is in output folder
