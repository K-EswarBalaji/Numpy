# NumPy Math Toolkit

A simple Flask web app for matrix operations and basic statistics using NumPy.

## Features

- Matrix add, multiply, determinant, and inverse
- Mean, median, standard deviation, and variance
- Clean Bootstrap-based UI

## Requirements

- Python 3.9+
- Flask
- NumPy

## Setup

1) Create and activate a virtual environment (optional but recommended).
2) Install dependencies:

```
pip install flask numpy
```

## Run

```
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Input Format

- Matrix: rows separated by `;`, values separated by `,`
  - Example: `1,2;3,4`
- Vector/series: values separated by `,`
  - Example: `1,2,3,4`
- Scalar: single number

## Project Structure

- app.py: Flask app and NumPy operations
- templates/index.html: UI template
