from app.models.customer import Customer
import unittest
import os


from serve import run
from app.controllers.customer_controller import CustomerController
from app.models.customer import Customer


class TestServe(unittest.TestCase):
      
      def setUp(self):
            self.input_path = "./input_files/"
            self.output_path = "./output_files/output.txt"
            self.distance = '100.'
            self.office_latitude = '53.339428'
            self.office_longitude = '-6.257664'
            
            self.sample_data = {
                  "latitude": "52.833502", 
                  "user_id": 25, 
                  "name": "David Behan", 
                  "longitude": "-8.522366"
            }
      
      def test_customer_controller(self):
            
            obj = CustomerController(self.input_path)
            
            # Test total input customers
            self.assertEqual(len(obj.data), 32)

            # Test input has all the keys from the input
            self.assertEqual(list(obj.data[0].keys()), [
                  'latitude', 
                  'user_id',
                  'name',
                  'longitude',
                  ]
            )
                        
            # Test First Customer user id
            self.assertEqual(obj.data[0]['user_id'], 12)
            
            # Test if Controller creates same number of Cutomer Objects
            # after calling create() method
            obj.create()
            self.assertEqual(len(obj.customers), 32)
            
            # Test the type of Customer objects also the the directory structure
            print(type(obj.customers[0]))
            self.assertEqual(str(type(obj.customers[0])), "<class 'app.models.customer.Customer'>")
      
            # Test fetch_customer_by_distance() method
            obj.fetch_customer_by_distance(
                  float(self.office_latitude),
                  float(self.office_longitude),
                  float(self.distance)
            )
            self.assertEqual(len(obj.filtered_data), 16)
            
            # Test if the filtered data is in ascending order w.r.t user_id
            user_ids = [i['user_id'] for i in obj.filtered_data]
            self.assertEqual(user_ids, sorted(user_ids))


            # Test output_customer() method
            obj.output_customer(self.output_path)
            self.assertEqual(os.path.exists(self.output_path), True)

      
      def test_model(self):
            
            # Test create object
            customer = Customer(
                  float(self.sample_data['latitude']),
                  float(self.sample_data['longitude']),
                  self.sample_data['user_id'],
                  self.sample_data['name']
            )
            self.assertEqual(customer.name, self.sample_data['name'])
            
            # Test Check for radians
            from math import sin, cos, radians
            self.assertEqual(customer.lat_radians, radians(customer.latitude))
            self.assertEqual(customer.lon_radians, radians(customer.longitude))
            
            
            # Test filter_by_distance() method
            obj = CustomerController(self.input_path)
            obj.create()
            filtered_customers = customer.filter_by_distance(
                  float(self.office_latitude), 
                  float(self.office_longitude), 
                  obj.customers, 
                  float(self.distance)
            )
            self.assertEqual(len(filtered_customers), 16)

            # Test filter_by_distance() within 10KM distance
            filtered_customers = customer.filter_by_distance(
                  float(self.office_latitude), 
                  float(self.office_longitude), 
                  obj.customers, 
                  10.
            )
            self.assertEqual(len(filtered_customers), 0)
            
            # Test filter_by_distance() with distance in negative value
            filtered_customers = customer.filter_by_distance(
                  self.office_latitude, 
                  self.office_longitude, 
                  obj.customers, 
                  -10.
            )
            self.assertEqual(len(filtered_customers), 0)
      
            # Test to_json() method
            self.assertDictEqual(customer.to_json(), {
                  "user_id": self.sample_data['user_id'],
                  "name": self.sample_data['name']
            })
      
      def test_final(self):
            run()
            self.assertEqual(os.path.exists(self.output_path), True)
            
            
