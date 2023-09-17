# main.py

import data_utils as data_loader
import clustering


def main(data_filename, K):
    data = data_loader.load_clustering_data(data_filename)
    D, N = data_loader.get_dimensions_and_samples(data)
    cluster_centers = clustering.initialize_cluster_centers(K, D)
    labels, new_cluster_centers = clustering.perform_kmeans_clustering(data, K, cluster_centers)
    clustering.plot_clusters(data, labels, new_cluster_centers)


if __name__ == "__main__":
    main('datasets/data_2c_2d.txt', K=2)
    main('datasets/data_2c_4d.txt', K=2)
    main('datasets/data_4c_2d.txt', K=4)
    main('datasets/data_4c_4d.txt', K=4)
