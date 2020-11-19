from math import sin, cos, radians

class Customer:
    EARTH_RADIUS = 6371.0
    # {"latitude": "52.833502", "user_id": 25, "name": "David Behan", "longitude": "-8.522366"}
    def __init__(self, latitude=None, longitude=None, user_id=None, name=None):
        self.latitude = latitude
        self.longitude = longitude
        self.user_id = user_id
        self.name = name
        
        if self.latitude and self.longitude:
            self.lat_radians = radians(self.latitude)
            self.lon_radians = radians(self.longitude)
        
    
    def create(self, customer_data):
        customers = []
        for meta_data in customer_data:
            
            customers.append(Customer(
                float(meta_data['latitude']),
                float(meta_data['longitude']),
                meta_data['user_id'],
                meta_data['name']
            ))
            

        return customers
    
    def filter_by_distance(self, o_lat, o_lon, all_customers, distance):
        if distance < 0. or len(all_customers) == 0:
            return []
        
        import numpy as np
        office_latitude = radians(o_lat)
        office_longitude = radians(o_lon)
        
        filtered_data = []
        for customer in all_customers:
            delta_lon = office_longitude - customer.lon_radians
            
            sin_prod = sin(office_latitude) * sin(customer.lat_radians)
            cos_prod = cos(office_latitude) * cos(customer.lat_radians) * cos(delta_lon)
            
            delta = np.arccos(sin_prod + cos_prod)
            
            delta_distance = self.EARTH_RADIUS * delta
            
            if delta_distance < distance:
                filtered_data.append(customer.to_json())
        
        return sorted(filtered_data, key = lambda i: i['user_id'])
            
    
    def to_json(self):
        return {
            "user_id": self.user_id,
            "name": self.name
        }
        