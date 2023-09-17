# K-Means Clustering Application
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Rohit](https://github.com/rohit1901/py-cluster/actions/workflows/test.yml/badge.svg)
This Python application demonstrates K-Means clustering on various datasets and provides a modularized structure for loading data and performing clustering. The code is organized into two modules: `data_loader` and `clustering`.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- NumPy
- scikit-learn
- seaborn
- matplotlib
- ruff
- pytest

You can install the required dependencies using pip:

```
pip install numpy scikit-learn seaborn matplotlib ruff pytest
```

### Installation

1. Clone the repository:

```
git clone https://github.com/rohit1901/py-cluster.git
cd py-cluster
```

2. Run the main script:

```
python main_1.py
python main_2.py
```

## Code Structure

- `data_utils` module: Responsible for loading data and extracting dimensions and samples.
- `clustering` module: Implements K-Means clustering and related functions.
- `classify_unknown_samples` module: Implements a function to classify unknown samples using a trained model.
- `main_1` script: Demonstrates classification of unknown samples using nearest neighbour classification.
- `main_2` script: Demonstrates K-Means clustering on various datasets.

## Testing

To run unit tests for the application, use the following commands:

```
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the need to understand K-Means clustering and its implementation in Python.
- Thanks to the contributors and open-source libraries that made this project possible.
