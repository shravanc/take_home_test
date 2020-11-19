# Filter Customer by Distance

## Working:
- Reads the input file cutomer.txt provided in the spec.
- Create Customer object for each customer.
- Create a lists of Customer.
- Filter the Customer list by distance within.
- Distance between Office location and Customer location is calculated from the first formula mention in the Wiki link provided in the spec.
- Once the filterin is done, it is written into a separate directory path.


## Folder Structure:
- requirements.txt  ## All the required libraries are mentioned.
- serve.py          ## Program starts here defining the required input arguments.
- test.py           ## All the test cases required for the program is written in here.
- app       
      - controllers
            - CustomerController.py  ## Business Logic is written in here, i.e. Filtering.
      - models
            - Customer.py            ## This represent a database objects. And provides necessary filtering methods.


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