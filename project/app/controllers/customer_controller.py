from math import radians
from app.models.customer import Customer

class CustomerController:
    def __init__(self, input):
        self.input = input
        self.data = []
        self._read_from_text()
        self.customer = Customer()
        self.customers = []
    
    def _read_from_text(self):
        import os
        for file in os.listdir(self.input):
            with open(os.path.join(self.input, file), mode="r") as fp:
                self._format_text_data(fp.readlines())
                        
    def _format_text_data(self, lines):
        import json
        for line in lines:
            self.data.append(json.loads(line))
            
    def create(self):
        self.customers = self.customer.create(self.data)
    
    def fetch_customer_by_distance(self, o_lat, o_lon, distance):
        self.filtered_data = self.customer.filter_by_distance(o_lat, o_lon, self.customers, distance)
        
        
    def output_customer(self, output_file):
        import json
        with open(output_file, mode="w") as fp:         
            for data in self.filtered_data:
                fp.write(json.dumps(data) + "\n")


