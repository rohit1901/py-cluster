# test_data_loader.py

import unittest
import numpy as np
from data_utils import load_clustering_data, get_dimensions_and_samples


class TestDataLoader(unittest.TestCase):

    def test_load_data(self):
        data = load_clustering_data('test_data.txt')
        self.assertIsInstance(data, np.ndarray)
        self.assertEqual(data.shape, (2, 2))  # Adjust shape based on your test data

    def test_get_dimensions_and_samples(self):
        data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        D, N = get_dimensions_and_samples(data)
        self.assertEqual(D, 2)
        self.assertEqual(N, 4)


if __name__ == '__main__':
    unittest.main()
