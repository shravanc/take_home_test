from app.controllers.customer_controller import CustomerController
from app.models.customer import Customer
import argparse


if __name__ == "__main__":
      
      parser = argparse.ArgumentParser()
      
      parser.add_argument(
            '--input',
            dest='input',
            default='./input_files/',
            help='Input file to path'
      )
      
      parser.add_argument(
            '--output',
            dest='output',
            default='./output_files/output.txt',
            help='Writes the filtered customer to Output file'
      )
      
      parser.add_argument(
            '--distance',
            dest='distance',
            default=100.,
            help='Filter customers by specified distance in KM'
      )
      
      parser.add_argument(
            '--office_latitude',
            dest='o_lat',
            default=53.339428,
            help='Dublin Office Latitude'
      )
      
      parser.add_argument(
            '--office_longitude',
            dest='o_lon',
            default=-6.257664,
            help='Dublin Office Longitude'
      )
      
      
      args = parser.parse_args()
      obj = CustomerController(args.input)
      obj.create()
      obj.fetch_customer_by_distance(args.o_lat, args.o_lon, args.distance)
      obj.output_customer(args.output)
      
      
      """
      customer.read_from_text()
      customer.find_within_100_miles()
      user_ids = customer.fetch_user_ids()
      
      print(user_ids)
      """