# Custom File I/O Library in Python

This project implements a simplified version of file I/O operations (`fopen`, `fread`, `fwrite`, `fclose`, `feof`, `ferror`) using Python's `os` module, mimicking low-level POSIX system calls.

It also includes a set of tests using `pytest` to verify correctness and simulate real-world file access scenarios.

---

## Project Structure

Python_testing/
├── app/
│ └── os_lib.py # Core file I/O library (business logic)
│
├── test/
│ └── lib_test.py # Pytest test cases for LibIO class
│
├── venv/ # Python virtual environment
│
├── .gitignore # Ignores venv, pycache.
├── README.md

Install dependencies:
```bash
pip install pytest

## How to Run the Tests
venv\Scripts\activate

# Run tests using pytest
pytest test/lib_test.py -v

OR

pytest -s test/lib_test.py -v

## Run first command of handleLongestContigousevenNumber.py
python handleLongestContigousevenNumber.py


 