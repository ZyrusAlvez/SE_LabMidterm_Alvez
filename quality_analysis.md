# Software Quality Analysis

## Overview

This document analyzes the software quality of the Calculator application using two relevant quality attributes defined by the **ISO/IEC 25010** standard. It also explains how the testing strategy and CI/CD pipeline support and improve those attributes.

---

## Quality Attribute 1: Functional Correctness

### Definition

Functional Correctness is a sub-characteristic of **Functional Suitability** in ISO/IEC 25010. It refers to the degree to which a system provides correct results with the needed degree of precision when given valid inputs — and handles invalid inputs predictably.

### Application to This Module

The `Calculator` model (`src/model/calculator.py`) is the core of this application. It exposes four operations: `add`, `subtract`, `multiply`, and `divide`. Each method is responsible for producing mathematically correct results and rejecting invalid inputs.

The `_validate` method enforces type correctness before any computation is performed:

- It raises a `TypeError` if either operand is not an `int` or `float`
- It explicitly rejects `bool` values, since Python treats `bool` as a subclass of `int`, which would otherwise silently produce incorrect results
- The `divide` method raises a `ZeroDivisionError` when the divisor is zero, preventing undefined mathematical behavior

This design ensures that the module behaves correctly across both valid and invalid input scenarios.

### How Testing Supports This Attribute

The test suite directly validates functional correctness through 17 unit tests split across four files:

| File | What it verifies |
|---|---|
| `test_add.py` | Correct sums for integers, floats, negatives, and type rejection |
| `test_subtract.py` | Correct differences including negative results |
| `test_multiply.py` | Correct products including multiplication by zero |
| `test_divide.py` | Correct quotients, division by zero, and type rejection |

Each test asserts an exact expected output or confirms that the correct exception is raised. This gives direct evidence that the module produces correct results and fails predictably on bad input — satisfying the Functional Correctness attribute.

---

## Quality Attribute 2: Fault Tolerance

### Definition

Fault Tolerance is a sub-characteristic of **Reliability** in ISO/IEC 25010. It refers to the degree to which a system continues to operate correctly in the presence of invalid inputs or unexpected conditions, rather than crashing or producing undefined behavior.

### Application to This Module

The Calculator application handles faults at two layers:

**Model layer** — `calculator.py` raises specific, descriptive exceptions (`TypeError`, `ZeroDivisionError`) instead of allowing Python to produce silent incorrect results or unhandled crashes.

**Controller layer** — `controller.py` catches those exceptions and routes them to the view via `set_error(e)`, displaying the error message inline on the calculator screen. The controller also calls `_reset_state()` after an error, restoring the application to a clean, operable state so the user can continue without restarting.

This two-layer approach means the application never crashes on bad input — it degrades gracefully and recovers automatically.

### How Testing Supports This Attribute

The test suite includes dedicated fault tolerance tests:

- `test_divide_by_zero` — confirms a `ZeroDivisionError` is raised, not a crash
- `test_add_string`, `test_subtract_string`, `test_multiply_string`, `test_divide_string` — confirm `TypeError` is raised for non-numeric inputs
- `test_add_bool` — confirms `bool` operands are explicitly rejected

These tests verify that the system handles faults in a controlled and predictable way, which is the core requirement of the Fault Tolerance attribute.

---

## How CI/CD Improves Reliability

The GitHub Actions pipeline (`.github/workflows/ci.yml`) is configured to trigger automatically on every push to the `main` branch. It performs two steps: installing dependencies and running the full test suite via `pytest`.

This improves reliability in the following ways:

**Prevents regression** — every code change is automatically tested before it can be considered stable. If a new change breaks an existing operation, the pipeline fails immediately and the developer is notified before the broken code affects anyone else.

**Enforces consistency** — the pipeline runs in a clean, isolated Ubuntu environment with a fixed Python version (3.11), eliminating "works on my machine" issues and ensuring the code behaves the same way regardless of the developer's local setup.

**Provides continuous verification** — rather than running tests manually and occasionally, the CI pipeline guarantees that tests are always run on every push. This means the `main` branch is always in a verified, tested state — directly supporting the Reliability quality attribute defined in ISO/IEC 25010.

A green check in GitHub Actions is evidence that all 17 tests pass and the application meets its defined functional and fault tolerance requirements.
