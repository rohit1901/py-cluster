# test_classification.py

import unittest
from data_utils import calculate_distance, load_data
from classify_unknown_samples import classify_unknown_samples


class TestDataUtils(unittest.TestCase):
    def test_calculate_distance(self):
        point1 = [1, 2]
        point2 = [4, 6]
        distance = calculate_distance(point1, point2)
        self.assertAlmostEqual(distance, 5.0)

    def test_load_data(self):
        filename = "../datasets/test_data.txt"
        with open(filename, "w") as file:
            file.write("1.0 2.0\n3.0 4.0\n")

        loaded_data = load_data(filename)
        self.assertEqual(loaded_data, [[1.0, 2.0], [3.0, 4.0]])


class TestClassification(unittest.TestCase):
    def test_classify_unknown_samples(self):
        unknown_data = [[0.5, 0.5], [2.0, 2.0], [5.0, 5.0]]
        red_data = [[1.0, 1.0], [3.0, 3.0]]
        blue_data = [[4.0, 4.0], [6.0, 6.0]]

        class_labels = classify_unknown_samples(unknown_data, red_data, blue_data)
        print (class_labels)
        expected_labels = [([0.5, 0.5], 'red'), ([2.0, 2.0], 'red'), ([5.0, 5.0], 'blue')]

        self.assertEqual(class_labels, expected_labels)


if __name__ == '__main__':
    unittest.main()
