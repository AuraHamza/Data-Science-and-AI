# 🔢 NumPy Learning

A hands-on repository documenting my learning and practice with **NumPy**, Python's fundamental library for numerical computing and array-based data processing.

This repository focuses on understanding NumPy arrays, multidimensional data, indexing, slicing, filtering, manipulation, and other core operations used in **Data Science, Machine Learning, and Artificial Intelligence**.

---

## 🎯 Purpose

The purpose of this repository is to develop a strong understanding of numerical computing with NumPy before progressing to higher-level Data Science and Machine Learning libraries.

The focus is on understanding **how NumPy works with structured numerical data**, rather than simply memorizing functions.

---

## 🧠 What I Am Learning

### NumPy Fundamentals

* NumPy installation
* Importing NumPy
* Creating arrays
* `ndarray`
* Python lists vs NumPy arrays
* Array dimensions
* Array properties

---

## 📐 Arrays & Dimensions

Understanding the difference between:

```text
Scalar
   │
   ▼
Vector
   │
   ▼
Matrix
   │
   ▼
Tensor
```

Important NumPy concepts include:

* 0-dimensional arrays
* 1-dimensional arrays
* 2-dimensional arrays
* Multidimensional arrays
* `ndim`
* `shape`
* `size`
* `dtype`

---

## 🔍 Indexing & Slicing

Practice with:

* Basic indexing
* Negative indexing
* Array slicing
* Row selection
* Column selection
* Multidimensional indexing

Example:

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0])
print(arr[:, 1])
print(arr[0:2, 1:3])
```

---

## 🎯 Filtering & Boolean Masking

Working with conditions to select data from arrays.

Example:

```python
import numpy as np

arr = np.array([10, 25, 30, 45, 50])

filtered = arr[arr > 30]

print(filtered)
```

This concept is particularly important for **data filtering and preprocessing**.

---

## 🔎 `np.where()`

Using conditional logic to locate or transform array values.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

result = np.where(arr > 25, 1, 0)

print(result)
```

---

## ✨ Fancy Indexing

Learning how to select multiple elements from an array using index arrays.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

selected = arr[[0, 2, 4]]

print(selected)
```

---

## 🔄 Array Manipulation

Practice with operations such as:

* Transpose
* Reshaping
* Stacking
* Concatenation
* Deleting elements
* Adding and removing dimensions

### Transpose

```python
arr.T
```

### Concatenation

```python
np.concatenate((arr1, arr2))
```

### Stacking

```python
np.vstack((arr1, arr2))
np.hstack((arr1, arr2))
```

---

## 🧩 Core NumPy Concepts

The repository focuses on understanding concepts such as:

| Concept         | Purpose                              |
| --------------- | ------------------------------------ |
| `ndarray`       | NumPy's primary array object         |
| `ndim`          | Number of dimensions                 |
| `shape`         | Size of each dimension               |
| `size`          | Total number of elements             |
| `dtype`         | Data type of array elements          |
| Indexing        | Access individual elements           |
| Slicing         | Select ranges of elements            |
| Boolean Masking | Filter data using conditions         |
| `where()`       | Conditional selection/transformation |
| Fancy Indexing  | Select elements using index arrays   |
| Transpose       | Swap array axes                      |
| Concatenation   | Join arrays                          |
| Stacking        | Combine arrays along dimensions      |
| Delete          | Remove array elements                |

---

## 🧪 Practical Examples

The repository contains hands-on examples designed to understand NumPy through experimentation.

A typical learning workflow is:

```text
Create Array
     │
     ▼
Inspect Array
     │
     ├── ndim
     ├── shape
     ├── size
     └── dtype
     │
     ▼
Access Data
     │
     ├── Indexing
     └── Slicing
     │
     ▼
Filter Data
     │
     ├── Boolean Mask
     └── np.where()
     │
     ▼
Manipulate Data
     │
     ├── Transpose
     ├── Stack
     ├── Concatenate
     └── Delete
```

---

## 🛠️ Technology

* **Python 3**
* **NumPy**
* **Jupyter Notebook**
* **VS Code**
* **Git**
* **GitHub**

---

## 📦 Installation

Install NumPy using pip:

```bash
pip install numpy
```

Verify the installation:

```python
import numpy as np

print(np.__version__)
```

---

## ▶️ Getting Started

Clone the repository:

```bash
git clone https://github.com/AuraHamza/numpy-learning.git
```

Navigate into the repository:

```bash
cd numpy-learning
```

If using a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install NumPy:

```bash
pip install numpy
```

Run your Python files or open the notebooks in Jupyter/VS Code.

---

## 📂 Repository Structure

```text
numpy-learning/
│
├── Array Basics
├── Dimensions & Shape
├── Indexing & Slicing
├── Filtering
├── Boolean Masking
├── np.where()
├── Fancy Indexing
├── Transpose
├── Stacking
├── Concatenation
├── Array Manipulation
├── Exercises
└── README.md
```

> The structure may evolve as additional NumPy concepts are explored.

---

## 📈 Learning Progress

| Topic                    | Status      |
| ------------------------ | ----------- |
| NumPy Basics             | ✅ Completed |
| `ndarray`                | ✅ Learned   |
| Lists vs Arrays          | ✅ Learned   |
| Vector / Matrix / Tensor | ✅ Learned   |
| `ndim`                   | ✅ Learned   |
| `shape`                  | ✅ Learned   |
| Transpose                | ✅ Learned   |
| Indexing                 | ✅ Learned   |
| Slicing                  | ✅ Learned   |
| Boolean Masking          | ✅ Learned   |
| `np.where()`             | ✅ Learned   |
| Fancy Indexing           | ✅ Learned   |
| Stacking                 | ✅ Learned   |
| Concatenation            | ✅ Learned   |
| Delete                   | ✅ Learned   |
| Advanced NumPy           | 🔄 Ongoing  |

---

## 🔗 Learning Roadmap

NumPy is part of a broader learning path toward Data Science and AI/ML:

```text
Python
  │
  ▼
NumPy
  │
  ▼
Pandas
  │
  ▼
Data Cleaning
  │
  ▼
Data Visualization
  │
  ▼
Exploratory Data Analysis
  │
  ▼
Machine Learning
  │
  ▼
Artificial Intelligence
```

---

## 🔮 Next Steps

After NumPy, the next major area is **Pandas**, focusing on:

* Series
* DataFrames
* Reading datasets
* Data selection
* Filtering
* Missing values
* Data cleaning
* Grouping
* Aggregation
* Data analysis

---

## 👨‍💻 Author

**Hamza Salahuddin**

Software Engineering Undergraduate
FAST-NUCES, Karachi

GitHub: [AuraHamza](https://github.com/AuraHamza)

---

## ⭐ Repository Purpose

This repository documents my practical journey with **NumPy and numerical computing in Python**.

It is continuously updated as I learn new concepts and apply them through examples and exercises.
