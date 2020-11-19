# Filter Customer by Distance

## Working:
- Reads the input file cutomer.txt provided in the spec.
- Create Customer object for each customer.
- Create a lists of Customer.
- Filter the Customer list by distance within.
- Distance between Office location and Customer location is calculated from the first formula mention in the Wiki link provided in the spec.
- Once the filterin is done, it is written into a separate directory path.


## Folder Structure:
```
.
├── project
│   ├── app
│   │   ├── controllers
│   │   │   ├── customer_controller.py
│   │   │   └── __pycache__
│   │   │       └── customer_controller.cpython-36.pyc
│   │   └── models
│   │       ├── customer.py
│   │       └── __pycache__
│   │           └── customer.cpython-36.pyc
│   ├── input_files
│   │   └── customers.txt
│   ├── output_files
│   │   └── output.txt
│   ├── __pycache__
│   │   ├── serve.cpython-36.pyc
│   │   ├── tests.cpython-36-pytest-6.1.2.pyc
│   │   ├── test_serve.cpython-36.pyc
│   │   └── test_serve.cpython-36-pytest-6.1.2.pyc
│   ├── requirements.txt
│   ├── serve.py
│   └── test_serve.py
└── README.md

```

## Installation:
Run the below command inside the root directory(Where the serve.py file is residing).
```
pip install -r requirements.txt
```

## Testing:
```
python -m unittest
```

## Execution:
```
python serve.py
```