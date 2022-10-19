# Simple Calculator
A simple project for Pytest, Mocks, and Coverage course.

## Dependencies installation
``` bash
pip install -r requirements.txt
```

# Run tests
## Run all test in current directory
``` bash
pytest -v .
```

## You can run pytest for a specific file:
``` bash
pytest test_main.py
```

## Run everything, that has special_run in it
``` bash
pytest -v -k 'add'
```

## Run tests, that are decorated with the selected marker - marker_name
Run test with marker
``` bash
pytest -v -m custom_mark 
```

Run tests with no marker
``` bash
 pytest -v -m "not custom_mark"
```

# Coverage
Collect coverage information from pytest
``` bash
coverage run -m pytest
```
or
``` bash
coverage run --source="." --omit="*/venv/*" -m pytest
```

Show coverage report
``` bash
coverage report
```
