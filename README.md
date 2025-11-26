# My Data Science Learning Journey

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.11+-blue" alt="Python Version" />
  <img src="https://img.shields.io/badge/Status-Learning-orange" alt="Status" />
  <img src="https://img.shields.io/badge/Notebooks-Jupyter-success" alt="Jupyter" />
</p>

Hands-on Python practice and mini-projects tracking my progress from fundamentals to practical applications.

## Overview
This repository contains Jupyter notebooks documenting Python concepts, exercises, and small projects. Each notebook focuses on specific topics with clear examples and explanations.

## Repository Structure
- `python learning journey/`
  - `practice and experiment 1.ipynb`: Core Python concepts and data structures
  - `Python task 1.ipynb`: Problem-solving with arithmetic, strings, and types
  - `Python task 2.ipynb`: Sets, functions, comprehensions, and sorting
  - `test and small projects 1.ipynb`: Mini-projects (calculator, login, grading, filters)
 - `examples/mini_apps.py`: Reusable functions refactored from notebook snippets

## Highlights
- **Data structures:** lists, tuples, sets; slicing, indexing, comprehensions
- **Control flow:** conditionals, loops, input handling
- **Functions:** signatures, scope, `global` usage
- **Mini-projects:** calculator, login attempts, grade converter, data filters

## Quick Start
```bash
# Clone the repository
git clone https://github.com/qurbaneliii/My-Data-Science-Learning-Journey.git
cd My-Data-Science-Learning-Journey

# Create and activate a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install Jupyter (minimal requirements)
pip install notebook

# Launch Jupyter Notebook
jupyter notebook
```

## Opening Notebooks
Open any `.ipynb` in `python learning journey/` and run cells sequentially. Where input is required, sample values are indicated in the surrounding markdown.

## Example
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
motorcycles
```

## Notes & Language
Some variable names/comments are in Azerbaijani (native language). All code follows standard Python conventions.

## Roadmap
- Add unit-test style checks for selected exercises
- Introduce NumPy/Pandas basics and simple EDA
- Expand mini-projects (CLI calculator, file I/O tasks)
 - Organize notebooks into `notebooks/` and add `tests/` directory
 - Add type hints and lightweight lint (ruff) configuration

## Contributing
Personal learning project. Suggestions via issues or PRs are welcome—focus on clarity and beginner-friendly explanations.

## Security Note
Login examples use plaintext credentials for demonstration only. In real applications store password hashes (e.g., `hashlib.pbkdf2_hmac`) and never hard-code secrets.

## License
Personal learning repository. Feel free to browse and learn; no warranty.


