import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

"""Initialize K cluster centers randomly with D dimensions."""


def initialize_cluster_centers(K, D):
    return np.random.rand(K, D)


"""Perform K-Means clustering and return cluster labels and centers."""


def perform_kmeans_clustering(data, K, cluster_centers, threshold=0.001):
    while True:
        kmeans = KMeans(n_clusters=K, init=cluster_centers, n_init=1, random_state=0)
        kmeans.fit(data)
        labels = kmeans.labels_
        new_cluster_centers = kmeans.cluster_centers_
        sum_distance = np.sum(np.abs(new_cluster_centers - cluster_centers))

        if sum_distance < threshold:
            return labels, new_cluster_centers
        else:
            cluster_centers = new_cluster_centers


"""Plot data samples and cluster centers using Seaborn."""


def plot_clusters(data, labels, cluster_centers):
    sns.set(style='whitegrid')
    plt.figure(figsize=(8, 6))

    sns.scatterplot(x=data[:, 0], y=data[:, 1], hue=labels, palette='viridis', legend='full')
    sns.scatterplot(x=cluster_centers[:, 0], y=cluster_centers[:, 1], marker='X', s=100, color='red')

    plt.title(f'K-Means Clustering with K={len(cluster_centers)}')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.legend(loc='upper right', title='Cluster')
    plt.show()
