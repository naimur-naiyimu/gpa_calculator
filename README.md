# GPA Calculator Package

This package allows users to calculate GPA, CGPA, and average marks easily.

## Installation

* [ ] You can install the package via PIP: ``pip install gpa_calculator``

## Usage

```python
from gpa_calculator import calculate_gpa, calculate_cgpa, calculate_average

# Calculate GPA
gpa = calculate_gpa([4.0, 3.5], [3, 4])

# Calculate CGPA
cgpa = calculate_cgpa([3.5, 3.7], [15, 18])

# Calculate Average Marks
average = calculate_average([85, 90, 78])

print(gpa, cgpa, average)
```

## License

This project is licensed under the MIT License.
