# My-Data-Science-Learning-Journey
Python and data science learning repository with hands-on exercises, practical projects, and comprehensive notes. Covering fundamentals to real-world applications.

# Python Fundamentals & Practice

A comprehensive collection of Python exercises and small projects covering core programming concepts, data structures, and practical applications.

## Overview

This repository contains Jupyter notebooks documenting my journey through Python fundamentals. Each notebook focuses on specific concepts with practical implementations and real-world examples.

## Contents

### [`practice and experiment 1.ipynb`](practice%20and%20experiment%201.ipynb)
Core Python concepts and data structure operations.

**Key Topics:**
- List operations: indexing, slicing, modification
- String manipulation and formatting
- Tuples and immutability
- List comprehensions
- Iterative patterns with `for` loops
- Built-in functions: `min()`, `max()`, `sum()`, `len()`

### [`Python task 1.ipynb`](Python%20task%201.ipynb)
Practical exercises focusing on problem-solving.

**Implementations:**
- Arithmetic calculations (area, age, discounts)
- String concatenation and formatting
- Type conversions
- Variable swapping techniques

### [`Python task 2.ipynb`](Python%20task%202.ipynb)
Advanced data manipulation and functional programming.

**Features:**
- Set operations
- Nested data structures
- List transformations and sorting algorithms
- Variable scope and the `global` keyword
- Function definitions
- List comprehensions for data transformation

### [`test and small projects 1.ipynb`](test%20and%20small%20projects%201.ipynb)
Mini-projects applying learned concepts.

**Projects:**
- **Calculator**: Basic arithmetic operations with operator detection
- **Login System**: Authentication with attempt limiting (3 tries)
- **Grade Converter**: Numeric to letter grade transformation
- **Data Filters**: Even numbers, positive/negative classification, word length filtering

## Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/python-fundamentals.git
cd python-fundamentals

# Install Jupyter Notebook
pip install notebook

# Launch
jupyter notebook
```

## Requirements

- Python 3.x
- Jupyter Notebook

## Usage

Open any `.ipynb` file in Jupyter to view code, execute cells, and experiment with examples.

```python
# Example: List manipulation
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)  # ['honda', 'yamaha', 'suzuki', 'ducati']
```

## Project Highlights

### Simple Calculator
```python
nums1 = 12
nums2 = 13
operator = "*"

if operator == "+":
    print(nums1 + nums2)
elif operator == "-":
    print(nums1 - nums2)
elif operator == "*":
    print(nums1 * nums2)
elif operator == "/":
    print(nums1 / nums2)
```

### Login System
```python
correct_username = "admin"
correct_password = "1234"

for i in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        print(f"Incorrect. {2 - i} attempts left.")
```

## Skills Demonstrated

- Data structure manipulation
- Control flow and conditional logic
- Function design and scope management
- Iterative problem-solving
- Code organization and documentation

## Notes

Some variable names and comments appear in Azerbaijani, reflecting my native language. Code logic follows standard Python conventions.

## License

MIT

---

*Learning Python one line at a time.*
