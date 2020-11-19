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

## Output:
Inside output_files/output.txt
```
{"user_id": 4, "name": "Ian Kehoe"}
{"user_id": 5, "name": "Nora Dempsey"}
{"user_id": 6, "name": "Theresa Enright"}
{"user_id": 8, "name": "Eoin Ahearn"}
{"user_id": 11, "name": "Richard Finnegan"}
{"user_id": 12, "name": "Christina McArdle"}
{"user_id": 13, "name": "Olive Ahearn"}
{"user_id": 15, "name": "Michael Ahearn"}
{"user_id": 17, "name": "Patricia Cahill"}
{"user_id": 23, "name": "Eoin Gallagher"}
{"user_id": 24, "name": "Rose Enright"}
{"user_id": 26, "name": "Stephen McArdle"}
{"user_id": 29, "name": "Oliver Ahearn"}
{"user_id": 30, "name": "Nick Enright"}
{"user_id": 31, "name": "Alan Behan"}
{"user_id": 39, "name": "Lisa Ahearn"}
```
