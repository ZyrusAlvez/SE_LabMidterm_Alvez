# Calculator App

A simple calculator application built with Python and CustomTkinter, developed as a Laboratory Midterm Exam for a Software Engineering course. The project demonstrates clean MVC architecture, automated unit testing, CI/CD pipeline configuration using GitHub Actions, and software quality analysis based on ISO/IEC 25010.

## Project Structure

```
SE_LabMidterm_Alvez/
├── src/
│   ├── model/
│   │   └── calculator.py       # Business logic (add, subtract, multiply, divide)
│   ├── controller/
│   │   └── controller.py       # Connects model and view
│   └── view/
│       └── app.py              # CustomTkinter UI
├── tests/
│   ├── test_add.py
│   ├── test_subtract.py
│   ├── test_multiply.py
│   └── test_divide.py
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI pipeline
├── quality_analysis.md         # ISO/IEC 25010 quality analysis
├── requirements.txt
└── README.md
```

## Key Highlights

- **MVC Pattern** — business logic, UI, and control flow are cleanly separated
- **Error Handling** — type validation and division by zero are handled at the model level
- **Unit Testing** — 17 tests across 4 files covering all operations and edge cases
- **CI/CD** — GitHub Actions pipeline runs all tests automatically on every push to `development`
- **Quality Analysis** — documents Functional Correctness and Fault Tolerance based on ISO/IEC 25010

## Prerequisites

- Python 3.11 or higher
- Git

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/ZyrusAlvez/SE_LabMidterm_Alvez.git
cd SE_LabMidterm_Alvez
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python src/view/app.py
```

## Running Unit Tests

Run all tests:
```bash
python -m pytest tests/ -v
```

Run a specific operation's tests:
```bash
python -m pytest tests/test_add.py -v
python -m pytest tests/test_subtract.py -v
python -m pytest tests/test_multiply.py -v
python -m pytest tests/test_divide.py -v
```

## CI/CD

This project uses GitHub Actions to automatically run the test suite on every push to `development`. The pipeline installs dependencies and runs `pytest` — if any test fails, the pipeline fails.

You can view the pipeline status in the **Actions** tab of the repository.

## Quality Analysis

See [quality_analysis.md](quality_analysis.md) for a detailed explanation of two ISO/IEC 25010 quality attributes — Functional Correctness and Fault Tolerance — and how the testing strategy and CI/CD pipeline support them.
