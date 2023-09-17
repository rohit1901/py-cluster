# test_clustering.py

import unittest
import numpy as np
from clustering import initialize_cluster_centers, perform_kmeans_clustering

class TestClustering(unittest.TestCase):

    def test_initialize_cluster_centers(self):
        K = 3
        D = 2
        centers = initialize_cluster_centers(K, D)
        self.assertEqual(centers.shape, (K, D))

    def test_perform_kmeans_clustering(self):
        data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        K = 2
        cluster_centers = np.array([[0, 0], [9, 9]])
        labels, new_cluster_centers = perform_kmeans_clustering(data, K, cluster_centers)
        self.assertEqual(labels.tolist(), [0, 0, 1, 1])  # Adjust labels based on your test data
        self.assertTrue(np.array_equal(new_cluster_centers, np.array([[2, 3], [6, 7]])))

if __name__ == '__main__':
    unittest.main()
